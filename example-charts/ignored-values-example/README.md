
# ignored-values-example



![Version: 0.1.0](https://img.shields.io/badge/Version-0.1.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: ](https://img.shields.io/badge/AppVersion--informational?style=flat-square)



Based on best-values-example



**Homepage:** <https://github.com/norwoodj/helm-docs/tree/master/example-charts/ignored-values-example>



## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| Jakub Buczak | <jakub.buczak@gmail.com> |  |




## Source Code

* <https://github.com/norwoodj/helm-docs/tree/master/example-charts/ignored-values-example>




## Values



<h1>-> global</h1><h2>config</h2>
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>config</td><td>dict</td><td><code>`{'databasesToCreate': ['postgresql', 'hashbash'], 'usersToCreate': [{'name': 'root', 'admin': True}, {'name': 'hashbash', 'readwriteDatabases': ['hashbash']}, {'name': 'test', 'readDatabases': ['test']}]}`</code></td><td></td></tr><tr style="" ><td>config.databasesToCreate</td><td>list</td><td><code>`['postgresql', 'hashbash']`</code></td><td></td></tr><tr style="" ><td>config.databasesToCreate[0]</td><td>str</td><td><code>`postgresql`</code></td><td><p><code> default database for storage of database metadata</code></p></td></tr><tr style="" ><td>config.databasesToCreate[1]</td><td>str</td><td><code>`hashbash`</code></td><td><p><code>1.  database for the <a href="https://github.com/norwoodj/hashbash">hashbash</a> project  <br/><br/>2.  database for the <a href="https://github.com/norwoodj/hashbash">hashbash</a> project</code></p></td></tr><tr style="" ><td>config.usersToCreate</td><td>list</td><td><code>`[{'name': 'root', 'admin': True}, {'name': 'hashbash', 'readwriteDatabases': ['hashbash']}, {'name': 'test', 'readDatabases': ['test']}]`</code></td><td></td></tr><tr style="" ><td>config.usersToCreate[0]</td><td>dict</td><td><code>`{'name': 'root', 'admin': True}`</code></td><td><p><code> admin user</code></p></td></tr><tr style="" ><td>config.usersToCreate[1]</td><td>dict</td><td><code>`{'name': 'hashbash', 'readwriteDatabases': ['hashbash']}`</code></td><td><p><code> user with access to the database with the same name</code></p></td></tr><tr style="" ><td>config.usersToCreate[2]</td><td>dict</td><td><code>`{'name': 'test', 'readDatabases': ['test']}`</code></td><td></td></tr>
</table>

<h2>configWithAllValuesIgnored</h2>
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>configWithAllValuesIgnored</td><td>dict</td><td><code>`{'ignoredOne': True, 'ignoredTwo': '?'}`</code></td><td></td></tr><tr style="" ><td>configWithAllValuesIgnored.ignoredOne</td><td>bool</td><td><code>`True`</code></td><td></td></tr><tr style="" ><td>configWithAllValuesIgnored.ignoredTwo</td><td>str</td><td><code>`?`</code></td><td></td></tr>
</table>

<h2>ignoredConfig</h2>
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>ignoredConfig</td><td>int</td><td><code>`6`</code></td><td></td></tr>
</table>

<h2>internalConfig</h2>
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>internalConfig</td><td>dict</td><td><code>`{'rpcPort': 8080, 'generateData': True}`</code></td><td></td></tr><tr style="" ><td>internalConfig.rpcPort</td><td>int</td><td><code>`8080`</code></td><td></td></tr><tr style="" ><td>internalConfig.generateData</td><td>bool</td><td><code>`True`</code></td><td><p><code> this should also be ignored</code></p></td></tr>
</table>

<h2>statefulset</h2>
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>statefulset</td><td>dict</td><td><code>`{'image': {'repository': 'jnorwood/postgresq', 'tag': '11'}, 'extraVolumes': [{'name': 'data', 'emptyDir': {}}], 'livenessProbe': {'enabled': False}, 'podLabels': {}}`</code></td><td></td></tr><tr style="" ><td>statefulset.image</td><td>dict</td><td><code>`{'repository': 'jnorwood/postgresq', 'tag': '11'}`</code></td><td></td></tr><tr style="" ><td>statefulset.image.repository</td><td>str</td><td><code>`jnorwood/postgresq`</code></td><td><p><code> Image to use for deploying, must support an entrypoint</code></p></td></tr><tr style="" ><td>statefulset.image.tag</td><td>str</td><td><code>`11`</code></td><td></td></tr><tr style="" ><td>statefulset.extraVolumes</td><td>list</td><td><code>`[{'name': 'data', 'emptyDir': {}}]`</code></td><td><p><code> Additional volumes to be mounted into the database container</code></p></td></tr><tr style="" ><td>statefulset.extraVolumes[0]</td><td>dict</td><td><code>`{'name': 'data', 'emptyDir': {}}`</code></td><td></td></tr><tr style="" ><td>statefulset.livenessProbe</td><td>dict</td><td><code>`{'enabled': False}`</code></td><td><p><code> Configure the healthcheck for the database</code></p></td></tr><tr style="" ><td>statefulset.livenessProbe.enabled</td><td>bool</td><td><code>`False`</code></td><td></td></tr><tr style="" ><td>statefulset.podLabels</td><td>dict</td><td><code>`{}`</code></td><td><p><code> The labels to be applied to instances of the database</code></p></td></tr>
</table>



Autogenerated from chart metadata using [doxy-helm v1.0.1](https://github.com/tactful-ai/doxyhelm)
    