import argparse
import os
import unittest
from unittest.mock import patch

from main import process_single_chart
from pkg.cmd.command_line import parse_command_line_args
from pkg.helm.charts_finder import find_chart_directories


class fullTest(unittest.TestCase):

    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(
        table_depth=3,
        chart_search_root='.',
        template_file='README.md.gotmpl',
        dry_run=True,
        output_file='README.md',
        ignore_file='.helmdocsignore',
        values_file='values.yaml',
        sort_values_order='File',
        ignore_non_descriptions=False
    ))
    def test_full_tool(self, mock_parse_args):
        # recive the args from user
        args = parse_command_line_args()
        # assign args to variables
        (charts_search_root, dry_run, ignore_file, output_file, ignore_non_descriptions,
         sort_values_order, values_file, template_file) = (
            args.chart_search_root, args.dry_run, args.ignore_file, args.output_file, args.ignore_non_descriptions,
            args.sort_values_order, args.values_file, args.template_file)

        # find all chart directories
        chart_directories = find_chart_directories(charts_search_root, ignore_file)
        # for each chart directory
        for chart_directory in chart_directories:
                readMe = process_single_chart(chart_directory, template_file, ignore_non_descriptions, values_file, sort_values_order)
                correct_readme = ''
                correct_readme_path = os.path.join(chart_directory, 'README.md')
                with open(correct_readme_path, 'r') as correct_readme_file:
                    correct_readme = correct_readme_file.read()

                try:
                    self.assertEqual(readMe, correct_readme)
                except AssertionError:
                    print("Assertion failed for chart directory:", chart_directory)
                    print("Expected README content:\n", correct_readme)
                    print("Actual README content:\n", readMe)
                    raise  # Re-raise the AssertionError to mark the test as failed

if __name__ == '__main__':
    unittest.main()
