import unittest
from unittest.mock import mock_open, patch

from pkg.comment_parser.comments_parser_utils import (
    print_key_comments,
    find_next_non_empty_line,
    extract_closing_tags_or_characters,
    find_line_with_closing_bracket,
    extract_text_from_brackets,
    get_key, get_closing_bracket
)


class TestCommentParserUtils(unittest.TestCase):

    def test_find_next_non_empty_line(self):
        yaml_file = iter(['', '  \n', 'line1', 'line2'])
        current_line = next(yaml_file)
        result = find_next_non_empty_line(yaml_file, current_line)
        self.assertEqual(result, 'line1')

    def test_extract_closing_tags_or_characters_with_closing_tag(self):
        line = '<tag_name> Some text </tag_name>'
        result = extract_closing_tags_or_characters(line)
        self.assertEqual(result, '</tag_name>')

    def test_extract_closing_tags_or_characters_with_opening_bracket(self):
        line = '[{{some_characters}}'
        result = extract_closing_tags_or_characters(line)
        self.assertEqual(result, '}}]')

    def test_find_line_with_closing_bracket(self):
        target_closing_bracket = '}'
        yaml_file = iter(['line1', 'line2', 'line3}'])
        current_line = next(yaml_file)
        result = find_line_with_closing_bracket(current_line, yaml_file, target_closing_bracket)
        self.assertEqual(result, 'line3}')

    def test_extract_text_from_brackets(self):
        comment = 'Text: {extract_this} and that'
        result = extract_text_from_brackets(comment, '{')
        self.assertEqual(result, 'extract_this')

    def test_get_key(self):
        keys_array = ['level1', 'level2', 'level3']
        result = get_key(keys_array)
        self.assertEqual(result, 'level1.level2.level3')


if __name__ == '__main__':
    unittest.main()
