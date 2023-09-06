import unittest
from unittest.mock import mock_open, patch
from pkg.comment_parser.comments_parser_utils import extract_text_from_brackets, get_key
from pkg.comment_parser.comments_parser import CommentParser


class TestCommentParser(unittest.TestCase):

    def setUp(self):
        self.comment_parser = CommentParser()

    def test_process_comment_with_custom_css(self):
        stripped_line = '# -- @custom_css {background-color: blue;}'
        self.comment_parser._process_comment(stripped_line)

        expected_custom_css_map = [{'table': '*', 'css': 'background-color: blue;'}]
        self.assertEqual(self.comment_parser.custom_css_map, expected_custom_css_map)

    def test_process_array(self):
        self.comment_parser.current_comment = ['Comment for array element']
        self.comment_parser.key_to_comment_map['example'] = {'beforeComments': [], 'afterComments': []}
        self.comment_parser.full_key = 'example'
        self.comment_parser.is_array = False

        self.comment_parser._process_array()

        expected_after_comments = [['Comment for array element']]
        self.assertEqual(self.comment_parser.key_to_comment_map['example']['afterComments'], expected_after_comments)
        self.assertTrue(self.comment_parser.is_array)
        self.assertEqual(self.comment_parser.current_comment, [])

    def test_process_key(self):
        stripped_line = """
        example_key: Some value
        """

        current_indentation = 0
        self.comment_parser.current_comment = ['Comment before key']
        self.comment_parser.full_key = 'example_key'
        self.comment_parser.prefix_keys = []
        self.comment_parser.last_key_indentation = [-1]

        self.comment_parser._process_key(stripped_line, current_indentation, 1)

        expected_comments_map = {
            'example_key': {'afterComments': [], 'beforeComments': ['Comment before key'], 'line_number': 1}
        }
        self.assertEqual(self.comment_parser.key_to_comment_map, expected_comments_map)


    @patch('builtins.open', new_callable=mock_open, read_data='key1: value1\n')
    def test_parse_comment_from_string(self, mock_file):
        yaml_file = mock_file.return_value.__enter__.return_value
        comments, transfers, custom_css = self.comment_parser.parse_comment_from_string(yaml_file)

        expected_comments_map = {'key1': {'beforeComments': [], 'afterComments': [], 'line_number': 1}}
        expected_transfers_map = []
        expected_custom_css_map = []

        self.assertEqual(comments, expected_comments_map)
        self.assertEqual(transfers, expected_transfers_map)
        self.assertEqual(custom_css, expected_custom_css_map)


if __name__ == '__main__':
    unittest.main()
