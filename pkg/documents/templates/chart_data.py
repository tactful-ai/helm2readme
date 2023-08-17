import yaml
import os

def get_chart_data(chart_yaml_folder):
    chart_yaml_path = os.path.join(chart_yaml_folder, 'Chart.yaml')
    with open(chart_yaml_path, 'r') as chart_file:
        chart_data = yaml.safe_load(chart_file) or {}
    return chart_data