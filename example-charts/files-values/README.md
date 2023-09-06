# best-values-example


One of the best values parsing example charts here, exhibits several more complicated examples



![Version: 0.2.0](https://img.shields.io/badge/Version-0.2.0-informational?style=flat-square)

![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)



## Additional Information

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore
et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum.

## Installing the Chart

To install the chart with the release name `my-release`:

```console
$ helm repo add foo-bar http://charts.foo-bar.com
$ helm install my-release foo-bar/best-values-example
```

Some file contents:

```
{{ .Files.Get "somefile.yaml" }}
```

Glob contents as config map:

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: test
data:
{{ (.Files.Glob "templates/**.yaml").AsConfig | indent 2 }}
dataSecret:
{{ (.Files.Glob "templates/**.yaml").AsSecrets | indent 2 }}
```

## Requirements

 | Repository | Name | Version |
|------------|------|---------|




## Values



<h1>> global</h1><h1>config</h1>
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[config](.\values.yaml#L19)

</td><td>dict</td><td><code>`{'databasesToCreate': ['postgresql', 'hashbash'], 'usersToCreate': [{'name': 'root', 'admin': True}, {'name': 'hashbash', 'readwriteDatabases': ['hashbash']}]}`</code></td><td></td></tr><tr style="" ><td>

[config.databasesToCreate](.\values.yaml#L20)

</td><td>list</td><td><code>`['postgresql', 'hashbash']`</code></td><td></td></tr><tr style="" ><td>

[config.databasesToCreate[0]](.\values.yaml#L20)

</td><td>str</td><td><code>`postgresql`</code></td><td><p><code> default database for storage of database metadata</code></p></td></tr><tr style="" ><td>

[config.databasesToCreate[1]](.\values.yaml#L20)

</td><td>str</td><td><code>`hashbash`</code></td><td><p><code> database for the <a href="https://github.com/norwoodj/hashbash">hashbash</a> project</code></p></td></tr><tr style="" ><td>

[config.usersToCreate](.\values.yaml#L27)

</td><td>list</td><td><code>`[{'name': 'root', 'admin': True}, {'name': 'hashbash', 'readwriteDatabases': ['hashbash']}]`</code></td><td></td></tr><tr style="" ><td>

[config.usersToCreate[0]](.\values.yaml#L27)

</td><td>dict</td><td><code>`{'name': 'root', 'admin': True}`</code></td><td><p><code> admin user</code></p></td></tr><tr style="" ><td>

[config.usersToCreate[1]](.\values.yaml#L27)

</td><td>dict</td><td><code>`{'name': 'hashbash', 'readwriteDatabases': ['hashbash']}`</code></td><td><p><code> user with access to the database with the same name</code></p></td></tr>
</table>

<h1>statefulset</h1>
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[statefulset](.\values.yaml#L1)

</td><td>dict</td><td><code>`{'image': {'repository': 'jnorwood/postgresq', 'tag': '11'}, 'extraVolumes': [{'name': 'data', 'emptyDir': {}}], 'livenessProbe': {'enabled': False}, 'podLabels': {}}`</code></td><td></td></tr><tr style="" ><td>

[statefulset.image](.\values.yaml#L2)

</td><td>dict</td><td><code>`{'repository': 'jnorwood/postgresq', 'tag': '11'}`</code></td><td></td></tr><tr style="" ><td>

[statefulset.image.repository](.\values.yaml#L4)

</td><td>str</td><td><code>`jnorwood/postgresq`</code></td><td><p><code> Image to use for deploying, must support an entrypoint which creates users/databases from appropriate config files</code></p></td></tr><tr style="" ><td>

[statefulset.image.tag](.\values.yaml#L5)

</td><td>str</td><td><code>`11`</code></td><td></td></tr><tr style="" ><td>

[statefulset.extraVolumes](.\values.yaml#L8)

</td><td>list</td><td><code>`[{'name': 'data', 'emptyDir': {}}]`</code></td><td><p><code> Additional volumes to be mounted into the database container</code></p></td></tr><tr style="" ><td>

[statefulset.extraVolumes[0]](.\values.yaml#L8)

</td><td>dict</td><td><code>`{'name': 'data', 'emptyDir': {}}`</code></td><td></td></tr><tr style="" ><td>

[statefulset.livenessProbe](.\values.yaml#L13)

</td><td>dict</td><td><code>`{'enabled': False}`</code></td><td><p><code> Configure the healthcheck for the database</code></p></td></tr><tr style="" ><td>

[statefulset.livenessProbe.enabled](.\values.yaml#L14)

</td><td>bool</td><td><code>`False`</code></td><td></td></tr><tr style="" ><td>

[statefulset.podLabels](.\values.yaml#L17)

</td><td>dict</td><td><code>`{}`</code></td><td><p><code> The labels to be applied to instances of the database</code></p></td></tr>
</table>



Autogenerated from chart metadata using [doxy-helm v1.0.1](https://github.com/tactful-ai/doxyhelm)
