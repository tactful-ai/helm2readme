import unittest
from unittest.mock import patch
import argparse
from pkg.cmd.command_line import parse_command_line_args, get_table_depth, get_ignore_non_descriptions, \
    get_values_sort_order, get_values_file


class TestCommandLineArgsParsing(unittest.TestCase):

    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(
        table_depth=3,
        chart_search_root='./example-charts/full-template',
        template_file='README.md.gotmpl',
        dry_run=True,
        output_file='README_test.md',
        ignore_file='.helmdocsignore_test',
        values_file='custom_values.yaml',
        sort_values_order='File',
        ignore_non_descriptions=True,
    ))
    def test_parse_command_line_args(self, mock_parse_args):
        args = parse_command_line_args()

        self.assertEqual(args.table_depth, 3)
        self.assertTrue(args.ignore_non_descriptions)
        self.assertEqual(args.sort_values_order, 'File')
        self.assertEqual(args.values_file, 'custom_values.yaml')
        self.assertEqual(args.chart_search_root, './example-charts/full-template')
        self.assertEqual(args.template_file, 'README.md.gotmpl')
        self.assertTrue(args.dry_run)
        self.assertEqual(args.output_file, 'README_test.md')
        self.assertEqual(args.ignore_file, '.helmdocsignore_test')


    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(table_depth=5))
    def test_get_table_depth(self, mock_parse_args):
        result = get_table_depth()
        self.assertEqual(result, 5)

    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(ignore_non_descriptions=True))
    def test_get_ignore_non_descriptions(self, mock_parse_args):
        result = get_ignore_non_descriptions()
        self.assertTrue(result)

    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(sort_values_order='AlphaNum'))
    def test_get_values_sort_order(self, mock_parse_args):
        result = get_values_sort_order()
        self.assertEqual(result, 'AlphaNum')

    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(values_file='custom_values.yaml'))
    def test_get_values_file(self, mock_parse_args):
        result = get_values_file()
        self.assertEqual(result, 'custom_values.yaml')


if __name__ == '__main__':
    unittest.main()
