def get_chart_requirements_header():
    """
    Generates the markdown header for the 'Requirements' section.

    Returns:
        str: Markdown header for the 'Requirements' section.
    """
    requirements_header_markdown = "## Requirements\n\n"
    return requirements_header_markdown


def get_chart_requirements_table(requirements_data):
    """
    Generates markdown tables for the 'Requirements' section of the chart.

    Args:
        requirements_data (dict): Data containing information about chart requirements.

    Returns:
        str: Markdown table representing the 'Requirements' section of the chart.
    """
    requirements = requirements_data.get('dependencies', [])  # Extract the list of dependencies from requirements_data
    requirements_table_markdown = "| Repository | Name | Version |\n|------------|------|---------|\n"

    for requirement in requirements:
        repository = requirement.get('repository', '')
        name = requirement.get('name', '')
        version = requirement.get('version', '')
        requirements_table_markdown += f"| {repository} | {name} | {version} |\n"

    requirements_table_markdown += "\n"
    return requirements_table_markdown


def get_chart_requirements_section(requirements_data):
    """
    Generates the complete markdown section for the 'Requirements' section of the chart.

    Args:
        requirements_data (dict): Data-containing information about chart requirements.

    Returns:
        str: Complete markdown section for the 'Requirements' section of the chart.
    """
    requirements_header = get_chart_requirements_header()  # Generate the 'Requirements' section header
    requirements_table = get_chart_requirements_table(requirements_data)  # Generate the 'Requirements' section table

    if requirements_header == '':
        print("Warning: 'kubeVersion' field is missing in chart_data.")
        return ''

    if requirements_table == '':
        print("Warning: 'requirements' field is missing in chart_data.")
        return ''

    requirements_section_markdown = f"{requirements_header} {requirements_table}\n"
    return requirements_section_markdown
