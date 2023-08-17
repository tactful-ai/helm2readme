from pkg.cmd.command_line import get_ignore_non_descriptions


def remove_special_chars(value):
    if isinstance(value, str):
        return value.replace('|', r'\|').strip()
    elif isinstance(value, dict):
        escaped_dict = {}
        for key, val in value.items():
            escaped_dict[key] = remove_special_chars(val)
        return escaped_dict
    else:
        return value


def get_raw_value(value, prefix, value_type, description='', custom_css=""):
    value = remove_special_chars(value)

    if description:
        description_code = f"<code>{description}</code>"
    else:
        description_code = ""

    raw = (
        f"<tr style=\"{custom_css}\" ><td>{prefix}</td>"
        f"<td>{value_type}</td>"
        f"<td><code>`{value}`</code></td>"
        f"<td>{description_code}</td></tr>"
    )
    return raw


def extract_type(value, comments=None):
    if comments is None:
        comments = []

    extracted_type = None

    for comment in comments:
        if '(' in comment and ')' in comment:
            start = comment.index('(') + 1
            end = comment.index(')', start)
            extracted_type = comment[start:end].strip()
            break  # Stop after finding the first comment with type information

    if extracted_type is None:
        extracted_type = type(value).__name__

    return extracted_type


def extract_text(comment):
    prefix = "-- ("
    suffix = ")"
    start = comment.find(prefix)
    end = comment.find(suffix, start + len(prefix))

    if start != -1 and end != -1:
        return comment[end + 1:].strip()
    else:
        return comment


def formate_description(comments):
    formatted_comments = []  # Create an empty list to store the modified comments
    for comment in comments:
        des_coment = comment.strip()  # Remove leading and trailing whitespace
        des_coment = des_coment.strip('-')  # Remove leading and trailing dashes
        formatted_comment = extract_text(des_coment)  # Extract text using the function
        formatted_comments.append(formatted_comment)  # Add the modified comment to the list

    numbered_comments = [f"{i + 1}. {comment}" for i, comment in enumerate(formatted_comments)] if len(
        formatted_comments) > 1 else formatted_comments
    return "  <br/><br/>".join([f"{comment}" for comment in numbered_comments])


def format_raw(value, prefix, comments, custom_css=""):
    extracted_type = extract_type(value, comments)
    description = formate_description(comments)

    ignore_none_description = get_ignore_non_descriptions()
    if ignore_none_description and not description:
        return ""

    return get_raw_value(value, prefix, extracted_type, description, custom_css)


def format_value_for_table(value, prefix="", key_to_comment_map=None):
    if isinstance(value, list):
        formatted_items = []
        list_comments = key_to_comment_map[prefix]
        formatted_items.append(format_raw(value, prefix, list_comments['beforeComments']))
        for index, item in enumerate(value):
            formatted_item = format_raw(value, f"{prefix}[{index}]", list_comments['afterComments'][index])
            formatted_items.append(formatted_item)
        return "\n".join(formatted_items)

    elif isinstance(value, dict):
        formatted_entries = []
        list_comments = key_to_comment_map[prefix]
        formatted_entries.append(format_raw(value, prefix, list_comments['beforeComments']))
        for k, v in value.items():
            formatted_entry = format_value_for_table(v, f"{prefix}.{k}", key_to_comment_map)
            if formatted_entry:
                formatted_entries.append(formatted_entry)
        return "\n".join(formatted_entries)

    else:
        comments = key_to_comment_map[prefix]
        return format_raw(value, prefix, comments['beforeComments'])


def generate_html_header(tag_number, text):
    if tag_number < 1:
        raise ValueError("Tag number should be between 1 and 6")

    if tag_number > 6:
        html_tag = f"<p>{text}</p>"
    else:
        html_tag = f"<h{tag_number}>{text}</h{tag_number}>"

    return html_tag

