def print_comments_map(key_to_comment_map):
    for key, comments_dict in key_to_comment_map.items():
        print("Key:", key)
        print("Before Comments:", comments_dict['beforeComments'])
        print("After Comments:", comments_dict['afterComments'])
        print()


def count_indentation(line):
    return len(line) - len(line.lstrip())


def next_non_empty_line(yaml_file, current_line):
    line = current_line
    stripped_line = line.strip()
    while len(stripped_line) == 0:
        line = next(yaml_file, '')
        stripped_line = line.strip()
    return line


def get_key(Keys_array):
    return '.'.join(Keys_array)


def get_closing_bracket(opening_bracket):
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    return brackets.get(opening_bracket, 'Invalid bracket')


def extract_and_create_closing_tags_or_characters(line):
    line = line.strip()

    if line.startswith('<') and '>' in line:
        opening_tag = line.split('>')[0] + '>'
        tag_name = opening_tag[1:-1]  # Extract the tag name
        closing_tag = f"</{tag_name}>"
        return closing_tag

    else:
        # Count the number of consecutive opening brackets
        num_opening_brackets = 0
        for char in line:
            if char in '[{':
                num_opening_brackets += 1
            else:
                break

        if num_opening_brackets > 0:
            closing_brackets = ']' * num_opening_brackets if line.startswith('[') else '}' * num_opening_brackets
            return closing_brackets

        else:
            return None  # Return None if the line doesn't start with a recognized opening tag, bracket, or character


def find_line_with_closing_bracket(current_line, yaml_file, target_closing_bracket):
    while True:
        if target_closing_bracket in current_line:
            return current_line
        else:
            current_line = next(yaml_file, '')


def extract_from_brackets(comment, bracket):
    prefix = bracket
    suffix = get_closing_bracket(bracket)
    start = comment.find(prefix)
    end = comment.find(suffix, start + len(prefix))

    if start != -1 and end != -1:
        return comment[start + len(prefix):end].strip()
    else:
        return None


def get_comment_from_string(yaml_file):
    key_to_comment_map = {}
    transfers_map = []
    custom_css_map = []
    current_comment = []
    full_key = None
    prefix_keys = []
    previous_indentation = 0
    last_key_indentation = [-1]
    # config_indentation = []
    is_array = False
    # is_config = False

    for line in yaml_file:
        if line.strip():

            current_indentation = count_indentation(line)
            is_comment = line.lstrip().startswith('# --')

            # if is_config:
            #     line = next_non_empty_line(yaml_file, line)
            #     bracket_value = extract_and_create_closing_tags_or_characters(line)
            #     if bracket_value is not None:
            #         find_line_with_closing_bracket(line, yaml_file, bracket_value)
            #         config_indentation.pop()
            #         is_config = False
            #         continue
            #
            #     is_config = False

            if current_indentation >= previous_indentation and is_array and not is_comment:
                continue
            else:
                is_array = False

            # if len(config_indentation) > 0:
            #     # we have config map we need to process
            #     if len(config_indentation) > 0 and current_indentation >= config_indentation[-1] and current_indentation > 0:
            #         current_indentation += config_indentation[-1]
            #
            #     elif current_indentation == 0 or current_indentation < config_indentation[-1]:
            #         config_indentation.pop()

            # # we found new config map
            # if line.rstrip().endswith('|'):
            #     config_indentation.append(current_indentation)
            #     is_config = True

            stripped_line = line.strip()

            if is_comment:
                current_comment.append(stripped_line.lstrip('#').strip())
                if stripped_line.startswith('# -- @custom_css'):
                    custom_css_map.append({
                        'table': '*',
                        'css': extract_from_brackets(stripped_line, '{')
                    })

            elif stripped_line.startswith('-'):
                key_to_comment_map[full_key]['afterComments'].append(current_comment)
                current_comment = []
                is_array = True

            elif ':' in stripped_line:
                current_key = stripped_line.split(':')[0].strip()

                if current_indentation > last_key_indentation[-1]:
                    prefix_keys.append(current_key)
                    last_key_indentation.append(current_indentation)
                else:
                    while current_indentation <= last_key_indentation[-1] and len(last_key_indentation) > 1:
                        prefix_keys.pop()
                        last_key_indentation.pop()
                    prefix_keys.append(current_key)
                    last_key_indentation.append(current_indentation)

                full_key = get_key(prefix_keys)
                comments_to_remove = []
                for comment in current_comment:
                    custom_css_table = extract_from_brackets(comment, '{')
                    transfer_table = extract_from_brackets(comment, '[')
                    if custom_css_table is not None:
                        custom_css_map.append({
                            'table': full_key,
                            'css': custom_css_table
                        })
                        comments_to_remove.append(comment)
                    if transfer_table is not None:
                        transfers_map.append({
                            'table': full_key,
                            'transfer': transfer_table
                        })
                        comments_to_remove.append(comment)

                for comment in comments_to_remove:
                    current_comment.remove(comment)

                key_to_comment_map[full_key] = {'beforeComments': [], 'afterComments': []}
                key_to_comment_map[full_key]['beforeComments'] = current_comment
                current_comment = []
                after_comments = []

            previous_indentation = current_indentation
    return key_to_comment_map, transfers_map, custom_css_map


def get_comments_map(yaml_file_path):
    with open(yaml_file_path, 'r') as yaml_file:
        comments = get_comment_from_string(yaml_file)
        return comments
