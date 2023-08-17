
import os


def return_default_template():
    default_documentation_template = """
{{ template "chart.header" . }}

{{ template "chart.badgesSection" . }}

{{ template "chart.description" . }}

{{ template "chart.homepageLine" . }}

{{ template "chart.maintainersSection" . }}

{{ template "chart.sourcesSection" . }}

{{ template "chart.valuesSection" . }}

{{ template "helm-docs.versionFooter" . }}
    """
    return default_documentation_template


def load_readme_template(folder_path, readme_path):
    return return_default_template()
    readme_template_path = os.path.join(folder_path, readme_path)
    if os.path.exists(readme_template_path):
        with open(readme_template_path, 'r') as template_file:
            readme_template_content = template_file.read()
        return readme_template_content
    else:
        return return_default_template()


def write_docs(file_content, output_path):
    with open(output_path, "w") as output_file:
        output_file.write(file_content)
