import os.path

from pkg.documents.templates.chart_data import get_chart_data
from pkg.documents.templates.replacement import replace_template_parts
from pkg.documents.templates.requirement_data import get_requirements_data
from pkg.helm.charts_finder import find_chart_directories
from pkg.cmd.command_line import parse_command_line_args
from pkg.helm.Template import load_readme_template
from pkg.helm.utils import write_file



def process_single_chart(chart_directory, template_files, ignore_none_description, values_path):
    readme_template = load_readme_template(chart_directory, template_files)
    # init chart data
    chart_data = get_chart_data(chart_directory)
    # init requirements data
    requirements_data = get_requirements_data(chart_directory, chart_data)
    # replace template parts
    readme_file = replace_template_parts(readme_template, chart_data, requirements_data, chart_directory, ignore_none_description, values_path)

    return readme_file


def full_run():
    # recive the args from user
    args = parse_command_line_args()
    # assign args to variables
    (charts_search_root, dry_run, ignore_file, output_file, ignore_non_descriptions,
     sort_values_order, values_file, template_file) = (
        args.chart_search_root, args.dry_run, args.ignore_file, args.output_file, args.ignore_non_descriptions,
        args.sort_values_order, args.values_file, args.template_file)

    # find all chart directories
    chart_directories = find_chart_directories(charts_search_root, ignore_file)

    # for each chart directory
    for chart_directory in chart_directories:
        try:
            readMe = process_single_chart(chart_directory, template_file, ignore_non_descriptions, values_file)
            # if dry run active just print the readme file
            if dry_run:
                print(readMe)
            # else write the readme file to the output file
            else:
                readme_directory = os.path.join(chart_directory, output_file)
                print(readme_directory)
                write_file(readMe, readme_directory)


        except Exception as e:
            print("Error in chart directory: " + chart_directory)
            print(e)