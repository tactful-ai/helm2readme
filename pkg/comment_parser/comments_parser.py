from pkg.comment_parser.comments_parser_utils import extract_text_from_brackets, get_key
from pkg.helm.utils import count_indentation


class CommentParser:
    def __init__(self):
        self.key_to_comment_map = {}
        self.transfers_map = []
        self.custom_css_map = []
        self.current_comment = []
        self.full_key = None
        self.prefix_keys = []
        self.previous_indentation = 0
        self.last_key_indentation = [-1]
        self.is_array = False

    def _process_comment(self, stripped_line):
        self.current_comment.append(stripped_line.lstrip('#').strip())
        if stripped_line.startswith('# -- @custom_css'):
            self.custom_css_map.append({
                'table': '*',
                'css': extract_text_from_brackets(stripped_line, '{')
            })

    def _process_array(self):
        self.key_to_comment_map[self.full_key]['afterComments'].append(self.current_comment)
        self.current_comment = []
        self.is_array = True

    def _process_key(self, stripped_line, current_indentation, line_number):
        current_key = stripped_line.split(':')[0].strip().strip("\"").strip("\'")

        if current_indentation > self.last_key_indentation[-1]:
            self.prefix_keys.append(current_key)
            self.last_key_indentation.append(current_indentation)
        else:
            while current_indentation <= self.last_key_indentation[-1] and len(self.last_key_indentation) > 1:
                self.prefix_keys.pop()
                self.last_key_indentation.pop()
            self.prefix_keys.append(current_key)
            self.last_key_indentation.append(current_indentation)

        self.full_key = get_key(self.prefix_keys)
        comments_to_remove = []
        for comment in self.current_comment:
            custom_css_table = extract_text_from_brackets(comment, '{')
            transfer_table = extract_text_from_brackets(comment, '[')
            if custom_css_table is not None:
                self.custom_css_map.append({
                    'table': self.full_key,
                    'css': custom_css_table
                })
                comments_to_remove.append(comment)
            if transfer_table is not None:
                self.transfers_map.append({
                    'table': self.full_key,
                    'transfer': transfer_table
                })
                comments_to_remove.append(comment)

        for comment in comments_to_remove:
            self.current_comment.remove(comment)

        self.key_to_comment_map[f'{self.full_key}'] = {'beforeComments': [], 'afterComments': []}
        self.key_to_comment_map[f'{self.full_key}']['beforeComments'] = self.current_comment
        self.key_to_comment_map[f'{self.full_key}']['line_number'] = line_number
        self.current_comment = []

    def parse_comment_from_string(self, yaml_file):
        line_number = 0
        for line in yaml_file:
            line_number += 1
            if line.strip():
                current_indentation = count_indentation(line)
                is_comment = line.lstrip().startswith('#')
                is_new_element_in_array = line.strip().startswith('-')

                #  this part is used to ignore the lines that are smaller or under the array element
                # as example:
                # usersToCreate:
                # -- admin user
                # - {name: root,
                #    admin: true}
                #     here we should ignore the admin: true} line since is just part of the array
                if current_indentation >= self.previous_indentation and self.is_array and not is_comment:
                    continue
                else:
                    self.is_array = False

                stripped_line = line.strip()

                if stripped_line.startswith('# --') | stripped_line.startswith('# @'):
                    self._process_comment(stripped_line)
                elif stripped_line.startswith('-'):
                    self._process_array()
                elif ':' in stripped_line:
                    self._process_key(stripped_line, current_indentation, line_number)

                self.previous_indentation = current_indentation


        return self.key_to_comment_map, self.transfers_map, self.custom_css_map

    def get_comments_map(self, yaml_file_path):
        with open(yaml_file_path, 'r') as yaml_file:
            comments = self.parse_comment_from_string(yaml_file)
            return comments
