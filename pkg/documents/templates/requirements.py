def get_chart_requirements_header():
    requirements_header_markdown = "## Requirements\n\n"
    return requirements_header_markdown


def get_chart_requirements_table(requirements_data):
    requirements = requirements_data.get('dependencies', [])
    requirements_table_markdown = "| Repository | Name | Version |\n|------------|------|---------|\n"
    for requirement in requirements:
        repository = requirement.get('repository', '')
        name = requirement.get('name', '')
        version = requirement.get('version', '')
        requirements_table_markdown += f"| {repository} | {name} | {version} |\n"
    requirements_table_markdown += "\n"
    return requirements_table_markdown


def get_chart_requirements_section(requirements_data):
    requirements_header = get_chart_requirements_header()
    requirements_table = get_chart_requirements_table(requirements_data)

    if requirements_header == '':
        print("Warning: 'kubeVersion' field is missing in chart_data.")
        return ''

    if requirements_table == '':
        print("Warning: 'requirements' field is missing in chart_data.")
        return ''

    requirements_section_markdown = f"{requirements_header} {requirements_table}\n"
    return requirements_section_markdown
