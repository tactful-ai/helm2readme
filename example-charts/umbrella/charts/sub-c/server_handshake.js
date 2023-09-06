helm-docs
=========
[![Go Report Card](https://goreportcard.com/badge/github.com/norwoodj/helm-docs)](https://goreportcard.com/report/github.com/norwoodj/helm-docs)

The helm-docs tool auto-generates documentation from helm charts into markdown files. The resulting
files contain metadata about their respective chart and a table with each of the chart's values, their defaults, and an
optional description parsed from comments.

The markdown generation is entirely [gotemplate](https://golang.org/pkg/text/template) driven. The tool parses metadata
from charts and generates a number of sub-templates that can be referenced in a template file (by default `README.md.gotmpl`).
If no template file is provided, the tool has a default internal template that will generate a reasonably formatted README.

The most useful aspect of this tool is the auto-detection of field descriptions from comments:
```yaml
config:
  databasesToCreate:
    # -- default database for storage of database metadata
    - postgres

    # -- database for the [hashbash](https://github.com/norwoodj/hashbash-backend-go) project
    - hashbash

  usersToCreate:
    # -- admin user
    - {name: root, admin: true}

    # -- user with access to the database with the same name
    - {name: hashbash, readwriteDatabases: [hashbash]}

statefulset:
  image:
    # -- Image to use for deploying, must support an entrypoint which creates users/databases from appropriate config files
    repository: jnorwood/postgresql
    tag: "11"

  # -- Additional volumes to be mounted into the database container
  extraVolumes:
    - name: data
      emptyDir: {}
```

Resulting in a resulting README section like so:

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| config.databasesToCreate[0] | string | `"postgresql"` | default database for storage of database metadata |
| config.databasesToCreate[1] | string | `"hashbash"` | database for the [hashbash](https://github.com/norwoodj/hashbash-backend-go) project |
| config.usersToCreate[0] | object | `{"admin":true,"name":"root"}` | admin user |
| config.usersToCreate[1] | object | `{"name":"hashbash","readwriteDatabases":["hashbash"]}` | user with access to the database with the same name |
| statefulset.extraVolumes | list | `[{"emptyDir":{},"name":"data"}]` | Additional volumes to be mounted into the database container |
| statefulset.image.repository | string | `"jnorwood/postgresql:11"` | Image to use for deploying, must support an entrypoint which creates users/databases from appropriate config files |
| statefulset.image.tag | string | `"18.0831"` |  |

You'll notice that some complex fields (lists and objects) are documented while others aren't, and that some simple fields
like `statefulset.image.tag` are documented even without a description comment. The rules for what is and isn't documented in
the final table will be described in detail later in this document.

## Installation
helm-docs can be installed using [homebrew](https://brew.sh/):

```bash
brew install norwoodj/tap/helm-docs
```

or [scoop](https://scoop.sh):

```bash
scoop install helm-docs
```

This will download and install the [latest release](https://github.com/norwoodj/helm-docs/releases/latest)
of the tool.

To build from source in this repository:

```bash
cd cmd/helm-docs
go build
```

Or install from source:

```bash
GO111MODULE=on go get github.com/norwoodj/helm-docs/cmd/helm-docs
```

## Usage

### Pre-commit hook

If you want to automatically generate `README.md` files with a pre-commit hook, make sure you
[install the pre-commit binary](https://pre-commit.com/#install), and add a [.pre-commit-config.yaml file](./.pre-commit-config.yaml)
to your project. Then run:

```bash
pre-commit install
pre-commit install-hooks
```

Future changes to your chart's `requirements.yaml`, `values.yaml`, `Chart.yaml`, or `README.md.gotmpl` files will cause an update to documentation when you commit.

### Running the binary directly

To run and geThe _appVersion_ field from the chart's `Chart.yaml` file |
| chart.appVersionBadge     | A badge stating the current appVersion of the chart |
| chart.homepage            | The _home_ link from the chart's `Chart.yaml` file, or "" if that field is not set |
| chart.homepageLine        | A text line stating the current homepage of the chart |
| chart.maintainersHeader   | The heading for the chart maintainers section |
| chart.maintainersTable    | A table of the chart's maintainers |
| chart.maintainersSection  | A section headed by the maintainersHeader from above containing the maintainersTable from above or "" if there are no maintainers |
| chart.sourcesHeader       | The heading for the chart sources section |
| chart.sourcesList         | A list of the chart's sources |
| chart.sourcesSection      | A section headed by the sourcesHeader from above containing the sourcesList from above or "" if there are no sources |
| chart.kubeVersion         | The _kubeVersion_ field from the chart's `Chart.yaml` file |
| chart.kubeVersionLine     | A text line stating the required Kubernetes version for the chart |~~~~
| chart.requirementsHeader  | The heading for the chart requirements section |
| chart.requirementsTable   | A table of the chart's required sub-charts |
| chart.requirementsSection | A section headed by the requirementsHeader from above containing the kubeVersionLine and/or the requirementsTable from above or "" if there are no requirements |
| chart.valuesHeader        | The heading for the chart values section |
| chart.valuesTable         | A table of the chart's values parsed from the `values.yaml` file (see below) |
| chart.valuesSection       | A section headed by the valuesHeader from above containing the valuesTable from above or "" if there are no values |
| chart.valuesTableHtml     | Like `chart.valuesTable` but it is rendered as (X)HTML tags to allow further rendering customization, instead of markdown tables format. |
| chart.valuesSectionHtml   | Like `chart.valuesSection` but uses `chart.valuesTableHtml` |
| chart.valueDefaultColumnRender | This is a hook template if you want to redefine how helm-docs render the default values in `chart.valuesTableHtml` mode. This is especially useful when combined with (X)HTML tags, so that you can nicely format multiline default values, like YAML/JSON object tree snippet with codeblock syntax highlighter, which is not possi