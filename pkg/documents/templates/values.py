from ..values_section import read_and_print_values
from pkg.helm.comments_docs import get_comments_map
from ...cmd.command_line import get_values_file
import os


def get_chart_values_header():
    requirements_header_markdown = "## Values\n\n"
    return requirements_header_markdown


def get_chart_values_table(chart_folder):
    values_path = get_values_file()
    values_path = os.path.join(chart_folder, values_path)
    values_tables = read_and_print_values(values_path)
    return values_tables


def get_chart_values_section(chart_folder):
    requirements_section_markdown = f"{get_chart_values_header()}\n\n" + get_chart_values_table(chart_folder)
    return requirements_section_markdown
