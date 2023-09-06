import markdown


def remove_special_chars(value):
    """
    Removes special characters from the provided value.

    Args:
        value: The value from which special characters need to be removed.

    Returns:
        The value with special characters replaced or stripped.
    """
    if isinstance(value, str):
        # If the value is a string, replace '|' with '\|' to escape for HTML rendering
        return value.replace('|', r'\|').strip()
    elif isinstance(value, dict):
        # If the value is a dictionary, iterate through key-value pairs and recursively call the function
        escaped_dict = {}
        for key, val in value.items():
            escaped_dict[key] = remove_special_chars(val)
        return escaped_dict
    else:
        # For other types of values, no special character removal is needed
        return value


# Function to get a formatted raw value for a markdown table
def get_raw_value(value, prefix, value_type, description='', custom_css=""):
    """
    Formats the provided value, type, and description into a raw HTML table row.

    Args:
        value: The value to be displayed in the table.
        prefix: The key or identifier associated with the value.
        value_type: The data type of the value.
        description: Optional description of the value (can include HTML code).
        custom_css: Optional custom CSS style for the table row.

    Returns:
        A formatted HTML table row containing the key, type, value, and description.
    """
    # Remove any special characters from the value
    value = remove_special_chars(value)

    # If a description is provided, format it as a <code> HTML element
    if description:
        description_code = f"{description}"
    else:
        description_code = ""

    # Construct the raw HTML table row
    raw = (
        f"<tr style=\"{custom_css}\" ><td>{prefix}</td>"
        f"<td>{value_type}</td>"
        f"<td><code>`{value}`</code></td>"
        f"<td>{description_code}</td></tr>"
    )
    return raw


# Function to extract the type information from comments or value itself
def extract_type(value, comments=None):
    """
    Extracts the data type of the provided value based on comments or the value itself.

    Args:
        value: The value for which the data type needs to be extracted.
        comments: Optional list of comments to extract type information.

    Returns:
        The extracted data type as a string.
    """
    # Initialize the extracted type as None
    extracted_type = None

    # Loop through the comments to find type information
    for comment in comments:
        if comment.startswith(' -- ('):
            # Extract type information enclosed in parentheses
            start = comment.index('(') + 1
            end = comment.index(')', start)
            extracted_type = comment[start:end].strip()
            break  # Stop after finding the first comment with type information

    # If type information is not found in comments, use the type of the value
    if extracted_type is None:
        extracted_type = type(value).__name__

    return extracted_type


# Function to extract text from a comment
def extract_text(comment):
    """
    Extracts text from a comment enclosed within parentheses.

    Args:
        comment: The comment containing the text enclosed in parentheses.

    Returns:
        The extracted text from the comment.
    """
    prefix = "-- ("  # Prefix indicating start of text
    suffix = ")"  # Suffix indicating end of text

    # Find the start and end of the text within parentheses
    start = comment.find(prefix)
    end = comment.find(suffix, start + len(prefix))

    if start != -1 and end != -1:
        # Return the text between the parentheses
        return comment[end + 1:].strip()
    else:
        # Return the original comment if text is not found
        return comment


# Function to format comments for description
def formate_description(comments):
    """
    Formats a list of comments into a structured HTML description.

    Args:
        comments: A list of comments to be formatted.

    Returns:
        A formatted HTML description.
    """
    # Initialize an empty list to store the modified comments
    formatted_comments = []

    # Iterate through the comments and format them
    for comment in comments:
        # Remove leading and trailing whitespace
        des_comment = comment.strip()

        # Remove leading and trailing dashes
        des_comment = des_comment.strip('-')

        # Extract text from the comment using the extract_text function
        formatted_comment = extract_text(des_comment)

        # Add the modified comment to the list
        formatted_comments.append(formatted_comment)

    # If there are multiple comments, number them; otherwise, keep the single comment
    numbered_comments = [f"{i + 1}. {comment}" for i, comment in enumerate(formatted_comments)] if len(
        formatted_comments) > 1 else formatted_comments

    description = "  <br/><br/>".join([f"{comment}" for comment in numbered_comments])
    if description:
        description = "<code>" + description + "</code>"

    markdown_description = markdown.markdown(description)

    # Join the formatted comments with line breaks
    return markdown_description


def formate_key(key, line_number):
    """
    formate the key to be link to the line number in the file

    Args:
        key: the key string.
        line_number: the line number in the file.

    Returns:
        A formatted HTML description.
    """
    if(line_number < 0):
        return key

    markdown_key = f"\n\n[{key}](./values.yaml#L{line_number})\n\n"

    return markdown_key


# Function to format a raw value with description and optional CSS
def format_raw(value, prefix, comments, custom_css="", ignore_none_description=False, line_number=-1):
    """
    Formats the provided value along with its description into a raw HTML table row.

    Args:
        value: The value to be displayed in the table.
        prefix: The key or identifier associated with the value.
        comments: List of comments to be used for description.
        custom_css: Optional custom CSS style for the table row.

    Returns:
        A formatted HTML table row containing the key, type, value, and description.
    """
    # Extract the data type from comments or the value itself
    extracted_type = extract_type(value, comments)

    # Format the description using the formate_description function
    description = formate_description(comments)

    # Format the key using the formate_key function
    prefix = formate_key(prefix, line_number)

    # Check if ignore_none_description is enabled and no description is provided
    if ignore_none_description and not description:
        return ""

    # Generate the formatted HTML table row using get_raw_value function
    return get_raw_value(value, prefix, extracted_type, description, custom_css)


# Function to generate an HTML header tag
def generate_html_header(tag_number, text):
    """
    Generates an HTML header tag with the specified tag number and text.

    Args:
        tag_number: The level of the header tag (1 to 6).
        text: The text content of the header.

    Returns:
        An HTML header tag.
    """
    # Validate the tag number
    if tag_number < 1:
        return f"<h1>{text}</h1>"

    # Generate the appropriate HTML tag based on the tag number
    if tag_number > 6:
        html_tag = f"<p>{text}</p>"
    else:
        html_tag = f"<h{tag_number}>{text}</h{tag_number}>"

    return html_tag


# Function to start an HTML table
def start_table(custom_css=""):
    """
    Generates the HTML code to start an HTML table.

    Args:
        custom_css: Optional custom CSS style for the table.

    Returns:
        The HTML code to start an HTML table.
    """
    return f"""
<table style=\"{custom_css}\">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
"""


end_table = """
</table>\n
"""
