doxy-helm
=========

The doxy-helm tool auto-generates documentation from helm charts into markdown files. The resulting files contain metadata about their respective chart and a table with each of the chart's values, their defaults, and an optional description parsed from comments.


The markdown generation is entirely [gotemplate](https://golang.org/pkg/text/template)(Currently) driven. The tool parses metadata from charts and generates a number of sub-templates that can be referenced in a template file (by default `README.md.gotmpl`).
If no template file is provided, the tool has a default internal template that will generate a reasonably formatted README.

## Features

- **Documentation Generation:** Automatically generates documentation from Helm charts into markdown files.
- **Metadata Inclusion:** Provides comprehensive metadata about charts and their corresponding values.
- **Comment Parsing:** Parses descriptions and default values from comments in Helm charts.
- **Template-Driven:** Utilizes [gotemplate](https://golang.org/pkg/text/template) for markdown generation (Currently).
- **Custom CSS:** Allows the addition of custom CSS for each element in tables, including entire tables or specific rows.
- **Global CSS:** Enables the application of global CSS to all elements in all tables.
- **Table Manipulation:** Transfers and reorders tables to sections of your choice.
- **Chart Directory Exclusion:** Supports the use of `.helmdocsignore` files to ignore specific chart directories.
- **Subdirectory Search:** Facilitates the auto-search for charts in subdirectories using the `--chart-search-root` flag.
- **Table Ordering:** Provides table ordering options by key, type, default, or description using the `--order-by` flag.

## Future Features

- **Ignoring Elements:** Introduces the capability to ignore elements or entire tables using the `@ignore` tag.
- **File Inclusion:** Enables loading different files inside the Go template for more flexibility.
- **Direct Go Template Rendering:** Allows rendering of direct Go templates for advanced customization.
- **Column Navigation:** Links each column name to the corresponding data line in the source file.
- **Default Values:** You dont have to provide defult value every time ou can add comment that represent the default value by `@default`.

The most useful aspect of this tool is the auto-detection of field descriptions from comments:
```yaml
# -- Image to use for deploying, must support an entrypoint which creates users/databases from appropriate config files
statefulset:
  image:
    # -- Imeeeeeage to use for deploying, must support an entrypoint which creates users/databases from appropriate config files
    # -- [section=global] Image to use for depeeloying, must support an entrypoint which creates users/databases from appropriate config files
    repository: jnorwood/postgresq
    tag: "11"

  # -- Additional volumes to be mounted into the database container
  extraVolumes:
      # this is commeooooooooooooontc
    - name: data
      emptyDir: {}
      emptyDisr: {}
      # this is comment

      emptyDisqr: {}

  # -- Configure the healthcheck for the database
  livenessProbe:
    enabled: false

  # -- The labels to be applied to instances of the database
  podLabels: {}
```

Resulting in a resulting README section like so:

<h1>> global</h1>

<h1>statefulset</h1><p><code> Image to use for deploying, must support an entrypoint which creates users/databases from appropriate config files</code></p>
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>statefulset</td><td>dict</td><td><code>`{'image': {'repository': 'jnorwood/postgresq', 'tag': '11'}, 'extraVolumes': [{'name': 'data', 'emptyDir': {}, 'emptyDisr': {}, 'emptyDisqr': {}}], 'livenessProbe': {'enabled': False}, 'podLabels': {}}`</code></td><td><p><code> Image to use for deploying, must support an entrypoint which creates users/databases from appropriate config files</code></p></td></tr><tr style="" ><td>statefulset.image</td><td>dict</td><td><code>`{'repository': 'jnorwood/postgresq', 'tag': '11'}`</code></td><td></td></tr><tr style="" ><td>statefulset.image.repository</td><td>str</td><td><code>`jnorwood/postgresq`</code></td><td><p><code> Imeeeeeage to use for deploying, must support an entrypoint which creates users/databases from appropriate config files</code></p></td></tr><tr style="" ><td>statefulset.image.tag</td><td>str</td><td><code>`11`</code></td><td></td></tr><tr style="" ><td>statefulset.extraVolumes</td><td>list</td><td><code>`[{'name': 'data', 'emptyDir': {}, 'emptyDisr': {}, 'emptyDisqr': {}}]`</code></td><td><p><code> Additional volumes to be mounted into the database container</code></p></td></tr><tr style="" ><td>statefulset.extraVolumes[0]</td><td>dict</td><td><code>`{'name': 'data', 'emptyDir': {}, 'emptyDisr': {}, 'emptyDisqr': {}}`</code></td><td></td></tr><tr style="" ><td>statefulset.livenessProbe</td><td>dict</td><td><code>`{'enabled': False}`</code></td><td><p><code> Configure the healthcheck for the database</code></p></td></tr><tr style="" ><td>statefulset.livenessProbe.enabled</td><td>bool</td><td><code>`False`</code></td><td></td></tr><tr style="" ><td>statefulset.podLabels</td><td>dict</td><td><code>`{}`</code></td><td><p><code> The labels to be applied to instances of the database</code></p></td></tr>
</table>


You may observe that certain intricate fields (lists and dictionaries) are documented, while others are not. Additionally, simple fields such as statefulset.image.tag are documented even in the absence of a description comment. The criteria determining what gets documented in the final table and what does not will be elaborated on later in this document.


## Installation
doxy-helm can be installed using [pip](https://pypi.org/project/pip/):

```bash
pip install doxy-helm
```

To build from source in this repository:

```bash
git clone https://github.com/tactful-ai/doxy-helm
cd doxy-helm
python setup.py sdist bdist_wheel
pip install .
```

## Usage

### Using Docker

```bash
docker run -v ./Helm-files-location:/app  doxy-helm
```

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

To run and generate documentation into READMEs for all helm charts within or recursively contained by a directory:

```bash
doxy
# OR
doxy --dry-run # prints generated documentation to stdout rather than modifying READMEs
```

The tool searches recursively through subdirectories of the current directory for `Chart.yaml` files and generates documentation for every chart that it finds.

### Using docker

You can mount a directory with charts under `/doxy-helm` within the container.

Then run:

```bash
docker run --rm --volume "$(pwd):/doxy-helm" -u $(id -u) waer1/doxy-helm:latest
```

## Ignoring Chart Directories
The doxy-helm tool supports a .helmdocsignore file, similar to a .gitignore file, where you can specify directories to be excluded from the chart search process. This feature allows you to ignore directories that might contain multiple charts or unrelated files, ensuring that only the desired charts are processed. You can also directly reference the Chart.yaml file for a specific chart to prevent it from being processed.

By using the .helmdocsignore file, you have the flexibility to tailor the chart search process to your project's structure and requirements. This is particularly useful when you want to focus on specific charts and exclude others that are not relevant for documentation generation.


## Markdown Rendering
When utilizing the doxy-helm tool, it's crucial to be mindful of two essential parameters. The first parameter, --chart-search-root, designates the root directory from which the tool will conduct a recursive search for charts to generate documentation for. The second parameter, --template-files, specifies a list of gotemplate files that should be employed in crafting the resulting markdown file for each discovered chart. By default, the values for these parameters are --chart-search-root=. and --template-files=README.md.gotmpl.

Should you provide a template file using just its filename, this indicates that the file should be interpreted as being relative to each individual chart directory found. Conversely, if a template file is provided as a relative path, such as in the form of --template-files=./_templates.gotmpl --template-files=README.md.gotmpl, then it is interpreted as being relative to the chart-search-root. This level of flexibility enables you to adapt the template usage according to the specific location and structure of your chart directories.

This repo is a good example of this in action. If you take a look at the [.pre-commit-config.yaml file](./.pre-commit-config.yaml)
here, you'll see our search root is set to [example-charts](./example-charts) and the list of templates used for each chart is the [_templates.gotmpl file in that directory](./example-charts/_templates.gotmpl) and the README.md.gotmpl file in each chart directory.

If any of the specified template files is not found for a chart (you'll notice most of the example charts do not have a README.md.gotmpl)
file, then the internal default template is used instead.

In addition to extra defined templates you specify in these template files, there are quite a few built-in templates that
can be used as well:

| Name | Description |
|------|-------------|
| chart.header              | The main heading of the generated markdown file |
| chart.name                | The _name_ field from the chart's `Chart.yaml` file |
| chart.deprecationWarning  | A deprecation warning which is displayed when the _deprecated_ field from the chart's `Chart.yaml` file is `true` |
| chart.description         | A description line containing the _description_ field from the chart's `Chart.yaml` file, or "" if that field is not set |
| chart.version             | The _version_ field from the chart's `Chart.yaml` file |
| chart.versionBadge        | A badge stating the current version of the chart |
| chart.type                | The _type_ field from the chart's `Chart.yaml` file |
| chart.typeBadge           | A badge stating the current type of the chart |
| chart.appVersion          | The _appVersion_ field from the chart's `Chart.yaml` file |
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

The default internal template mentioned above uses many of these and looks like this:
```
{{ template "chart.header" . }}
{{ template "chart.deprecationWarning" . }}

{{ template "chart.badgesSection" . }}

{{ template "chart.description" . }}

{{ template "chart.homepageLine" . }}

{{ template "chart.maintainersSection" . }}

{{ template "chart.sourcesSection" . }}

{{ template "chart.requirementsSection" . }}

{{ template "chart.valuesSection" . }}
```

The tool also includes the internal comment parser, so those functions can be used in the templates you supply.

### values.yaml metadata
This tool can parse descriptions and defaults of values from `values.yaml` files. The defaults are pulled directly from
the yaml in the file.


```yaml
controller:
  publishService:
    # -- Whether to expose the ingress controller to the public world
    enabled: false

  # -- Number of nginx-ingress pods to load balance between.
  # Do not set this below 2.
  replicas: 2
```

I invite you to check out the [example-charts](./example-charts) to see how this is done in practice. The `but-auto-comments` examples in particular document the new comment format.

Note that comments is only for the line that start with # -- . In that case leave out the double dash, and the lines will simply be appended with a space in-between, as in the `controller.replicas` field in the example above

The following rules are used to determine which values will be added to the values table in the README:

* By default, only _leaf nodes_, that is, fields of type `int`, `string`, `float`, `bool`, empty lists, and empty maps
  are added as rows in the values table. These fields will be added even if they do not have a description comment
* Lists and maps which contain elements will be added as rows in the values table.
  comment which refers to them

e.g. In this case, both `livenessProbe` and `livenessProbe.httpGet.path` will be added as rows in
the values table, also `livenessProbe.httpGet.port` will be added
```yaml
# -- Configure the healthcheck for the ingress controller
livenessProbe:
  httpGet:
    # -- This is the liveness check endpoint
    path: /healthz
    port: http
```

Results in:

<h1>livenessProbe</h1>
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>livenessProbe</td><td>dict</td><td><code>`{'httpGet': {'path': '/healthz', 'port': 'http'}}`</code></td><td><p><code> Configure the healthcheck for the ingress controller</code></p></td></tr><tr style="" ><td>livenessProbe.httpGet</td><td>dict</td><td><code>`{'path': '/healthz', 'port': 'http'}`</code></td><td></td></tr><tr style="" ><td>livenessProbe.httpGet.path</td><td>str</td><td><code>`/healthz`</code></td><td><p><code> This is the liveness check endpoint</code></p></td></tr><tr style="" ><td>livenessProbe.httpGet.port</td><td>str</td><td><code>`http`</code></td><td></td></tr>
</table>

### Custom css
you can add css for one table or element in table or even for add tables in the values section by adding `@customcss` tag to the start of table.
and for each single css that can be added to the table or element in table or even for add tables in the values section by adding `-- {the css you want}` tag to the start of table.
```yaml
# -- @custom_css {color: red;}
# -- hello
# -- {text-align: right;}
controller:
  name: controller
  # -- {color: purple;}
  image:
    repository: nginx-ingress-controller
    tag: "18.0831"
```

and the result aable will be look like that:

<h1>controller</h1><p><code> hello</code></p>
<table style="color: red;color: red;text-align: right;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>controller</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td><p><code> hello</code></p></td></tr><tr style="" ><td>controller.name</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="color: purple;" ><td>controller.image</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>controller.image.repository</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>controller.image.tag</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr>
</table>

### organize and reorder the table
You can easily divide your tables into logical sections and reorder them by adding a `[]` tag at the start of the table's comment. This action will relocate the table to the desired section and allow you to reorder it according to your preference. This approach enables you to effectively organize and structure the tables within the values section, aligning with your desired logical order.
You should take care of transfering table since it executes in order of less `.` that mean big section will be transfered before the small one.

```yaml
  # -- [section-main]
statefulset:
  image:
    # -- Imeeeeeage to use for deploying, must support an entrypoint which creates users/databases from appropriate config files
    repository: jnorwood/postgresq
    tag: "11"
```
it will be rendered as follow:

<h1>> section-main</h1><h1>statefulset</h1><p><code> Image to use for deploying, must support an entrypoint which creates users/databases from appropriate config files</code></p>
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>statefulset</td><td>dict</td><td><code>`{'image': {'repository': 'jnorwood/postgresq', 'tag': '11'}, 'extraVolumes': [{'name': 'data', 'emptyDir': {}, 'emptyDisr': {}, 'emptyDisqr': {}}], 'livenessProbe': {'enabled': False}, 'podLabels': {}}`</code></td><td><p><code> Image to use for deploying, must support an entrypoint which creates users/databases from appropriate config files</code></p></td></tr><tr style="" ><td>statefulset.image</td><td>dict</td><td><code>`{'repository': 'jnorwood/postgresq', 'tag': '11'}`</code></td><td></td></tr><tr style="" ><td>statefulset.image.repository</td><td>str</td><td><code>`jnorwood/postgresq`</code></td><td><p><code> Imeeeeeage to use for deploying, must support an entrypoint which creates users/databases from appropriate config files</code></p></td></tr><tr style="" ><td>statefulset.image.tag</td><td>str</td><td><code>`11`</code></td><td></td></tr><tr style="" ><td>statefulset.extraVolumes</td><td>list</td><td><code>`[{'name': 'data', 'emptyDir': {}, 'emptyDisr': {}, 'emptyDisqr': {}}]`</code></td><td><p><code> Additional volumes to be mounted into the database container</code></p></td></tr><tr style="" ><td>statefulset.extraVolumes[0]</td><td>dict</td><td><code>`{'name': 'data', 'emptyDir': {}, 'emptyDisr': {}, 'emptyDisqr': {}}`</code></td><td></td></tr><tr style="" ><td>statefulset.livenessProbe</td><td>dict</td><td><code>`{'enabled': False}`</code></td><td><p><code> Configure the healthcheck for the database</code></p></td></tr><tr style="" ><td>statefulset.livenessProbe.enabled</td><td>bool</td><td><code>`False`</code></td><td></td></tr><tr style="" ><td>statefulset.podLabels</td><td>dict</td><td><code>`{}`</code></td><td><p><code> The labels to be applied to instances of the database</code></p></td></tr>
</table>

### nil values
If you would like to define a key for a value, but leave the default empty, you can still specify a description for it
as well as a type. This is possible with both the old and the new comment format:
```yaml
controller:
  # -- (int) Number of nginx-ingress pods to load balance between
  replicas:

  # controller.image -- (string) Number of nginx-ingress pods to load balance between
  image:
```
This could be useful when wanting to enforce user-defined values for the chart, where there are no sensible defaults.

### Default values/column (Soon)
In cases where you do not want to include the default value from `values.yaml`, or where the real default is calculated
inside the chart, you can change the contents of the column like so:

```yaml
service:
  # -- Add annotations to the service, this is going to be a long comment across multiple lines
  # but that's fine, these will be concatenated and the @default will be rendered as the default for this field
  # @default -- the chart will add some internal annotations automatically
  annotations: []
```

See [here](./example-charts/custom-template/values.yaml) for an example.
### Ignoring values
In cases you would like to ignore certain values, you can mark it with @ignored tag:

```yaml
# @ignored
service:
  port: 8080
```



