from pkg.values_parser.table_formate.formate_table import format_raw


def format_value_for_table(value, prefix="", key_to_comment_map=None, ignore_none_description=False):
    """
    Formats a value along with its prefix and associated comments for rendering in an HTML table.

    Args:
        value: The value to be formatted.
        prefix: The prefix or key associated with the value.
        key_to_comment_map: A dictionary mapping prefixes to comments.

    Returns:
        A formatted string containing the value, type, and description for the HTML table.
    """
    if isinstance(value, list):
        formatted_items = []
        list_comments = key_to_comment_map[prefix]

        # Format the value itself with its prefix and beforeComments
        formatted_items.append(format_raw(value, prefix, list_comments['beforeComments'], ignore_none_description))

        # Iterate through each item in the list and format them separately
        for index, item in enumerate(value):
            formatted_item = format_raw(item, f"{prefix}[{index}]", list_comments['afterComments'][index], ignore_none_description)
            formatted_items.append(formatted_item)

        # Join the formatted items with newline characters
        return "\n".join(formatted_items)

    elif isinstance(value, dict):
        formatted_entries = []
        dict_comments = key_to_comment_map[prefix]

        # Format the dictionary itself with its prefix and beforeComments
        formatted_entries.append(format_raw(value, prefix, dict_comments['beforeComments']), ignore_none_description)

        # Iterate through key-value pairs in the dictionary and format the values recursively
        for k, v in value.items():
            formatted_entry = format_value_for_table(v, f"{prefix}.{k}", key_to_comment_map,ignore_none_description)
            if formatted_entry:
                formatted_entries.append(formatted_entry)

        # Join the formatted entries with newline characters
        return "\n".join(formatted_entries)

    else:
        # For non-list and non-dictionary values, format with the associated comments' beforeComments
        comments = key_to_comment_map[prefix]
        return format_raw(value, prefix, comments['beforeComments'], ignore_none_description)
