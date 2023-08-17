import os.path

from pkg.documents.templates.chart_data import get_chart_data
from pkg.documents.templates.replacement import replace_template_parts
from pkg.documents.templates.requirement_data import get_requirements_data
from pkg.helm.charts_finder import find_chart_directories
from pkg.cmd.command_line import parse_command_line_args
from pkg.helm.Template import load_readme_template, write_docs


def process_single_chart(chart_directory, template_files, output_file, dry_run):
    readme_template = load_readme_template(chart_directory, template_files)
    # init chart data
    chart_data = get_chart_data(chart_directory)
    # init requirements data
    requirements_data = get_requirements_data(chart_directory)
    # replace template parts
    readme_file = replace_template_parts(readme_template, chart_data, requirements_data, chart_directory)
    # if dry run active just print the readme file
    if dry_run:
        print(readme_file)
    # else write the readme file to the output file
    else:
        write_docs(readme_file, './' + output_file)


def full_run():
    # recive the args from user
    args = parse_command_line_args()
    # assign args to variables
    (charts_search_root, dry_run, ignore_file, output_file, ignore_non_descriptions,
     sort_values_order, values_file, template_file) = (
        args.chart_search_root, args.dry_run, args.ignore_file, args.output_file, args.ignore_non_descriptions,
        args.sort_values_order, args.values_file, args.template_files)

    # find all chart directories
    chart_directories = find_chart_directories(charts_search_root, ignore_file)

    # for each chart directory
    for chart_directory in chart_directories:
        process_single_chart(chart_directory, template_file, output_file, dry_run)


def main():
    # full_run()

    chart_directory = './example-charts/full-template'
    template_files = 'README.md.gotmpl'
    output_file = "README.md"
    dry_run = False
    process_single_chart(chart_directory, template_files, output_file, dry_run)


if __name__ == "__main__":
    main()
