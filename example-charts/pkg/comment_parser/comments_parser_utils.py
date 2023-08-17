from pkg.helm.utils import get_closing_bracket


def print_key_comments(key_to_comment_map):
    """
    Prints comments associated with keys in the key_to_comment_map.

    Args:
        key_to_comment_map (dict): A dictionary mapping keys to comments.

    Returns:
        None
    """
    for key, comments_dict in key_to_comment_map.items():
        print("Key:", key)
        print("Before Comments:", comments_dict['before_comments'])
        print("After Comments:", comments_dict['after_comments'])
        print()


def find_next_non_empty_line(yaml_file, current_line):
    """
    Finds the next non-empty line in the YAML file.

    Args:
        yaml_file: The YAML file object.
        current_line (str): The current line in the file.

    Returns:
        str: The next non-empty line in the file.
    """
    line = current_line
    stripped_line = line.strip()
    while len(stripped_line) == 0:
        line = next(yaml_file, '')
        stripped_line = line.strip()
    return line


def extract_closing_tags_or_characters(line):
    """
    Extracts closing tags or characters from a given line.

    Args:
        line (str): The line to extract from.

    Returns:
        str or None: The extracted closing tag or characters, or None if not found.
    """
    line = line.strip()

    if line.startswith('<') and '>' in line:
        opening_tag = line.split('>')[0] + '>'
        tag_name = opening_tag[1:-1]  # Extract the tag name
        closing_tag = f"</{tag_name}>"
        return closing_tag
    else:
        # Count the number of consecutive opening brackets
        num_opening_brackets = 0
        for char in line:
            if char in '[{':
                num_opening_brackets += 1
            else:
                break

        if num_opening_brackets > 0:
            closing_brackets = ']' * num_opening_brackets if line.startswith('[') else '}' * num_opening_brackets
            return closing_brackets
        else:
            return None  # Return None if the line doesn't start with a recognized opening tag, bracket, or character


def find_line_with_closing_bracket(current_line, yaml_file, target_closing_bracket):
    """
    Finds the line containing the target closing bracket.

    Args:
        current_line (str): The current line in the file.
        yaml_file: The YAML file object.
        target_closing_bracket (str): The target closing bracket to find.

    Returns:
        str: The line containing the target closing bracket.
    """
    while True:
        if target_closing_bracket in current_line:
            return current_line
        else:
            current_line = next(yaml_file, '')


def extract_text_from_brackets(comment, bracket):
    """
    Extracts text enclosed within a specific bracket pair.

    Args:
        comment (str): The comment containing the bracket pair.
        bracket (str): The opening bracket character.

    Returns:
        str or None: The extracted text from within the brackets, or None if not found.
    """
    prefix = bracket
    suffix = get_closing_bracket(bracket)
    start = comment.find(prefix)
    end = comment.find(suffix, start + len(prefix))

    if start != -1 and end != -1:
        return comment[start + len(prefix):end].strip()
    else:
        return None


def get_key(keys_array):
    return '.'.join(keys_array)
