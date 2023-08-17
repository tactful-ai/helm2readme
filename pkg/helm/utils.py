import yaml


def read_values_yaml(values_path):
    with open(values_path, "r") as values_file:
        values_data = yaml.load(values_file, Loader=yaml.FullLoader)
        return values_data
