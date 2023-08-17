import yaml
import os


def get_requirements_data(chart_yaml_folder):
    requirements_path = os.path.join(chart_yaml_folder, 'requirements.yaml')

    if not os.path.exists(requirements_path):
        print(f"Warning: '{requirements_path}' does not exist.")
        return {}  # Return an empty dictionary if the file doesn't exist

    with open(requirements_path, 'r') as chart_file:
        requirements_data = yaml.safe_load(chart_file) or {}

    return requirements_data