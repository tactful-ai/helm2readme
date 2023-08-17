import yaml
import os

def get_chart_data(chart_yaml_folder):
    """
    Reads and retrieves chart data from the 'Chart.yaml' file in the given folder.

    Args:
        chart_yaml_folder (str): Path to the folder containing 'Chart.yaml'.

    Returns:
        dict: Dictionary containing chart data or an empty dictionary if file is empty or missing.
    """
    # Construct the path to the 'Chart.yaml' file
    chart_yaml_path = os.path.join(chart_yaml_folder, 'Chart.yaml')

    # Open the 'Chart.yaml' file and load its content as YAML data
    with open(chart_yaml_path, 'r') as chart_file:
        chart_data = yaml.safe_load(chart_file) or {}  # Load data or provide an empty dictionary

    return chart_data
