from pkg.documents.formate_table import formate_description, get_raw_value, format_raw, extract_type, \
    generate_html_header
from pkg.helm.comments_docs import get_comments_map

from pkg.helm.utils import read_values_yaml


def start_of_table(custom_css=""):
    return f"""
<table style=\"{custom_css}\">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
            """


end_of_table = """
</table>\n
"""


def extract_top_level_entries(data):
    top_level_entries = []

    for key, value in data.items():
        top_level_entries.append({
            "title": key,
            "value": value
        })

    return top_level_entries


def get_entry_value(value, prefix, key_to_comment_map):
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
            }
        ]
        for index, item in enumerate(value):
            formatted_items.append({
                'title': f"{prefix}[{index}]",
                'value': item,
                'comments': list_comments['afterComments'][index],
                'new_table': False,
                'custom_css': '',
                'end_element': True,
            })

        list_value = formatted_items
        return list_value

    elif isinstance(value, dict):
        formatted_entries = [
            {
                'title': prefix,
                'value': value,
                'comments': list_comments['beforeComments'],
                'new_table': False,
                'custom_css': '',
                'end_element': True,
            }
        ]

        for k, v in value.items():
            formatted_entry = get_entry_value(v, f"{prefix}.{k}", key_to_comment_map)
            if formatted_entry:
                formatted_entries.append(formatted_entry)

        dict_value = formatted_entries
        return dict_value

    else:
        comments = key_to_comment_map[prefix]
        return {
            'title': prefix,
            'value': value,
            'comments': comments['beforeComments'],
            'new_table': False,
            'custom_css': '',
            'end_element': True,
        }


def new_table(formatted_value, custom_css=""):
    return end_of_table + formatted_value + start_of_table(custom_css)


def convert_key_to_markdown(row):
    returned_raws = ''
    if isinstance(row, list):
        for v in row:
            returned_raws += convert_key_to_markdown(v)
    elif isinstance(row, dict):
        if row['end_element']:
            return format_raw(row['value'], row['title'], row['comments'], row['custom_css'])
        else:
            return convert_key_to_markdown(row['value'])

    return returned_raws


def get_element_by_key(key, table):
    if isinstance(table, dict):
        if table['title'] == key:
            return table
    else:
        for row in table:
            if isinstance(row, dict):
                if row['title'] == key:
                    return row
            elif isinstance(row, list):
                for v in row:
                    if get_element_by_key(key, v):
                        return v


def apply_custom_css(custom_css_map, values_table):
    for custom_css in custom_css_map:
        if custom_css['table'] == '*':
            for table in values_table:
                table['custom_css'] += custom_css['css']
            continue

        table_title = custom_css['table']
        css = custom_css['css']

        # init the var that i will arrive to my target table with
        target_element = values_table
        if '.' in table_title:
            # gain the title of the main table
            for table in target_element:
                if table['title'] == table_title.split('.', 1)[0]:
                    target_element = table['value']
                    break

            target_element = get_element_by_key(table_title, target_element)
            target_element['custom_css'] += css
        else:
            for table in target_element:
                if table['title'] == table_title.split('.', 1)[0]:
                    table['custom_css'] += css


def convert_table_to_markdown(table, level=1):
    markdown_content = ""

    intermidiate_table = True

    for table_row in table['value']:
        if not table_row['new_table']:
            intermidiate_table = False
            break

    table_title = generate_html_header(level, table['title'])
    markdown_content += table_title
    if not intermidiate_table:
        table_description = formate_description(table['comments'])
        markdown_content += table_description
        markdown_content += start_of_table(table['custom_css'])

    for row in table['value']:
        if isinstance(row, list):
            for v in row:
                markdown_content += convert_key_to_markdown(v)
        elif isinstance(row, dict):
            if row['new_table']:
                markdown_content += end_of_table + convert_table_to_markdown(row, level + 1)
            else:
                formatted_value = convert_key_to_markdown(row)
                markdown_content += formatted_value

    markdown_content += end_of_table

    return markdown_content


def process_string(level, key):
    num_dots = key.count('.')

    if level > num_dots:
        return key
    else:
        return key.split('.', level)[0]


def remove_element_by_key(key, table, level=1):
    for row in table:
        if isinstance(row, dict):
            if row.get('title') == key:
                table.remove(row)
                return row
            elif row.get('title') == process_string(level, key):
                return remove_element_by_key(key, row['value'], level + 1)
        elif isinstance(row, list):
            for v in row:
                if isinstance(v, (dict, list)):
                    removed_element = remove_element_by_key(key, v, level + 1)
                    if removed_element:
                        return removed_element


def remove_first_occurrence(substring, main_string):
    index = main_string.find(substring)
    if index != -1:
        new_string = main_string[:index] + main_string[index + len(substring):]
        return new_string
    else:
        return main_string


def append_element_to_table(table, element):
    table_addition_path = remove_first_occurrence(table['title'], element['title'])
    table_addition_path = table_addition_path.strip('.')
    table_addition_path = table_addition_path.split('.')
    # final_title = table_addition_path[-1]
    final_append = table
    for inner_table in (table_addition_path[:-1]):
        new_dir = {
            'title': table['title'] + '.' + inner_table,
            'comments': '',
            'value': [],
            'new_table': True,
            'custom_css': '',
            'end_element': False,
        }
        final_append['value'].append(new_dir)
        final_append = new_dir
        final_append['value'] = sorted(final_append['value'], key=lambda x: x['new_table'])
    element['new_table'] = True
    # element['title'] = final_title
    final_append['value'].append(element)


def insert_into_target_table(target_table, element, table, level=1):
    if table['end_element']:
        return

    for row in table['value']:
        if isinstance(row, dict):
            if target_table.startswith(row['title']):
                insert_into_target_table(target_table, element, row, level + 1)
                return True
        elif isinstance(row, list):
            for v in row:
                inserted_element = insert_into_target_table(target_table, element, v, level + 1)
                if inserted_element:
                    return inserted_element

    append_element_to_table(table, element)


def count_dots(element):
    return element.count('.')


def split_and_merge_tables(values_table, transfers_map):
    splitted_tables = []
    transfers_map = sorted(transfers_map, key=lambda x: count_dots(x['transfer']))

    for transfer in transfers_map:
        is_new_table = False
        from_table = transfer['table']
        to_table = transfer['transfer']
        target_table = remove_element_by_key(from_table, values_table[0]['value'])
        for table in values_table + splitted_tables:
            if to_table.startswith(table['title']):
                is_new_table = True
                target_table['title'] = to_table
                target_table['new_table'] = True
                target_table['end_element'] = False
                insert_into_target_table(to_table, target_table, table)
                break

        if not is_new_table:
            target_table['title'] = to_table
            target_table['new_table'] = True
            target_table['end_element'] = False
            new_main_dir = {
                'title': '',
                'comments': [],
                'value': [],
                'new_table': False,
                'custom_css': '',
                'end_element': False,
            }
            append_element_to_table(new_main_dir, target_table)
            splitted_tables.append(new_main_dir)

    sorted_global = sorted(values_table, key=lambda x: x['new_table'])
    sorted_splitted_tables = sorted(splitted_tables, key=lambda x: x['new_table'])
    return sorted_global + sorted_splitted_tables


def generate_markdown_output(entries, key_to_comment_map, transfers_map, custom_css_map):
    values_table = []
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
            'new_table': False,
            'custom_css': '',
            'end_element': False,
        })

    # applying custom css
    apply_custom_css(custom_css_map, values_table)

    # adding global table
    values_table = [{
        'title': 'global',
        'comments': '',
        'value': values_table,
        'new_table': True,
        'custom_css': '',
        'end_element': False,
    }]

    # split and merge tables
    final_tables = split_and_merge_tables(values_table, transfers_map)

    markdown_content = ""
    for table in final_tables:
        markdown_content += convert_table_to_markdown(table)

    return markdown_content


def read_and_print_values(values_path, sort='AlphaNum'):
    values_data = read_values_yaml(values_path)
    top_level_entries = extract_top_level_entries(values_data)
    if sort == 'AlphaNum':
        # Sort top_level_entries alphabetically
        top_level_entries = sorted(top_level_entries, key=lambda x: x['title'], )
    key_to_comment_map, transfers_map, custom_css_map = get_comments_map(values_path)

    markdown_content = generate_markdown_output(top_level_entries, key_to_comment_map, transfers_map, custom_css_map)
    return markdown_content