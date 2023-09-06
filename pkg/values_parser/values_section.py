from pkg.comment_parser.comments_parser import CommentParser
from pkg.values_parser.table_formate.formate_table import formate_description, format_raw, generate_html_header, \
    start_table, end_table
from pkg.helm.utils import read_yaml_file
from pkg.values_parser.values_parser_utils import apply_custom_css, remove_element_by_key, append_element_to_table, \
    insert_into_target_table, count_dots, check_for_ignore, extract_the_default_from_the_comment, \
    remove_and_get_default


def extract_top_level_entries(data):
    """
    Extracts top-level entries from a dictionary of data.

    This function iterates through the provided dictionary and extracts each key-value pair,
    creating a structured list of dictionaries where each dictionary contains the title (key) and
    value of the entry.

    Args:
        data (dict): A dictionary containing the data to be processed.

    Returns:
        list: A list of dictionaries, each containing 'title' (key) and 'value' (value) entries.

    Example:
        data = {
            'key1': 'value1',
            'key2': 'value2'
        }
        entries = extract_top_level_entries(data)
        # Output: [{'title': 'key1', 'value': 'value1'}, {'title': 'key2', 'value': 'value2'}]
    """
    top_level_entries = []

    # Iterate through the dictionary items and create a structured list of entries
    for key, value in data.items():
        top_level_entries.append({
            "title": key,       # The title (key) of the entry
            "value": value      # The value of the entry
        })

    return top_level_entries


def get_entry_value(value, prefix, key_to_comment_map):
    """
    Recursively formats and structures a value along with its comments for display in a Markdown table.

    This function takes a value, its associated prefix (title), and comments map, and formats them
    to be presented as a structured dictionary suitable for Markdown table representation. It handles
    different types of values, including lists and dictionaries, and applies comments accordingly.

    Args:
        value: The value to be formatted (could be a scalar, list, or dictionary).
        prefix (str): The prefix/title of the entry.
        key_to_comment_map (dict): A dictionary mapping prefixes to their comments.

    Returns:
        dict: A dictionary containing formatted value, comments, and metadata for Markdown table.

    Example:
        value = {
            'key1': 'value1',
            'key2': [1, 2, 3]
        }
        prefix = 'example'
        comments_map = {
            'example': {'beforeComments': 'This is an example value', 'afterComments': []},
            'example.key1': {'beforeComments': 'Comment for key1', 'afterComments': []},
            'example.key2': {'beforeComments': 'Comment for key2', 'afterComments': ['Comment1', 'Comment2']}
        }
        formatted_value = get_entry_value(value, prefix, comments_map)
        # Output: {
        #     'title': 'example',
        #     'value': {
        #         'key1': {'title': 'example.key1', 'value': 'value1', 'comments': 'Comment for key1', ...},
        #         'key2': [{'title': 'example.key2[0]', 'value': 1, 'comments': 'Comment for key2', ...}, ...]
        #     },
        #     'comments': 'This is an example value',
        #     'new_table': False,
        #     'custom_css': '',
        #     'end_element': True
        # }
    """
    list_comments = key_to_comment_map[prefix]
    if isinstance(value, list):
        formatted_items = [
            {
                'title': prefix,
                'value': value,
                'comments': list_comments['beforeComments'],
                'new_table': False,
                'custom_css': '',
                'end_element': True,
                'line_number': list_comments['line_number'],
                'is_section': False
            }
        ]
        for index, item in enumerate(value):
            comments = list_comments.get('afterComments', [])[index] if index < len(
                list_comments.get('afterComments', [])) else []

            formatted_items.append({
                'title': f"{prefix}[{index}]",
                'value': item,
                'comments': comments,
                'new_table': False,
                'custom_css': '',
                'line_number': list_comments['line_number'],
                'end_element': True,
                'is_section': False
            })
        return formatted_items

    elif isinstance(value, dict):
        formatted_entries = [
            {
                'title': prefix,
                'value': value,
                'comments': list_comments['beforeComments'],
                'new_table': False,
                'custom_css': '',
                'line_number': list_comments['line_number'],
                'end_element': True,
                'is_section': False
            }
        ]
        for k, v in value.items():
            formatted_entry = get_entry_value(v, f"{prefix}.{k}", key_to_comment_map)
            if formatted_entry:
                formatted_entries.append(formatted_entry)
        return formatted_entries

    else:
        comments = key_to_comment_map[prefix]
        return [{
            'title': prefix,
            'value': value,
            'comments': comments['beforeComments'],
            'new_table': False,
            'custom_css': '',
            'line_number': comments['line_number'],
            'end_element': True,
            'is_section': False
        }]


def convert_key_to_markdown(row, ignore_none_description=False):
    """
    Recursively converts a structured dictionary into markdown content.

    This function takes a structured dictionary representing a Markdown table and converts it into
    formatted markdown content. It handles nested dictionaries and lists, extracting values, comments,
    and custom CSS information to generate the appropriate markdown representation.

    Args:
        row (dict or list): A dictionary or list containing structured data to be converted.

    Returns:
        str: Formatted markdown content.
    """
    returned_raws = ''

    # Handle lists: Iterate through each element in the list and recursively convert
    # its contents to markdown content
    if isinstance(row, list):
        for v in row:
            returned_raws += convert_key_to_markdown(v, ignore_none_description)
    # Handle dictionaries:
    elif isinstance(row, dict):

        if check_for_ignore(row['comments']):
            return ''

        target_comment = remove_and_get_default(row['comments'])
        if target_comment:
            row['value'] = extract_the_default_from_the_comment(target_comment)

        if row['end_element']:
            # If it's an end element, format and return the row's value as markdown content
            return format_raw(row['value'], row['title'], row['comments'], row['custom_css'], ignore_none_description, row['line_number'])
        else:
            # If it's not an end element, recursively convert the value part of the dictionary
            # and continue the process
            return convert_key_to_markdown(row['value'], ignore_none_description)

    return returned_raws


def convert_table_to_markdown(table, level=1, ignore_none_description=False):
    """
    Recursively converts a structured table to format markdown content.

    This function takes a structured table (dictionary) and recursively converts it into formatted
    markdown content. It handles nested dictionaries and lists, creating Markdown tables and headers.

    Args:
        table (dict): A structured dictionary representing a Markdown table.
        Level (int, optional): The nesting level of the table (default is 1).

    Returns:
        str: Formatted markdown content.

    Example:
        structured_table = {
            'title': 'example',
            'value': [
                {'title': 'example.key1', 'value': 'value1', ...},
                {'title': 'example.key2[0]', 'value': 1, ...},
                ...

            'Comments': 'This is an example value',
            'new_table': True,
            'custom_css': '',
            'end_element': False,
        }
        markdown_content = convert_table_to_markdown(structured_table)
        # Output: Formatted markdown content representing the structured table.
        :param level:
        :param table:
        :param ignore_none_description:
    """

    if check_for_ignore(table['comments']):
        return ''

    markdown_content = ""

    table_title = table.get('title', '') if not table.get('is_section', False) else level * '-' + '> ' + table.get('title', '')

    table_title = generate_html_header(level, table_title)
    markdown_content += table_title

    if not table['is_section']:
        # If there are no intermediate tables, add table description and start table formatting
        table_description = formate_description(table['comments'])
        markdown_content += table_description
        markdown_content += start_table(table['custom_css'])

    for row in table['value']:

        if isinstance(row, list):
            # If the row is a list, iterate through its elements and convert each recursively
            for v in row:
                markdown_content += convert_key_to_markdown(v, ignore_none_description)
        elif isinstance(row, dict):
            if row['new_table']:
                # If the row indicates a new nested table, recursively convert it
                markdown_content += convert_table_to_markdown(row, level + 1, ignore_none_description)
            else:
                # If it's not a new table, convert the row using convert_key_to_markdown
                formatted_value = convert_key_to_markdown(row, ignore_none_description)
                markdown_content += formatted_value

    if not table['is_section']:
        # Close the current table formatting
        markdown_content += end_table

    return markdown_content


def split_and_merge_tables(values_table, transfers_map):
    """
    Splits and merges tables based on a transfers map and the number of dots in transfer paths.

    This function takes a values table and a transfers map, sorts the transfers map based on the count of dots
    in transfer paths, and then splits and merges tables according to the transfers map.

    Args:
        values_table (list): The list of structured tables to be split and merged.
        transfers_map (list): The transfers map containing transfer and table paths.

    Returns:
        list: The sorted list of merged tables after splitting and merging.

    Example:
        merged_tables = split_and_merge_tables(values_table, transfers_map)
    """
    splitted_tables = []

    # Sort the transfers_map based on the count of dots in the transfer path
    transfers_map = sorted(transfers_map, key=lambda x: count_dots(x['transfer']))

    for transfer in transfers_map:
        is_new_global_table = True
        from_table = transfer['table']
        to_table = transfer['transfer']

        # Remove the element from the original values_table based on the from_table path
        target_table = remove_element_by_key(from_table, values_table[0]['value'])

        if target_table is None:
            print(f"Warning: The table {from_table} is not found or maybe transferd in previous step in the values.yaml file. ")
            continue

        # Search for the target_table within the current values_table and already splitted_tables
        for table in values_table + splitted_tables:
            if to_table.startswith(table['title']):
                is_new_global_table = False
                target_table['new_table'] = True
                target_table['end_element'] = False
                insert_into_target_table(to_table, target_table, table)
                break

        if is_new_global_table:
            # If the target table isn't found in existing tables, create a new intermediate table
            # important note here when we insert new global table you should be take care of the more depth sections
            target_table['new_table'] = True
            target_table['end_element'] = False
            new_main_dir = {
                'title': to_table.split('.', 1)[0],
                'comments': [],
                'value': [],
                'new_table': False,
                'custom_css': '',
                'end_element': False,
                'is_section': True
            }
            append_element_to_table(new_main_dir, target_table, to_table)
            splitted_tables.append(new_main_dir)

    # Sort the global and split tables based on the 'new_table' property
    sorted_global = sorted(values_table, key=lambda x: x['new_table'])
    sorted_splitted_tables = sorted(splitted_tables, key=lambda x: x['new_table'])

    # Return the combined list of sorted global and split tables
    return sorted_global + sorted_splitted_tables


def generate_markdown_output(entries, key_to_comment_map, transfers_map, custom_css_map, ignore_none_description):
    """
    Generates markdown content by processing entries, applying custom CSS, and merging tables.

    This function takes entries, key-to-comment map, transfer map, and custom CSS map, processes the entries to
    create structured tables, applies custom CSS to the tables, and then merges tables based on transfers map.

    Args:
        entries (list): List of entry objects containing title and value.
        key_to_comment_map (dict): Map of titles to comments.
        transfers_map (list): List of transfer mappings between tables.
        custom_css_map (list): List of custom CSS mappings for tables.

    Returns:
        str: The generated markdown content.

    Example:
        markdown_output = generate_markdown_output(entries, key_to_comment_map, transfers_map, custom_css_map)
        :param entries:
        :param key_to_comment_map:
        :param transfers_map:
        :param custom_css_map:
        :param ignore_none_description:
    """
    values_table = []

    # Process entries and create structured tables
    for entry in entries:
        title = entry['title']
        title_comments = key_to_comment_map[entry['title']]['beforeComments']
        title_value = get_entry_value(value=entry['value'],
                                      prefix=entry['title'],
                                      key_to_comment_map=key_to_comment_map)
        values_table.append({
            'title': title,
            'comments': title_comments,
            'value': title_value,
            'new_table': True,
            'custom_css': '',
            'end_element': False,
            'line_number': key_to_comment_map[title]['line_number'],
            'is_section': False
        })

    # Apply custom CSS to the structured tables
    apply_custom_css(custom_css_map, values_table)

    # Create a global table containing the structured tables
    values_table = [{
        'title': 'global',
        'comments': '',
        'value': values_table,
        'new_table': True,
        'custom_css': '',
        'end_element': False,
        'is_section': True
    }]

    # Split and merge tables based on transfer map
    final_tables = split_and_merge_tables(values_table, transfers_map)

    markdown_content = ""
    # Convert each merged table to markdown content
    for table in final_tables:
        markdown_content += convert_table_to_markdown(table, ignore_none_description)

    return markdown_content


def read_and_print_values(values_path, ignore_none_description, sort='AlphaNum'):
    """
    Reads values from a YAML file, processes them, and generates markdown content for printing.

    This function reads data from a YAML file, processes the top-level entries, extracts comments and transfers map
    using CommentParser, and generates markdown content for printing the structured tables.

    Args:
        values_path (str): Path to the YAML file containing values.
        sort (str): Sorting option for top-level entries. Default is 'AlphaNum'.

    Returns:
        str: The generated markdown content for printing.

    Example:
        markdown_output = read_and_print_values('values.yaml', sort='AlphaNum')
        :param ignore_none_description:
    """
    # Read data from the YAML file
    values_data = read_yaml_file(values_path)

    if values_data is None:
        return ''

    # Extract top-level entries from the values data
    top_level_entries = extract_top_level_entries(values_data)

    if sort == 'AlphaNum':
        # Sort top_level_entries alphabetically by 'title' key
        top_level_entries = sorted(top_level_entries, key=lambda x: x['title'])

    # Create an instance of the CommentParser class
    comment_parser = CommentParser()

    # Call the get_comments_map method with the values_path to extract comments, transfers map, and custom CSS map
    key_to_comment_map, transfers_map, custom_css_map = comment_parser.get_comments_map(values_path)

    # Generate markdown content using the extracted data
    markdown_content = generate_markdown_output(top_level_entries, key_to_comment_map, transfers_map,
                                                custom_css_map, ignore_none_description)

    return markdown_content
