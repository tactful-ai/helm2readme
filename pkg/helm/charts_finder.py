import os
import fnmatch


def find_chart_directories(root_directory, ignore_file_path=None):
    """
    Finds directories containing 'Chart.yaml' files in the given root directory.

    Args:
        root_directory (str): The root directory to start searching from.
        ignore_file_path (str, optional): Path to the ignore file containing patterns to exclude directories. Default is None.

    Returns:
        list: List of directory paths containing 'Chart.yaml' files.
    """
    chart_directories = []  # Initialize an empty list to store directory paths

    ignore_patterns = []  # Initialize an empty list to store ignore patterns

    # Check if an ignore file path is provided, otherwise use the default '.helmdocsignore' path in the root directory
    if ignore_file_path is None:
        ignore_file_path = os.path.join(root_directory, '.helmdocsignore')

    # If the ignore file exists, read its contents and populate the ignore_patterns list
    if os.path.exists(ignore_file_path):
        with open(ignore_file_path, 'r') as ignore_file_content:
            ignore_patterns = [line.strip() for line in ignore_file_content.readlines()]

    # Traverse the directory tree starting from the root directory
    for root, dirs, files in os.walk(root_directory):
        if "Chart.yaml" in files:
            # If a 'Chart.yaml' file is found in the current directory, add the directory to chart_directories list
            chart_directories.append(root)
            dirs.clear()  # Clear the subdirectories list to prevent further traversal
        else:
            # Iterate over the ignore_patterns and remove matching directories from the dirs list
            for pattern in ignore_patterns:
                for d in dirs[:]:  # Create a copy of dirs for iteration to avoid modifying the list while iterating
                    full_path = os.path.join(root, d)
                    if fnmatch.fnmatch(full_path, pattern):
                        dirs.remove(d)  # Remove the directory from dirs to prevent further traversal

    return chart_directories  # Return the list of directory paths containing 'Chart.yaml' files
