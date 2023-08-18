def get_element_by_key(key, table):
    """
    Recursively searches for an element with a specific key in a nested dictionary or list.

    This function searches for an element with a specific key within a structured dictionary or list.
    It traverses through the nested structure and returns the element if found.

    Args:
        key (str): The key/title to search for.
        table (dict or list): The structured dictionary or list to search within.

    Returns:
        dict or None: The dictionary element matching the key, or None if not found.
    """
    if isinstance(table, dict):
        # If the current element is a dictionary, check if its title matches the target key
        if table['title'] == key:
            return table
    else:
        # If the current element is a list, iterate through each element (row) within the list
        for row in table:
            if isinstance(row, dict):
                # If the row is a dictionary, check if its title matches the target key
                if row['title'] == key:
                    return row
            elif isinstance(row, list):
                # If the row is a list, recursively call the function for each nested element (v)
                for v in row:
                    # Recursively search for the key within the nested element (v)
                    if get_element_by_key(key, v):
                        return v
    return None


def apply_custom_css(custom_css_map, values_table):
    """
    Applies custom CSS styles to specific tables in a structured values table.

    This function iterates through a list of custom CSS mappings and applies the corresponding styles
    to specific tables within a structured values table. It supports wildcard matching and traverses
    the nested structure to find the appropriate table to apply the CSS to.

    Args:
        custom_css_map (list): A list of custom CSS mappings, each containing 'table' and 'css' keys.
        values_table (list): A structured values table containing nested dictionaries and lists.

    Returns:
        None
    """
    for custom_css in custom_css_map:
        if custom_css['table'] == '*':
            # Apply custom CSS to all tables in the values_table
            for table in values_table:
                table['custom_css'] += custom_css['css']
            continue

        table_title = custom_css['table']
        css = custom_css['css']

        # Initialize the variable that will track the path to the target table
        target_element = values_table
        if '.' in table_title:
            # If table_title contains dots, traverse through the nested structure
            # to find the target table and apply the custom CSS
            for table in target_element:
                if table['title'] == table_title.split('.', 1)[0]:
                    target_element = table['value']
                    break

            # Get the target element by key and apply the custom CSS
            target_element = get_element_by_key(table_title, target_element)
            target_element['custom_css'] += css
        else:
            # If table_title doesn't contain dots, apply the custom CSS to the
            # table with a matching title within the current level
            for table in target_element:
                if table['title'] == table_title.split('.', 1)[0]:
                    table['custom_css'] += css


def process_string(level, key):
    """
    Extracts the key portion based on the nesting level.

    This function extracts the key portion of a string based on the provided nesting level.
    It calculates the number of dots (.) in the key and returns the portion up to the specified level.

    Args:
        level (int): The nesting level.
        key (str): The original string key.

    Returns:
        str: The extracted key portion.

    Example:
        original_key = 'example.key1.key2'
        extracted_key = process_string(2, original_key)
        # Output: 'example.key1'
    """
    num_dots = key.count('.')

    if level > num_dots:
        # If the level is greater than the number of dots, return the full key
        return key
    else:
        # Otherwise, split the key at the specified level and return the portion up to that level
        return key.split('.', level)[0]


def remove_element_by_key(key, table, level=1):
    """
    Recursively removes an element with a specific key from a nested dictionary or list.

    This function recursively searches for an element with a specific key within a structured dictionary
    or list and removes it. It supports nested structures and maintains the integrity of the structure.

    Args:
        key (str): The key/title of the element to be removed.
        table (dict or list): The structured dictionary or list to search within.
        level (int, optional): The nesting level of the structure (default is 1).

    Returns:
        dict or None: The removed dictionary element, or None if not found.
    """
    for row in table:
        if isinstance(row, dict):
            if row.get('title') == key:
                # Remove the matching element from the table and return it
                table.remove(row)
                return row
            elif row.get('title') == process_string(level, key):
                # If the key matches the processed string, search within the nested 'value'
                return remove_element_by_key(key, row['value'], level + 1)
        elif isinstance(row, list):
            if row[0].get('title') == key:
                # Remove the matching element from the table and return it
                table.remove(row)
                return {
                    'title': key,
                    'comments': [],
                    'value': row,
                    'new_table': False,
                    'custom_css': '',
                    'end_element': False,
                    'is_section': False
                }

            for v in row:
                # Recursively search within the nested list or dictionary
                removed_element = remove_element_by_key(key, v, level + 1)
                if removed_element:
                    return removed_element
    return None


def remove_first_occurrence(substring, main_string):
    """
    Removes the first occurrence of a substring from a main string.

    This function finds and removes the first occurrence of a specified substring from a main string.

    Args:
        substring (str): The substring to be removed.
        main_string (str): The main string from which to remove the substring.

    Returns:
        str: The main string with the first occurrence of the substring removed.
    """
    index = main_string.find(substring)
    if index != -1:
        # If the substring is found in the main string
        new_string = main_string[:index] + main_string[index + len(substring):]
        return new_string
    else:
        # If the substring is not found, return the original main string
        return main_string


def append_element_to_table(table, element, sections):
    """
    Appends an element to a structured table based on its title path.

    This function appends an element to a structured table by determining its position based on the title path.
    It creates intermediate nested tables as needed and inserts the element at the appropriate location.

    Args:
        table (dict): The structured table to which the element should be appended.
        element (dict): The element to be appended to the table.

    Returns:
        None
        :param sections:
    """

    if table['title'] == sections:
        table['value'].append(element)
        return


    # Determine the path to the table where the element should be appended
    table_addition_path = remove_first_occurrence(table['title'], sections)
    table_addition_path = table_addition_path.strip('.')
    table_addition_path = table_addition_path.split('.')

    # Initialize the pointer to track the addition path
    final_append = table
    increased_title = table['title']
    for inner_table in table_addition_path:
        # Create intermediate nested tables along the addition path
        new_dir = {
            'title': increased_title + '.' + inner_table,
            'comments': '',
            'value': [],
            'new_table': True,
            'custom_css': '',
            'end_element': False,
            'is_section': True
        }
        increased_title = new_dir['title']
        # Append the new intermediate table and update the pointer
        final_append['value'].append(new_dir)
        final_append = new_dir
        final_append['value'] = sorted(final_append['value'], key=lambda x: x['new_table'])

    # Mark the element as a new table and append it to the final intermediate table
    element['new_table'] = True
    final_append['value'].append(element)


def insert_into_target_table(target_table, element, table, level=1):
    """
    Inserts an element into a target table within a structured table or its nested tables.

    This function recursively searches for the target table within a structured table or its nested tables,
    and inserts the given element into the target table. If the target table is not found, it appends the element
    using the append_element_to_table function.

    Args:
        target_table (str): The title of the target table where the element should be inserted.
        element (dict): The element to be inserted.
        table (dict): The structured table to search within.
        level (int, optional): The nesting level of the structure (default is 1).

    Returns:
        bool or None: True if the element was inserted, None if not found and element was appended.

    Example:
        structured_table = {
            'title': 'main_table',
            'value': [...],  # List of dictionaries and sub-tables
            ...
        }
        target_table_title = 'nested_table.target_suitable'
        element_to_insert = {'title': ..., 'value': ..., ...}
        inserted = insert_into_target_table(target_table_title, element_to_insert, structured_table)
        # Output: The element is inserted into the specified target_table if found, or appended if not found.
    """
    if table['end_element']:
        # If the current table is an end element, return
        return

    for row in table['value']:
        if isinstance(row, dict):
            if target_table.startswith(row['title']):
                # If the target table is a sub-table, recursively insert into it
                insert_into_target_table(target_table, element, row, level + 1)
                return True
        elif isinstance(row, list):
            for v in row:
                # If it's a list, recursively search within its elements
                inserted_element = insert_into_target_table(target_table, element, v, level + 1)
                if inserted_element:
                    return inserted_element

    # If the target table is not found, append the element using append_element_to_table
    append_element_to_table(table, element, target_table)
    return None


def count_dots(element):
    """
    Counts the number of dots (periods) in a given string.

    This function calculates and returns the number of dots in the provided string.

    Args:
        element (str): The string to count dots in.

    Returns:
        int: The count of dots in the string.

    Example:
        dot_count = count_dots('example.key1.key2')
        # Output: 2
    """
    return element.count('.')
