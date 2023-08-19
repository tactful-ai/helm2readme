def get_chart_header(chart_data):
    name = chart_data.get('name')
    if name is None:
        print("Warning: 'name' field is missing in chart_data.")
        return ''

    chart_header_markdown = f"# {name}\n\n"
    return chart_header_markdown


def get_chart_deprecation_warning(chart_data):
    return "> **:exclamation: This Helm Chart is deprecated!**\n\n"


def get_chart_name(chart_data):
    name = chart_data.get('name')
    if name is None:
        print("Warning: 'name' field is missing in chart_data.")
        return ''

    chart_name_markdown = f"{name}"
    return chart_name_markdown


def get_chart_description(chart_data):
    description = chart_data.get('description')
    if description is None:
        print("Warning: 'description' field is missing in chart_data.")
        return ''

    chart_description_markdown = f"{description}\n\n"
    return chart_description_markdown


def get_chart_version(chart_data):
    version = chart_data.get('version')
    if version is None:
        print("Warning: 'version' field is missing in chart_data.")
        return ''

    chart_version_markdown = f"{version}\n\n"
    return chart_version_markdown


def get_chart_version_badge(chart_data):
    version = chart_data.get('version')
    if version is None:
        print("Warning: 'version' field is missing in chart_data.")
        return ''

    version_badge_markdown = f"![Version: {version}](https://img.shields.io/badge/Version-{version}-informational?style=flat-square)\n\n"
    return version_badge_markdown


def get_chart_type(chart_data):
    chart_type = chart_data.get('type')
    if chart_type is None:
        print("Warning: 'type' field is missing in chart_data.")
        return ''

    chart_type_markdown = f"{chart_type}\n\n"
    return chart_type_markdown


def get_chart_type_badge(chart_data):
    chart_type = chart_data.get('type')
    if chart_type is None:
        print("Warning: 'type' field is missing in chart_data.")
        return ''

    chart_type_badge_markdown = f"![Type: {chart_type}](https://img.shields.io/badge/Type-{chart_type}-informational?style=flat-square)\n\n"
    return chart_type_badge_markdown


def get_chart_app_version(chart_data):
    app_version = chart_data.get('appVersion')
    if app_version is None:
        print("Warning: 'appVersion' field is missing in chart_data.")
        return ''

    chart_app_version_markdown = f"{app_version}\n\n"
    return chart_app_version_markdown


def get_chart_app_version_badge(chart_data):
    app_version = chart_data.get('appVersion')
    if app_version is None:
        print("Warning: 'appVersion' field is missing in chart_data.")
        return ''

    app_version_badge_markdown = f"![AppVersion: {app_version}](https://img.shields.io/badge/AppVersion-{app_version}-informational?style=flat-square)\n\n"
    return app_version_badge_markdown


def get_chart_badges_section(chart_data):
    version = chart_data.get('version')
    chart_type = chart_data.get('type')
    app_version = chart_data.get('appVersion')

    if version is None:
        print("Warning: 'version' field is missing in chart_data.")
        version = ''
    if chart_type is None:
        print("Warning: 'type' field is missing in chart_data.")
        chart_type = ''
    if app_version is None:
        print("Warning: 'appVersion' field is missing in chart_data.")
        app_version = ''

    badges_section_markdown = f"![Version: {version}](https://img.shields.io/badge/Version-{version}-informational?style=flat-square) ![Type: {chart_type}](https://img.shields.io/badge/Type-{chart_type}-informational?style=flat-square) ![AppVersion: {app_version}](https://img.shields.io/badge/AppVersion-{app_version}-informational?style=flat-square)\n\n"
    return badges_section_markdown


def get_chart_homepage(chart_data):
    homepage = chart_data.get('home')
    if homepage is None:
        print("Warning: 'home' field is missing in chart_data.")
        return ''

    homepage_markdown = f"{homepage}\n\n"
    return homepage_markdown


def get_chart_homepage_line(chart_data):
    homepage = chart_data.get('home')
    if homepage is None:
        print("Warning: 'home' field is missing in chart_data.")
        return ''

    homepage_line_markdown = f"**Homepage:** <{homepage}>\n\n"
    return homepage_line_markdown


def get_chart_maintainers_header(chart_data):
    maintainers_header_markdown = "## Maintainers\n\n"
    return maintainers_header_markdown


def get_chart_maintainers_table(chart_data):
    maintainers = chart_data.get('maintainers', [])
    maintainers_table_markdown = "| Name | Email | Url |\n| ---- | ------ | --- |\n"
    for maintainer in maintainers:
        name = maintainer.get('name', '')
        email = maintainer.get('email', '')
        url = maintainer.get('url', '')
        maintainers_table_markdown += f"| {name} | <{email}> | {url} |\n"
    maintainers_table_markdown += "\n"
    return maintainers_table_markdown


def get_chart_maintainers_section(chart_data):
    maintainers_section_markdown = "## Maintainers\n\n" + get_chart_maintainers_table(chart_data) + "\n"
    return maintainers_section_markdown


def get_chart_sources_header(chart_data):
    sources_header_markdown = "## Source Code\n\n"
    return sources_header_markdown


def get_chart_sources_list(chart_data):
    sources = chart_data.get('sources', [])
    sources_list_markdown = ""
    for source in sources:
        sources_list_markdown += f"* <{source}>\n"
    sources_list_markdown += "\n"
    return sources_list_markdown


def get_chart_sources_section(chart_data):
    sources_section_markdown = "## Source Code\n\n" + get_chart_sources_list(chart_data) + "\n"
    return sources_section_markdown


def get_chart_kube_version(chart_data):
    kube_version = chart_data.get('kubeVersion')
    if kube_version is None:
        print("Warning: 'kubeVersion' field is missing in chart_data.")
        return ''

    kube_version_markdown = f"Kubernetes: `{kube_version}`\n\n"
    return kube_version_markdown


def get_chart_kube_version_line(chart_data):
    kube_version = chart_data.get('kubeVersion')
    if kube_version is None:
        print("Warning: 'kubeVersion' field is missing in chart_data.")
        return ''

    kube_version_line_markdown = f"Kubernetes: `{kube_version}`\n\n"
    return kube_version_line_markdown


def get_doxy_helm_version_footer(doxy_helm_version):
    version_footer = f"Autogenerated from chart metadata using [doxy-helm {doxy_helm_version}](https://github.com/tactful-ai/doxyhelm)"
    return version_footer


