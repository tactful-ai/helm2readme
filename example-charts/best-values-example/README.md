
# best-values-example



![Version: 0.2.0](https://img.shields.io/badge/Version-0.2.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: ](https://img.shields.io/badge/AppVersion--informational?style=flat-square)



One of the best values parsing example charts here, exhibits several more complicated examples



**Homepage:** <https://github.com/norwoodj/helm-docs/tree/master/example-charts/best-values-example>



## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| John Norwood | <norwood.john.m@gmail.com> |  |




## Source Code

* <https://github.com/norwoodj/helm-docs/tree/master/example-charts/best-values-example>




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

[config](.\values.yaml#L26)

</td><td>dict</td><td><code>`{'databasesToCreate': ['postgresql', 'hashbash'], 'usersToCreate': [{'name': 'root', 'admin': True}, {'name': 'hashbash', 'readwriteDatabases': ['hashbash']}]}`</code></td><td></td></tr><tr style="" ><td>

[config.databasesToCreate](.\values.yaml#L28)

</td><td>list</td><td><code>`['postgresql', 'hashbash']`</code></td><td><p><code> default database for storage of database metadataaaaaaa</code></p></td></tr><tr style="" ><td>

[config.databasesToCreate[0]](.\values.yaml#L28)

</td><td>str</td><td><code>`postgresql`</code></td><td><p><code> default database for storage of database metadata</code></p></td></tr><tr style="" ><td>

[config.databasesToCreate[1]](.\values.yaml#L28)

</td><td>str</td><td><code>`hashbash`</code></td><td><p><code> database for the <a href="https://github.com/norwoodj/hashbash">hashbash</a> project</code></p></td></tr><tr style="" ><td>

[config.usersToCreate](.\values.yaml#L36)

</td><td>list</td><td><code>`[{'name': 'root', 'admin': True}, {'name': 'hashbash', 'readwriteDatabases': ['hashbash']}]`</code></td><td></td></tr><tr style="" ><td>

[config.usersToCreate[0]](.\values.yaml#L36)

</td><td>dict</td><td><code>`{'name': 'root', 'admin': True}`</code></td><td><p><code> admin user</code></p></td></tr><tr style="" ><td>

[config.usersToCreate[1]](.\values.yaml#L36)

</td><td>dict</td><td><code>`{'name': 'hashbash', 'readwriteDatabases': ['hashbash']}`</code></td><td><p><code> user with access to the database with the same name</code></p></td></tr>
</table>

<h1>services</h1>
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[services](.\values.yaml#L53)

</td><td>dict</td><td><code>`{'api': {'image': None, 'tag': None}, 'front': {'image': None, 'tag': None}, 'elasticsearch': {'image': None, 'tag': None}}`</code></td><td></td></tr><tr style="" ><td>

[services.elasticsearch](.\values.yaml#L65)

</td><td>dict</td><td><code>`{'image': None, 'tag': None}`</code></td><td></td></tr><tr style="" ><td>

[services.elasticsearch.image](.\values.yaml#L66)

</td><td>NoneType</td><td><code>`None`</code></td><td></td></tr><tr style="" ><td>

[services.elasticsearch.tag](.\values.yaml#L67)

</td><td>NoneType</td><td><code>`None`</code></td><td></td></tr>
</table>

<h1>> section-main</h1><h1>statefulset</h1><p><code> Image to use for deploying, must support an entrypoint which creates users/databases from appropriate config files</code></p>
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[statefulset](.\values.yaml#L3)

</td><td>dict</td><td><code>`{'image': {'repository': 'jnorwood/postgresq', 'tag': '11'}, 'extraVolumes': [{'name': 'data', 'emptyDir': {}, 'emptyDisr': {}, 'emptyDisqr': {}}], 'livenessProbe': {'enabled': False}, 'podLabels': {}}`</code></td><td><p><code> Image to use for deploying, must support an entrypoint which creates users/databases from appropriate config files</code></p></td></tr><tr style="" ><td>

[statefulset.image](.\values.yaml#L4)

</td><td>dict</td><td><code>`{'repository': 'jnorwood/postgresq', 'tag': '11'}`</code></td><td></td></tr><tr style="" ><td>

[statefulset.image.repository](.\values.yaml#L6)

</td><td>str</td><td><code>`jnorwood/postgresq`</code></td><td><p><code> Imeeeeeage to use for deploying, must support an entrypoint which creates users/databases from appropriate config files</code></p></td></tr><tr style="" ><td>

[statefulset.image.tag](.\values.yaml#L7)

</td><td>str</td><td><code>`11`</code></td><td></td></tr><tr style="" ><td>

[statefulset.extraVolumes](.\values.yaml#L10)

</td><td>list</td><td><code>`[{'name': 'data', 'emptyDir': {}, 'emptyDisr': {}, 'emptyDisqr': {}}]`</code></td><td><p><code> Additional volumes to be mounted into the database container</code></p></td></tr><tr style="" ><td>

[statefulset.extraVolumes[0]](.\values.yaml#L10)

</td><td>dict</td><td><code>`{'name': 'data', 'emptyDir': {}, 'emptyDisr': {}, 'emptyDisqr': {}}`</code></td><td></td></tr><tr style="" ><td>

[statefulset.livenessProbe](.\values.yaml#L20)

</td><td>dict</td><td><code>`{'enabled': False}`</code></td><td><p><code> Configure the healthcheck for the database</code></p></td></tr><tr style="" ><td>

[statefulset.livenessProbe.enabled](.\values.yaml#L21)

</td><td>bool</td><td><code>`False`</code></td><td></td></tr><tr style="" ><td>

[statefulset.podLabels](.\values.yaml#L24)

</td><td>dict</td><td><code>`{}`</code></td><td><p><code> The labels to be applied to instances of the database</code></p></td></tr>
</table>

<h1>> section=api</h1><h1>services.api</h1>
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[services.api](.\values.yaml#L56)

</td><td>dict</td><td><code>`{'image': None, 'tag': None}`</code></td><td></td></tr><tr style="" ><td>

[services.api.image](.\values.yaml#L57)

</td><td>NoneType</td><td><code>`None`</code></td><td></td></tr><tr style="" ><td>

[services.api.tag](.\values.yaml#L58)

</td><td>NoneType</td><td><code>`None`</code></td><td></td></tr>
</table>

<h1>> section=frontend</h1><h1>services.front</h1>
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[services.front](.\values.yaml#L61)

</td><td>dict</td><td><code>`{'image': None, 'tag': None}`</code></td><td></td></tr><tr style="" ><td>

[services.front.image](.\values.yaml#L62)

</td><td>NoneType</td><td><code>`None`</code></td><td></td></tr><tr style="" ><td>

[services.front.tag](.\values.yaml#L63)

</td><td>NoneType</td><td><code>`None`</code></td><td></td></tr>
</table>

<h1>> section=global</h1><h1>-> section=global.billing</h1><h2>billing</h2>
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[billing](.\values.yaml#L44)

</td><td>dict</td><td><code>`{'stripApiKey': 'hello'}`</code></td><td></td></tr><tr style="" ><td>

[billing.stripApiKey](.\values.yaml#L45)

</td><td>str</td><td><code>`hello`</code></td><td></td></tr>
</table>

<h1>-> section=global.subscription</h1><h2>subscription</h2>
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[subscription](.\values.yaml#L48)

</td><td>dict</td><td><code>`{'subscriptionApiKey': 'hello2'}`</code></td><td></td></tr><tr style="" ><td>

[subscription.subscriptionApiKey](.\values.yaml#L49)

</td><td>str</td><td><code>`hello2`</code></td><td></td></tr>
</table>



Autogenerated from chart metadata using [doxy-helm v1.0.1](https://github.com/tactful-ai/doxyhelm)
    