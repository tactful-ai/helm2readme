import yaml


def read_yaml_file(yaml_file_path):
    """
    Reads and loads content from a YAML file.

    Args:
        yaml_file_path (str): The path to the YAML file.

    Returns:
        dict: A dictionary containing the parsed YAML data.
    """
    with open(yaml_file_path, "r") as values_file:
        values_data = yaml.load(values_file, Loader=yaml.FullLoader)
        return values_data


def write_file(file_content, output_path):
    """
    Writes content to a file.

    Args:
        file_content (str): The content to be written to the file.
        output_path (str): The path of the output file.
    """
    with open(output_path, "w") as output_file:
        output_file.write(file_content)


def count_indentation(line):
    """
    Counts the number of leading spaces in a line to determine its indentation level.

    Args:
        line (str): The line of text to analyze.

    Returns:
        int: The number of leading spaces indicating the indentation level.
    """
    return len(line) - len(line.lstrip())


def get_closing_bracket(opening_bracket):
    """
    Retrieves the corresponding closing bracket for a given opening bracket.

    Args:
        opening_bracket (str): The opening bracket character.

    Returns:
        str: The corresponding closing bracket character, or 'Invalid bracket' if unmatched.
    """
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    return brackets.get(opening_bracket, 'Invalid bracket')
