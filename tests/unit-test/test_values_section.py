import unittest
from unittest.mock import patch, Mock
from pkg.helm.utils import read_yaml_file, write_file, count_indentation, get_closing_bracket
from pkg.values_parser.table_formate.formate_table import formate_description, format_raw, generate_html_header, \
    start_table, end_table
from pkg.helm.utils import read_yaml_file
from pkg.values_parser.values_parser_utils import apply_custom_css, remove_element_by_key, count_dots
from pkg.values_parser.values_section import extract_top_level_entries, get_entry_value, convert_key_to_markdown, \
    convert_table_to_markdown, split_and_merge_tables


class TestCommentsParser(unittest.TestCase):

    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data='key1: value1\nkey2: value2\n')
    @patch('pkg.helm.utils.yaml.load')
    def test_read_yaml_file(self, mock_yaml_load, mock_open):
        mock_yaml_load.return_value = {'key1': 'value1', 'key2': 'value2'}
        data = read_yaml_file('test_yaml_file.yaml')
        mock_open.assert_called_with('test_yaml_file.yaml', 'r')
        self.assertEqual(data['key1'], 'value1')
        self.assertEqual(data['key2'], 'value2')

    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_write_file(self, mock_open):
        content = "This is a test content."
        output_path = 'test_output_file.txt'
        write_file(content, output_path)
        mock_open.assert_called_with(output_path, 'w')
        mock_open().write.assert_called_with(content)

    def test_count_indentation(self):
        line = "    indented line"
        indentation = count_indentation(line)
        self.assertEqual(indentation, 4)

    def test_get_closing_bracket(self):
        closing_bracket = get_closing_bracket('(')
        self.assertEqual(closing_bracket, ')')

        invalid_bracket = get_closing_bracket('[')
        self.assertEqual(invalid_bracket, ']')


class TestValuesParserUtils(unittest.TestCase):

    def test_apply_custom_css(self):
        custom_css_map = [
            {'table': 'table1', 'css': 'custom_css1'},
            {'table': 'table2', 'css': 'custom_css2'}
        ]
        values_table = [
            {'title': 'table1', 'custom_css': '', 'value': [], 'new_table': False},
            {'title': 'table2', 'custom_css': '', 'value': [], 'new_table': False},
            {'title': 'table3', 'custom_css': '', 'value': [], 'new_table': False}
        ]
        apply_custom_css(custom_css_map, values_table)
        self.assertEqual(values_table[0]['custom_css'], 'custom_css1')
        self.assertEqual(values_table[1]['custom_css'], 'custom_css2')
        self.assertEqual(values_table[2]['custom_css'], '')

    # not yet finished
    def test_remove_element_by_key(self):
        key = 'value2'
        data = [{'title': 'value1'}, {'title': 'value2'}, {'title': 'value3'}]
        result = remove_element_by_key(key, data)
        self.assertEqual(result['title'], 'value2')

    # not yet finished
    def test_count_dots(self):
        path = 'table1.entry1.entry2'
        dots = count_dots(path)
        self.assertEqual(dots, 2)


class TestValuesParser(unittest.TestCase):

    def test_extract_top_level_entries(self):
        data = {'key1': 'value1', 'key2': 'value2'}
        entries = extract_top_level_entries(data)
        self.assertEqual(entries[0]['title'], 'key1')
        self.assertEqual(entries[0]['value'], 'value1')
        self.assertEqual(entries[1]['title'], 'key2')
        self.assertEqual(entries[1]['value'], 'value2')

    def test_get_entry_value_scalar(self):
        value = 'scalar value'
        prefix = 'example'
        comments_map = {
            'example': {'beforeComments': 'This is an example value', 'afterComments': [], 'line_number': 1}
        }
        formatted_value = get_entry_value(value, prefix, comments_map)
        self.assertEqual(formatted_value[0]['title'], 'example')
        self.assertEqual(formatted_value[0]['value'], value)
        self.assertEqual(formatted_value[0]['comments'], comments_map['example']['beforeComments'])

    def test_convert_key_to_markdown_scalar(self):
        row = {
            'title': 'example',
            'value': 'scalar value',
            'comments': 'This is an example value',
            'line_number': 1,
            'custom_css': '',
            'end_element': True
        }
        markdown_content = convert_key_to_markdown(row, ".\\values.yml", False)
        expected_content = format_raw(row['value'], row['title'], row['comments'], ".\\values.yml", row['custom_css'], False, row['line_number'])
        self.assertEqual(markdown_content, expected_content)

    def test_convert_key_to_markdown_list(self):
        row = {
            'title': 'example',
            'value': [1, 2, 3],
            'comments': 'This is an example value',
            'line_number': 1,
            'custom_css': '',
            'end_element': True
        }
        markdown_content = convert_key_to_markdown(row, ".\\values.yml")
        expected_content = format_raw(row['value'], row['title'], row['comments'], ".\\values.yml", row['custom_css'], False, row['line_number'])
        self.assertEqual(markdown_content, expected_content)

    def test_convert_key_to_markdown_dict(self):
        row = {
            'title': 'example',
            'value': {
                'key1': 'value1',
                'key2': [1, 2, 3]
            },
            'comments': 'This is an example value',
            'line_number': 1,
            'custom_css': '',
            'end_element': True
        }
        markdown_content = convert_key_to_markdown(row, ".\\values.yml")
        expected_content = format_raw(row['value'], row['title'], row['comments'], ".\\values.yml", row['custom_css'], False, row['line_number'])
        self.assertEqual(markdown_content, expected_content)

    def test_convert_table_to_markdown(self):
        table = {
            'title': 'example',
            'value': [
                {
                    'title': 'example.key1',
                    'value': 'value1',
                    'comments': ['Comment for key1'],
                    'custom_css': '',
                    'end_element': True,
                    'line_number': 1,
                    'new_table': False
                },
                {
                    'title': 'example.key2[0]',
                    'value': 1,
                    'comments': ['Comment for key2'],
                    'custom_css': '',
                    'line_number': 5,
                    'end_element': True,
                    'new_table': False
                }
            ],
            'comments': ['This is an example value'],
            'custom_css': '',
            'end_element': False,
            'line_number': 9,
            'new_table': True,
            'is_section': False
        }
        markdown_content = convert_table_to_markdown(table, ".\\values.yml",False)
        expected_content = generate_html_header(1, table['title']) + formate_description(table['comments']) + start_table(table['custom_css']) + \
            convert_key_to_markdown(table['value'][0], ".\\values.yml", False) + convert_key_to_markdown(table['value'][1], ".\\values.yml", False) + end_table
        self.assertEqual(markdown_content, expected_content)

    def test_split_and_merge_tables(self):
        values_table = [
            {
                'title': 'global',
                'comments': [''],
                'value': [
                    {
                        'title': 'table1',
                        'comments': [''],
                        'value': [
                            {
                                'title': 'table1.entry1',
                                'value': 'data1',
                                'comments': [''],
                                'custom_css': '',
                                'new_table': False,
                                'end_element': True
                            }
                        ],
                        'custom_css': '',
                        'new_table': True,
                        'end_element': False
                    },
                    {
                        'title': 'table2',
                        'comments': [''],
                        'value': [
                            {
                                'title': 'table1.entry1',
                                'value': 'data1',
                                'comments': [''],
                                'custom_css': '',
                                'new_table': False,
                                'end_element': True
                            }
                        ],
                        'custom_css': '',
                        'new_table': True,
                        'end_element': False
                    }
                ],
                'custom_css': '',
                'new_table': True,
                'end_element': False
            }
        ]
        transfers_map = [
            {'table': 'table1', 'transfer': 'table2'}
        ]
        merged_tables = split_and_merge_tables(values_table, transfers_map)
        self.assertEqual(merged_tables[0]['title'], 'global')
        self.assertEqual(merged_tables[0]['new_table'], True)
        self.assertEqual(merged_tables[0]['end_element'], False)
        self.assertEqual(merged_tables[0]['value'][0]['title'], 'table2')
        self.assertEqual(merged_tables[0]['value'][0]['new_table'], True)
        self.assertEqual(merged_tables[0]['value'][0]['end_element'], False)
        self.assertEqual(merged_tables[1]['title'], 'table2')
        self.assertEqual(merged_tables[1]['new_table'], False)
        self.assertEqual(merged_tables[1]['end_element'], False)
        self.assertEqual(merged_tables[1]['value'][0]['title'], 'table1')
        self.assertEqual(merged_tables[1]['value'][0]['end_element'], False)


if __name__ == '__main__':
    unittest.main()
