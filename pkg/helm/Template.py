
import os

from pkg.helm.utils import read_yaml_file


def return_default_template():
    """
    Returns a default documentation template.

    Returns:
        str: The default documentation template as a string.
    """
    default_documentation_template = """
{{ template "chart.header" . }}

{{ template "chart.badgesSection" . }}

{{ template "chart.description" . }}

{{ template "chart.homepageLine" . }}

{{ template "chart.maintainersSection" . }}

{{ template "chart.sourcesSection" . }}

{{ template "chart.valuesSection" . }}

{{ template "doxy-helm.versionFooter" . }}
    """
    return default_documentation_template


def load_readme_template(folder_path, readme_path):
    """
    Loads a README template from a file or returns the default template.

    Args:
        folder_path (str): The path to the folder containing the template file.
        readme_path (str): The name of the README template file.

    Returns:
        str: The contents of the README template as a string.
    """
    # return return_default_template()
    readme_template_path = os.path.join(folder_path, readme_path)
    if os.path.exists(readme_template_path):
        with open(readme_template_path, 'r') as template_file:
            readme_template_content = template_file.read()
        return readme_template_content
    else:
        return return_default_template()


