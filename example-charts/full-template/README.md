# full-template




## `extra.flower`
Extra Flower Replacement

## `chart.deprecationWarning`
> **:exclamation: This Helm Chart is deprecated!**



## `chart.name`

full-template

## `chart.description`

A chart for showing every README-element



## `chart.version`

1.0.0



## `chart.versionBadge`

![Version: 1.0.0](https://img.shields.io/badge/Version-1.0.0-informational?style=flat-square)



## `chart.type`

application




## `chart.typeBadge`

![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)



## `chart.appVersion`

13.0.0



## `chart.appVersionBadge`

![AppVersion: 13.0.0](https://img.shields.io/badge/AppVersion-13.0.0-informational?style=flat-square)



## `chart.badgesSection`

![Version: 1.0.0](https://img.shields.io/badge/Version-1.0.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 13.0.0](https://img.shields.io/badge/AppVersion-13.0.0-informational?style=flat-square)



## `chart.homepage`

https://github.com/norwoodj/helm-docs/tree/master/example-charts/full-template



## `chart.homepageLine`

**Homepage:** <https://github.com/norwoodj/helm-docs/tree/master/example-charts/full-template>



## `chart.maintainersHeader`

## Maintainers



## `chart.maintainersTable`

| Name | Email | Url |
| ---- | ------ | --- |
| John Norwood | <norwood.john.m@gmail.com> |  |



## `chart.maintainersSection`

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| John Norwood | <norwood.john.m@gmail.com> |  |




## `chart.sourcesHeader`

## Source Code



## `chart.sourcesList`

* <https://github.com/norwoodj/helm-docs/tree/master/example-charts/full-template>



## `chart.sourcesSection`

## Source Code

* <https://github.com/norwoodj/helm-docs/tree/master/example-charts/full-template>




## `chart.kubeVersion`

Kubernetes: `<=1.18`



## `chart.kubeVersionLine`

Kubernetes: `<=1.18`



## `chart.requirementsHeader`

## Requirements



## `chart.requirementsTable`

| Repository | Name | Version |
|------------|------|---------|
| @stable | nginx-ingress | 0.22.1 |



## `chart.requirementsSection`

## Requirements

 | Repository | Name | Version |
|------------|------|---------|
| @stable | nginx-ingress | 0.22.1 |




## `chart.valuesHeader`

## Values



## `chart.valuesTable`

<h1>> global</h1><h1>controller</h1><p><code> hello</code></p>
<table style="color: red;color: red;text-align: right;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller](.\values.yaml#L4)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td><p><code> hello</code></p></td></tr><tr style="" ><td>

[controller.name](.\values.yaml#L5)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="color: purple;" ><td>

[controller.image](.\values.yaml#L7)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller.image.repository](.\values.yaml#L8)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller.image.tag](.\values.yaml#L9)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller.persistentVolumeClaims](.\values.yaml#L14)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[controller.extraVolumes](.\values.yaml#L16)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller.extraVolumes[0]](.\values.yaml#L16)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller.ingressClass](.\values.yaml#L23)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h1>controller13</h1>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller13](.\values.yaml#L46)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[controller13.name](.\values.yaml#L47)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller13.image](.\values.yaml#L48)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller13.image.repository](.\values.yaml#L49)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller13.image.tag](.\values.yaml#L50)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller13.persistentVolumeClaims](.\values.yaml#L55)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[controller13.extraVolumes](.\values.yaml#L57)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller13.extraVolumes[0]](.\values.yaml#L57)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller13.ingressClass](.\values.yaml#L64)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h1>controller19</h1>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller19](.\values.yaml#L396)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[controller19.name](.\values.yaml#L397)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller19.persistentVolumeClaims](.\values.yaml#L406)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[controller19.extraVolumes](.\values.yaml#L408)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller19.extraVolumes[0]](.\values.yaml#L408)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller19.ingressClass](.\values.yaml#L415)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h1>services</h1>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[services](.\values.yaml#L418)

</td><td>dict</td><td><code>`{'waer': {'controller19': {'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}}}`</code></td><td></td></tr>
</table>

<h1>-> global.mahmoud</h1><h2>controller2</h2>
<table style="color: red;color:pink;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller2](.\values.yaml#L91)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[controller2.name](.\values.yaml#L92)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller2.image](.\values.yaml#L93)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller2.image.repository](.\values.yaml#L94)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller2.image.tag](.\values.yaml#L95)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller2.persistentVolumeClaims](.\values.yaml#L100)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="background-color:blue;" ><td>

[controller2.extraVolumes](.\values.yaml#L103)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller2.extraVolumes[0]](.\values.yaml#L103)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller2.ingressClass](.\values.yaml#L110)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h2>--> global.mahmoud.waer</h2><h3>---> global.mahmoud.waer.king</h3><h4>controller8</h4>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller8](.\values.yaml#L220)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[controller8.name](.\values.yaml#L221)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller8.image](.\values.yaml#L222)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller8.image.repository](.\values.yaml#L223)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller8.image.tag](.\values.yaml#L224)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller8.persistentVolumeClaims](.\values.yaml#L229)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[controller8.extraVolumes](.\values.yaml#L231)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller8.extraVolumes[0]](.\values.yaml#L231)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller8.ingressClass](.\values.yaml#L238)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h3>---> global.mahmoud.waer.kok</h3><h4>controller9</h4>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller9](.\values.yaml#L242)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[controller9.name](.\values.yaml#L243)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller9.image](.\values.yaml#L244)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller9.image.repository](.\values.yaml#L245)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller9.image.tag](.\values.yaml#L246)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller9.persistentVolumeClaims](.\values.yaml#L251)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[controller9.extraVolumes](.\values.yaml#L253)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller9.extraVolumes[0]](.\values.yaml#L253)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller9.ingressClass](.\values.yaml#L260)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h3>---> global.mahmoud.waer.455454ss</h3><h4>----> global.mahmoud.waer.455454ss.stttopp</h4><h5>controller7</h5>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller7](.\values.yaml#L198)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[controller7.name](.\values.yaml#L199)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller7.image](.\values.yaml#L200)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller7.image.repository](.\values.yaml#L201)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller7.image.tag](.\values.yaml#L202)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller7.persistentVolumeClaims](.\values.yaml#L207)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[controller7.extraVolumes](.\values.yaml#L209)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller7.extraVolumes[0]](.\values.yaml#L209)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller7.ingressClass](.\values.yaml#L216)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h1>-> global.hello</h1><h2>controller3</h2>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller3](.\values.yaml#L113)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[controller3.name](.\values.yaml#L114)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller3.image](.\values.yaml#L115)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller3.image.repository](.\values.yaml#L116)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller3.image.tag](.\values.yaml#L117)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller3.persistentVolumeClaims](.\values.yaml#L122)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[controller3.extraVolumes](.\values.yaml#L124)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller3.extraVolumes[0]](.\values.yaml#L124)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller3.ingressClass](.\values.yaml#L131)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h1>> dstny</h1><h1>controller4</h1>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller4](.\values.yaml#L134)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[controller4.name](.\values.yaml#L135)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller4.image](.\values.yaml#L136)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller4.image.repository](.\values.yaml#L137)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller4.image.tag](.\values.yaml#L138)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller4.persistentVolumeClaims](.\values.yaml#L143)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[controller4.extraVolumes](.\values.yaml#L145)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller4.extraVolumes[0]](.\values.yaml#L145)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller4.ingressClass](.\values.yaml#L152)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h1>-> dstny.hamada</h1><h2>controller12</h2>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller12](.\values.yaml#L26)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[controller12.name](.\values.yaml#L27)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller12.image](.\values.yaml#L28)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller12.image.repository](.\values.yaml#L29)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller12.image.tag](.\values.yaml#L30)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller12.persistentVolumeClaims](.\values.yaml#L35)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[controller12.extraVolumes](.\values.yaml#L37)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller12.extraVolumes[0]](.\values.yaml#L37)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller12.ingressClass](.\values.yaml#L44)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h2>controller6</h2>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller6](.\values.yaml#L176)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[controller6.name](.\values.yaml#L177)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller6.image](.\values.yaml#L178)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller6.image.repository](.\values.yaml#L179)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller6.image.tag](.\values.yaml#L180)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller6.persistentVolumeClaims](.\values.yaml#L185)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[controller6.extraVolumes](.\values.yaml#L187)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller6.extraVolumes[0]](.\values.yaml#L187)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller6.ingressClass](.\values.yaml#L194)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h2>controller19.image</h2>
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller19.image](.\values.yaml#L399)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller19.image.repository](.\values.yaml#L400)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller19.image.tag](.\values.yaml#L401)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr>
</table>

<h2>--> dstny.hamada.tooto</h2><h3>controller5</h3>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller5](.\values.yaml#L155)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[controller5.name](.\values.yaml#L156)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller5.image](.\values.yaml#L157)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller5.image.repository](.\values.yaml#L158)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller5.image.tag](.\values.yaml#L159)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller5.persistentVolumeClaims](.\values.yaml#L164)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[controller5.extraVolumes](.\values.yaml#L166)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller5.extraVolumes[0]](.\values.yaml#L166)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller5.ingressClass](.\values.yaml#L173)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h3>---> dstny.hamada.tooto.soso</h3><h4>controller11</h4><p><code> this is so good</code></p>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller11](.\values.yaml#L69)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td><p><code> this is so good</code></p></td></tr><tr style="" ><td>

[controller11.name](.\values.yaml#L70)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller11.image](.\values.yaml#L71)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller11.image.repository](.\values.yaml#L72)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller11.image.tag](.\values.yaml#L73)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller11.persistentVolumeClaims](.\values.yaml#L78)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[controller11.extraVolumes](.\values.yaml#L80)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller11.extraVolumes[0]](.\values.yaml#L80)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller11.ingressClass](.\values.yaml#L87)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h3>---> dstny.hamada.tooto.kiki</h3><h4>controller56</h4>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller56](.\values.yaml#L265)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[controller56.name](.\values.yaml#L266)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller56.image](.\values.yaml#L267)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller56.image.repository](.\values.yaml#L268)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller56.image.tag](.\values.yaml#L269)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller56.persistentVolumeClaims](.\values.yaml#L274)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td><p><code>1.  List of persistent volume claims to create.  <br/><br/>2.  For very long comments, break them into multiple lines.</code></p></td></tr><tr style="" ><td>

[controller56.extraVolumes](.\values.yaml#L277)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td><p><code> this is the extra volume for any additional data</code></p></td></tr><tr style="" ><td>

[controller56.extraVolumes[0]](.\values.yaml#L277)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller56.ingressClass](.\values.yaml#L284)

</td><td>str</td><td><code>`nginx`</code></td><td><p><code> controller.ingressClass -- Name of the ingress class to route through this controller</code></p></td></tr>
</table>

<h1>> test</h1><h1>controller14</h1>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller14](.\values.yaml#L288)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[controller14.name](.\values.yaml#L289)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller14.image](.\values.yaml#L290)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller14.image.repository](.\values.yaml#L291)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller14.image.tag](.\values.yaml#L292)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller14.persistentVolumeClaims](.\values.yaml#L297)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[controller14.extraVolumes](.\values.yaml#L299)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller14.extraVolumes[0]](.\values.yaml#L299)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller14.ingressClass](.\values.yaml#L306)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h1>controller15</h1>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller15](.\values.yaml#L310)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[controller15.name](.\values.yaml#L311)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller15.image](.\values.yaml#L312)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller15.image.repository](.\values.yaml#L313)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller15.image.tag](.\values.yaml#L314)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller15.persistentVolumeClaims](.\values.yaml#L319)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[controller15.extraVolumes](.\values.yaml#L321)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller15.extraVolumes[0]](.\values.yaml#L321)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller15.ingressClass](.\values.yaml#L328)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h1>controller16</h1>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller16](.\values.yaml#L332)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[controller16.name](.\values.yaml#L333)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller16.image](.\values.yaml#L334)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller16.image.repository](.\values.yaml#L335)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller16.image.tag](.\values.yaml#L336)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller16.persistentVolumeClaims](.\values.yaml#L341)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[controller16.extraVolumes](.\values.yaml#L343)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller16.extraVolumes[0]](.\values.yaml#L343)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller16.ingressClass](.\values.yaml#L350)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h1>-> test.test2</h1><h2>controller17</h2>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller17](.\values.yaml#L355)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[controller17.name](.\values.yaml#L356)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller17.image](.\values.yaml#L357)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller17.image.repository](.\values.yaml#L358)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller17.image.tag](.\values.yaml#L359)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller17.persistentVolumeClaims](.\values.yaml#L364)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[controller17.extraVolumes](.\values.yaml#L366)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller17.extraVolumes[0]](.\values.yaml#L366)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller17.ingressClass](.\values.yaml#L373)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h2>controller18</h2>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller18](.\values.yaml#L376)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[controller18.name](.\values.yaml#L377)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller18.image](.\values.yaml#L378)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller18.image.repository](.\values.yaml#L379)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller18.image.tag](.\values.yaml#L380)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller18.persistentVolumeClaims](.\values.yaml#L385)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[controller18.extraVolumes](.\values.yaml#L387)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller18.extraVolumes[0]](.\values.yaml#L387)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller18.ingressClass](.\values.yaml#L394)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h1>> nginx-ingress</h1><h1>services.waer</h1>
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[services.waer](.\values.yaml#L420)

</td><td>dict</td><td><code>`{'controller19': {'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}}`</code></td><td></td></tr><tr style="" ><td>

[services.waer.controller19](.\values.yaml#L421)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[services.waer.controller19.name](.\values.yaml#L422)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[services.waer.controller19.image](.\values.yaml#L423)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[services.waer.controller19.image.repository](.\values.yaml#L424)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[services.waer.controller19.image.tag](.\values.yaml#L425)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[services.waer.controller19.persistentVolumeClaims](.\values.yaml#L430)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[services.waer.controller19.extraVolumes](.\values.yaml#L432)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[services.waer.controller19.extraVolumes[0]](.\values.yaml#L432)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[services.waer.controller19.ingressClass](.\values.yaml#L439)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>



## `chart.valuesSection`

## Values



<h1>> global</h1><h1>controller</h1><p><code> hello</code></p>
<table style="color: red;color: red;text-align: right;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller](.\values.yaml#L4)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td><p><code> hello</code></p></td></tr><tr style="" ><td>

[controller.name](.\values.yaml#L5)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="color: purple;" ><td>

[controller.image](.\values.yaml#L7)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller.image.repository](.\values.yaml#L8)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller.image.tag](.\values.yaml#L9)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller.persistentVolumeClaims](.\values.yaml#L14)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[controller.extraVolumes](.\values.yaml#L16)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller.extraVolumes[0]](.\values.yaml#L16)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller.ingressClass](.\values.yaml#L23)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h1>controller13</h1>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller13](.\values.yaml#L46)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[controller13.name](.\values.yaml#L47)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller13.image](.\values.yaml#L48)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller13.image.repository](.\values.yaml#L49)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller13.image.tag](.\values.yaml#L50)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller13.persistentVolumeClaims](.\values.yaml#L55)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[controller13.extraVolumes](.\values.yaml#L57)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller13.extraVolumes[0]](.\values.yaml#L57)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller13.ingressClass](.\values.yaml#L64)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h1>controller19</h1>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller19](.\values.yaml#L396)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[controller19.name](.\values.yaml#L397)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller19.persistentVolumeClaims](.\values.yaml#L406)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[controller19.extraVolumes](.\values.yaml#L408)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller19.extraVolumes[0]](.\values.yaml#L408)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller19.ingressClass](.\values.yaml#L415)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h1>services</h1>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[services](.\values.yaml#L418)

</td><td>dict</td><td><code>`{'waer': {'controller19': {'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}}}`</code></td><td></td></tr>
</table>

<h1>-> global.mahmoud</h1><h2>controller2</h2>
<table style="color: red;color:pink;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller2](.\values.yaml#L91)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[controller2.name](.\values.yaml#L92)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller2.image](.\values.yaml#L93)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller2.image.repository](.\values.yaml#L94)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller2.image.tag](.\values.yaml#L95)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller2.persistentVolumeClaims](.\values.yaml#L100)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="background-color:blue;" ><td>

[controller2.extraVolumes](.\values.yaml#L103)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller2.extraVolumes[0]](.\values.yaml#L103)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller2.ingressClass](.\values.yaml#L110)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h2>--> global.mahmoud.waer</h2><h3>---> global.mahmoud.waer.king</h3><h4>controller8</h4>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller8](.\values.yaml#L220)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[controller8.name](.\values.yaml#L221)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller8.image](.\values.yaml#L222)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller8.image.repository](.\values.yaml#L223)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller8.image.tag](.\values.yaml#L224)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller8.persistentVolumeClaims](.\values.yaml#L229)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[controller8.extraVolumes](.\values.yaml#L231)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller8.extraVolumes[0]](.\values.yaml#L231)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller8.ingressClass](.\values.yaml#L238)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h3>---> global.mahmoud.waer.kok</h3><h4>controller9</h4>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller9](.\values.yaml#L242)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[controller9.name](.\values.yaml#L243)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller9.image](.\values.yaml#L244)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller9.image.repository](.\values.yaml#L245)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller9.image.tag](.\values.yaml#L246)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller9.persistentVolumeClaims](.\values.yaml#L251)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[controller9.extraVolumes](.\values.yaml#L253)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller9.extraVolumes[0]](.\values.yaml#L253)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller9.ingressClass](.\values.yaml#L260)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h3>---> global.mahmoud.waer.455454ss</h3><h4>----> global.mahmoud.waer.455454ss.stttopp</h4><h5>controller7</h5>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller7](.\values.yaml#L198)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[controller7.name](.\values.yaml#L199)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller7.image](.\values.yaml#L200)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller7.image.repository](.\values.yaml#L201)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller7.image.tag](.\values.yaml#L202)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller7.persistentVolumeClaims](.\values.yaml#L207)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[controller7.extraVolumes](.\values.yaml#L209)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller7.extraVolumes[0]](.\values.yaml#L209)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller7.ingressClass](.\values.yaml#L216)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h1>-> global.hello</h1><h2>controller3</h2>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller3](.\values.yaml#L113)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[controller3.name](.\values.yaml#L114)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller3.image](.\values.yaml#L115)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller3.image.repository](.\values.yaml#L116)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller3.image.tag](.\values.yaml#L117)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller3.persistentVolumeClaims](.\values.yaml#L122)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[controller3.extraVolumes](.\values.yaml#L124)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller3.extraVolumes[0]](.\values.yaml#L124)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller3.ingressClass](.\values.yaml#L131)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h1>> dstny</h1><h1>controller4</h1>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller4](.\values.yaml#L134)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[controller4.name](.\values.yaml#L135)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller4.image](.\values.yaml#L136)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller4.image.repository](.\values.yaml#L137)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller4.image.tag](.\values.yaml#L138)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller4.persistentVolumeClaims](.\values.yaml#L143)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[controller4.extraVolumes](.\values.yaml#L145)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller4.extraVolumes[0]](.\values.yaml#L145)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller4.ingressClass](.\values.yaml#L152)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h1>-> dstny.hamada</h1><h2>controller12</h2>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller12](.\values.yaml#L26)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[controller12.name](.\values.yaml#L27)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller12.image](.\values.yaml#L28)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller12.image.repository](.\values.yaml#L29)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller12.image.tag](.\values.yaml#L30)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller12.persistentVolumeClaims](.\values.yaml#L35)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[controller12.extraVolumes](.\values.yaml#L37)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller12.extraVolumes[0]](.\values.yaml#L37)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller12.ingressClass](.\values.yaml#L44)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h2>controller6</h2>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller6](.\values.yaml#L176)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[controller6.name](.\values.yaml#L177)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller6.image](.\values.yaml#L178)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller6.image.repository](.\values.yaml#L179)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller6.image.tag](.\values.yaml#L180)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller6.persistentVolumeClaims](.\values.yaml#L185)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[controller6.extraVolumes](.\values.yaml#L187)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller6.extraVolumes[0]](.\values.yaml#L187)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller6.ingressClass](.\values.yaml#L194)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h2>controller19.image</h2>
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller19.image](.\values.yaml#L399)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller19.image.repository](.\values.yaml#L400)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller19.image.tag](.\values.yaml#L401)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr>
</table>

<h2>--> dstny.hamada.tooto</h2><h3>controller5</h3>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller5](.\values.yaml#L155)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[controller5.name](.\values.yaml#L156)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller5.image](.\values.yaml#L157)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller5.image.repository](.\values.yaml#L158)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller5.image.tag](.\values.yaml#L159)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller5.persistentVolumeClaims](.\values.yaml#L164)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[controller5.extraVolumes](.\values.yaml#L166)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller5.extraVolumes[0]](.\values.yaml#L166)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller5.ingressClass](.\values.yaml#L173)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h3>---> dstny.hamada.tooto.soso</h3><h4>controller11</h4><p><code> this is so good</code></p>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller11](.\values.yaml#L69)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td><p><code> this is so good</code></p></td></tr><tr style="" ><td>

[controller11.name](.\values.yaml#L70)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller11.image](.\values.yaml#L71)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller11.image.repository](.\values.yaml#L72)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller11.image.tag](.\values.yaml#L73)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller11.persistentVolumeClaims](.\values.yaml#L78)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[controller11.extraVolumes](.\values.yaml#L80)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller11.extraVolumes[0]](.\values.yaml#L80)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller11.ingressClass](.\values.yaml#L87)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h3>---> dstny.hamada.tooto.kiki</h3><h4>controller56</h4>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller56](.\values.yaml#L265)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[controller56.name](.\values.yaml#L266)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller56.image](.\values.yaml#L267)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller56.image.repository](.\values.yaml#L268)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller56.image.tag](.\values.yaml#L269)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller56.persistentVolumeClaims](.\values.yaml#L274)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td><p><code>1.  List of persistent volume claims to create.  <br/><br/>2.  For very long comments, break them into multiple lines.</code></p></td></tr><tr style="" ><td>

[controller56.extraVolumes](.\values.yaml#L277)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td><p><code> this is the extra volume for any additional data</code></p></td></tr><tr style="" ><td>

[controller56.extraVolumes[0]](.\values.yaml#L277)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller56.ingressClass](.\values.yaml#L284)

</td><td>str</td><td><code>`nginx`</code></td><td><p><code> controller.ingressClass -- Name of the ingress class to route through this controller</code></p></td></tr>
</table>

<h1>> test</h1><h1>controller14</h1>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller14](.\values.yaml#L288)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[controller14.name](.\values.yaml#L289)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller14.image](.\values.yaml#L290)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller14.image.repository](.\values.yaml#L291)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller14.image.tag](.\values.yaml#L292)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller14.persistentVolumeClaims](.\values.yaml#L297)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[controller14.extraVolumes](.\values.yaml#L299)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller14.extraVolumes[0]](.\values.yaml#L299)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller14.ingressClass](.\values.yaml#L306)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h1>controller15</h1>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller15](.\values.yaml#L310)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[controller15.name](.\values.yaml#L311)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller15.image](.\values.yaml#L312)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller15.image.repository](.\values.yaml#L313)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller15.image.tag](.\values.yaml#L314)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller15.persistentVolumeClaims](.\values.yaml#L319)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[controller15.extraVolumes](.\values.yaml#L321)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller15.extraVolumes[0]](.\values.yaml#L321)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller15.ingressClass](.\values.yaml#L328)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h1>controller16</h1>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller16](.\values.yaml#L332)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[controller16.name](.\values.yaml#L333)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller16.image](.\values.yaml#L334)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller16.image.repository](.\values.yaml#L335)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller16.image.tag](.\values.yaml#L336)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller16.persistentVolumeClaims](.\values.yaml#L341)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[controller16.extraVolumes](.\values.yaml#L343)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller16.extraVolumes[0]](.\values.yaml#L343)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller16.ingressClass](.\values.yaml#L350)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h1>-> test.test2</h1><h2>controller17</h2>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller17](.\values.yaml#L355)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[controller17.name](.\values.yaml#L356)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller17.image](.\values.yaml#L357)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller17.image.repository](.\values.yaml#L358)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller17.image.tag](.\values.yaml#L359)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller17.persistentVolumeClaims](.\values.yaml#L364)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[controller17.extraVolumes](.\values.yaml#L366)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller17.extraVolumes[0]](.\values.yaml#L366)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller17.ingressClass](.\values.yaml#L373)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h2>controller18</h2>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[controller18](.\values.yaml#L376)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[controller18.name](.\values.yaml#L377)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[controller18.image](.\values.yaml#L378)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[controller18.image.repository](.\values.yaml#L379)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[controller18.image.tag](.\values.yaml#L380)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[controller18.persistentVolumeClaims](.\values.yaml#L385)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[controller18.extraVolumes](.\values.yaml#L387)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[controller18.extraVolumes[0]](.\values.yaml#L387)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[controller18.ingressClass](.\values.yaml#L394)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h1>> nginx-ingress</h1><h1>services.waer</h1>
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>

[services.waer](.\values.yaml#L420)

</td><td>dict</td><td><code>`{'controller19': {'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}}`</code></td><td></td></tr><tr style="" ><td>

[services.waer.controller19](.\values.yaml#L421)

</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>

[services.waer.controller19.name](.\values.yaml#L422)

</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>

[services.waer.controller19.image](.\values.yaml#L423)

</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>

[services.waer.controller19.image.repository](.\values.yaml#L424)

</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>

[services.waer.controller19.image.tag](.\values.yaml#L425)

</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>

[services.waer.controller19.persistentVolumeClaims](.\values.yaml#L430)

</td><td>str</td><td><code>`-- the chart will construct this list internally unless specified`</code></td><td></td></tr><tr style="" ><td>

[services.waer.controller19.extraVolumes](.\values.yaml#L432)

</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>

[services.waer.controller19.extraVolumes[0]](.\values.yaml#L432)

</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>

[services.waer.controller19.ingressClass](.\values.yaml#L439)

</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>



Autogenerated from chart metadata using [doxy-helm v1.0.1](https://github.com/tactful-ai/doxyhelm)
