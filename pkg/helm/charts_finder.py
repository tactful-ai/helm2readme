import os
import fnmatch


def find_chart_directories(root_directory, ignore_file_path=None):
    chart_directories = []

    ignore_patterns = []
    if ignore_file_path is None:
        ignore_file_path = os.path.join(root_directory, '.helmdocsignore')

    if os.path.exists(ignore_file_path):
        with open(ignore_file_path, 'r') as ignore_file_content:
            ignore_patterns = [line.strip() for line in ignore_file_content.readlines()]

    for root, dirs, files in os.walk(root_directory):
        if "Chart.yaml" in files:
            chart_directories.append(root)
            dirs.clear()  # Clear the subdirectories list to prevent further traversal
        else:
            for pattern in ignore_patterns:
                for d in dirs[:]:  # Create a copy of dirs for iteration
                    full_path = os.path.join(root, d)
                    if fnmatch.fnmatch(full_path, pattern):
                        dirs.remove(d)  # Remove the directory from dirs

    return chart_directories


