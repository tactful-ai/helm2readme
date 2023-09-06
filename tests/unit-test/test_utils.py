import unittest
from pkg.helm.utils import read_yaml_file, write_file, count_indentation, get_closing_bracket


class TestUtilsFunctions(unittest.TestCase):

    def test_read_yaml_file(self):
        yaml_content = """
        key1: value1
        key2:
          subkey: subvalue
        """
        with open('test_yaml_file.yaml', 'w') as test_file:
            test_file.write(yaml_content)

        data = read_yaml_file('test_yaml_file.yaml')

        self.assertEqual(data['key1'], 'value1')
        self.assertEqual(data['key2']['subkey'], 'subvalue')

    def test_write_file(self):
        content = "This is a test content."
        output_path = 'test_output_file.txt'
        write_file(content, output_path)

        with open(output_path, 'r') as test_file:
            read_content = test_file.read()

        self.assertEqual(read_content, content)

    def test_count_indentation(self):
        line = "    indented line"
        indentation = count_indentation(line)
        self.assertEqual(indentation, 4)

    def test_get_closing_bracket(self):
        closing_bracket = get_closing_bracket('(')
        self.assertEqual(closing_bracket, ')')

        invalid_bracket = get_closing_bracket('[')
        self.assertEqual(invalid_bracket, ']')

if __name__ == '__main__':
    unittest.main()
