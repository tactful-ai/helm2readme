import argparse


def parse_command_line_args():
    parser = argparse.ArgumentParser(
        prog="doxy-helm",
        description="Helm Docs Command Line Tool",
        epilog="For more information, visit https://github.com/tactful-ai/doxy-helm",
    )

    parser.add_argument("-td", "--table-depth", default=1, type=int, help="Depth of separate tables to generate")
    parser.add_argument("-c", "--chart-search-root", default=".", help="Directory to search recursively within for charts")
    parser.add_argument("-t", "--template-file", default='README.md.gotmpl', help="Gotemplate file paths relative to each chart directory from which documentation will be generated")
    parser.add_argument("-d", "--dry-run", default=False, action="store_true", help="Don't actually render any markdown files, just print to stdout")
    parser.add_argument("-o", "--output-file", default="README.md", help="Markdown file path relative to each chart directory to which rendered documentation will be written")
    parser.add_argument("-i", "--ignore-file", default=".helmdocsignore", help="The filename to use as an ignore file to exclude chart directories")
    parser.add_argument("-f", "--values-file", default="values.yaml", help="Path to values file")
    parser.add_argument("-s", "--sort-values-order", default="File", choices=["AlphaNum", "File"], help="Order in which to sort the values table")
    parser.add_argument("-n", "--ignore-non-descriptions", default=False, action="store_true", help="Ignore values without a comment, these values will not be included in the README")

    # parser.add_argument("-b", "--badge-style", default="flat-square", help="Badge style to use for charts")
    # parser.add_argument("-u", "--document-dependency-values", action="store_true", help="Include dependency values in the chart values documentation")
    # parser.add_argument("-g", "--chart-to-generate", nargs="+", default=[], help="List of charts that will have documentation generated")
    # parser.add_argument("-x", "--documentation-strict-mode", action="store_true", help="Fail the generation of docs if there are undocumented values")
    # parser.add_argument("-y", "--documentation-strict-ignore-absent", nargs="+", default=["service.type", "image.repository", "image.tag"], help="Values which are allowed not to be documented in strict mode")
    # parser.add_argument("-z", "--documentation-strict-ignore-absent-regex", nargs="+", default=[".*service\\.type", ".*image\\.repository", ".*image\\.tag"], help="Regex patterns of values which are allowed not to be documented in strict mode")

    args = parser.parse_args()

    return args

