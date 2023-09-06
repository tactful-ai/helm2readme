from pkg.values_parser.values_section import read_and_print_values
import os


def get_chart_values_header():
    """
    Generates the markdown header for the 'Values' section.

    Returns:
        str: Markdown header for the 'Values' section.
    """
    values_header_markdown = "## Values\n\n"
    return values_header_markdown


def get_chart_values_table(chart_folder, ignore_none_description, values_path):
    """
    Generates markdown tables for the 'Values' section of the chart.

    Args:
        chart_folder (str): Path to the chart folder.

    Returns:
        str: Markdown tables representing the 'Values' section of the chart.
    """

    values_path = os.path.join(chart_folder, values_path)  # Construct the full path to the values.yaml file
    values_tables = read_and_print_values(values_path,
                                          ignore_none_description)  # Read and print the values from the values.yaml file
    return values_tables


def get_chart_values_section(chart_folder, ignore_none_description, values_path):
    """
    Generates the complete markdown section for the 'Values' section of the chart.

    Args:
        chart_folder (str): Path to the chart folder.

    Returns:
        str: Complete markdown section for the 'Values' section of the chart.
    """
    values_section_markdown = f"{get_chart_values_header()}\n\n" + get_chart_values_table(chart_folder,ignore_none_description, values_path )
    return values_section_markdown
