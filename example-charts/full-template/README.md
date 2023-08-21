
# full-template



![Version: 1.0.0](https://img.shields.io/badge/Version-1.0.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 13.0.0](https://img.shields.io/badge/AppVersion-13.0.0-informational?style=flat-square)



A chart for showing every README-element



**Homepage:** <https://github.com/norwoodj/helm-docs/tree/master/example-charts/full-template>



## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| John Norwood | <norwood.john.m@gmail.com> |  |




## Source Code

* <https://github.com/norwoodj/helm-docs/tree/master/example-charts/full-template>




## Values



<h1>> global</h1><h1>controller</h1><p><code> hello</code></p>
<table style="color: red;color: red;text-align: right;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>controller</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td><p><code> hello</code></p></td></tr><tr style="" ><td>controller.name</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="color: purple;" ><td>controller.image</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>controller.image.repository</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>controller.image.tag</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>controller.persistentVolumeClaims</td><td>list</td><td><code>`[]`</code></td><td></td></tr><tr style="" ><td>controller.extraVolumes</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>controller.extraVolumes[0]</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>controller.ingressClass</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h1>controller13</h1>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>controller13</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>controller13.name</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>controller13.image</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>controller13.image.repository</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>controller13.image.tag</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>controller13.persistentVolumeClaims</td><td>list</td><td><code>`[]`</code></td><td></td></tr><tr style="" ><td>controller13.extraVolumes</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>controller13.extraVolumes[0]</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>controller13.ingressClass</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h1>controller19</h1>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>controller19</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>controller19.name</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>controller19.persistentVolumeClaims</td><td>list</td><td><code>`[]`</code></td><td></td></tr><tr style="" ><td>controller19.extraVolumes</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>controller19.extraVolumes[0]</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>controller19.ingressClass</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h1>services</h1>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>services</td><td>dict</td><td><code>`{'waer': {'controller19': {'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}}}`</code></td><td></td></tr>
</table>

<h1>-> global.mahmoud</h1><h2>controller2</h2>
<table style="color: red;color:pink;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>controller2</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>controller2.name</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>controller2.image</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>controller2.image.repository</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>controller2.image.tag</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>controller2.persistentVolumeClaims</td><td>list</td><td><code>`[]`</code></td><td></td></tr><tr style="background-color:blue;" ><td>controller2.extraVolumes</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>controller2.extraVolumes[0]</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>controller2.ingressClass</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h2>--> global.mahmoud.waer</h2><h3>---> global.mahmoud.waer.king</h3><h4>controller8</h4>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>controller8</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>controller8.name</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>controller8.image</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>controller8.image.repository</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>controller8.image.tag</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>controller8.persistentVolumeClaims</td><td>list</td><td><code>`[]`</code></td><td></td></tr><tr style="" ><td>controller8.extraVolumes</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>controller8.extraVolumes[0]</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>controller8.ingressClass</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h3>---> global.mahmoud.waer.kok</h3><h4>controller9</h4>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>controller9</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>controller9.name</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>controller9.image</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>controller9.image.repository</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>controller9.image.tag</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>controller9.persistentVolumeClaims</td><td>list</td><td><code>`[]`</code></td><td></td></tr><tr style="" ><td>controller9.extraVolumes</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>controller9.extraVolumes[0]</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>controller9.ingressClass</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h3>---> global.mahmoud.waer.455454ss</h3><h4>----> global.mahmoud.waer.455454ss.stttopp</h4><h5>controller7</h5>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>controller7</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>controller7.name</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>controller7.image</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>controller7.image.repository</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>controller7.image.tag</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>controller7.persistentVolumeClaims</td><td>list</td><td><code>`[]`</code></td><td></td></tr><tr style="" ><td>controller7.extraVolumes</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>controller7.extraVolumes[0]</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>controller7.ingressClass</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h1>-> global.hello</h1><h2>controller3</h2>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>controller3</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>controller3.name</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>controller3.image</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>controller3.image.repository</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>controller3.image.tag</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>controller3.persistentVolumeClaims</td><td>list</td><td><code>`[]`</code></td><td></td></tr><tr style="" ><td>controller3.extraVolumes</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>controller3.extraVolumes[0]</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>controller3.ingressClass</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h1>> dstny</h1><h1>controller4</h1>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>controller4</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>controller4.name</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>controller4.image</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>controller4.image.repository</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>controller4.image.tag</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>controller4.persistentVolumeClaims</td><td>list</td><td><code>`[]`</code></td><td></td></tr><tr style="" ><td>controller4.extraVolumes</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>controller4.extraVolumes[0]</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>controller4.ingressClass</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h1>-> dstny.hamada</h1><h2>controller12</h2>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>controller12</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>controller12.name</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>controller12.image</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>controller12.image.repository</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>controller12.image.tag</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>controller12.persistentVolumeClaims</td><td>list</td><td><code>`[]`</code></td><td></td></tr><tr style="" ><td>controller12.extraVolumes</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>controller12.extraVolumes[0]</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>controller12.ingressClass</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h2>controller6</h2>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>controller6</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>controller6.name</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>controller6.image</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>controller6.image.repository</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>controller6.image.tag</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>controller6.persistentVolumeClaims</td><td>list</td><td><code>`[]`</code></td><td></td></tr><tr style="" ><td>controller6.extraVolumes</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>controller6.extraVolumes[0]</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>controller6.ingressClass</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h2>controller19.image</h2>
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>controller19.image</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>controller19.image.repository</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>controller19.image.tag</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr>
</table>

<h2>--> dstny.hamada.tooto</h2><h3>controller5</h3>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>controller5</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>controller5.name</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>controller5.image</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>controller5.image.repository</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>controller5.image.tag</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>controller5.persistentVolumeClaims</td><td>list</td><td><code>`[]`</code></td><td></td></tr><tr style="" ><td>controller5.extraVolumes</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>controller5.extraVolumes[0]</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>controller5.ingressClass</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h3>---> dstny.hamada.tooto.soso</h3><h4>controller11</h4><p><code> this is so good</code></p>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>controller11</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td><p><code> this is so good</code></p></td></tr><tr style="" ><td>controller11.name</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>controller11.image</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>controller11.image.repository</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>controller11.image.tag</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>controller11.persistentVolumeClaims</td><td>list</td><td><code>`[]`</code></td><td></td></tr><tr style="" ><td>controller11.extraVolumes</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>controller11.extraVolumes[0]</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>controller11.ingressClass</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h3>---> dstny.hamada.tooto.kiki</h3><h4>controller56</h4>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>controller56</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>controller56.name</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>controller56.image</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>controller56.image.repository</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>controller56.image.tag</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>controller56.persistentVolumeClaims</td><td>list</td><td><code>`[]`</code></td><td></td></tr><tr style="" ><td>controller56.extraVolumes</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>controller56.extraVolumes[0]</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>controller56.ingressClass</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h1>> test</h1><h1>controller14</h1>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>controller14</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>controller14.name</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>controller14.image</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>controller14.image.repository</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>controller14.image.tag</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>controller14.persistentVolumeClaims</td><td>list</td><td><code>`[]`</code></td><td></td></tr><tr style="" ><td>controller14.extraVolumes</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>controller14.extraVolumes[0]</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>controller14.ingressClass</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h1>controller15</h1>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>controller15</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>controller15.name</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>controller15.image</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>controller15.image.repository</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>controller15.image.tag</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>controller15.persistentVolumeClaims</td><td>list</td><td><code>`[]`</code></td><td></td></tr><tr style="" ><td>controller15.extraVolumes</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>controller15.extraVolumes[0]</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>controller15.ingressClass</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h1>controller16</h1>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>controller16</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>controller16.name</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>controller16.image</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>controller16.image.repository</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>controller16.image.tag</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>controller16.persistentVolumeClaims</td><td>list</td><td><code>`[]`</code></td><td></td></tr><tr style="" ><td>controller16.extraVolumes</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>controller16.extraVolumes[0]</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>controller16.ingressClass</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h1>-> test.test2</h1><h2>controller17</h2>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>controller17</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>controller17.name</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>controller17.image</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>controller17.image.repository</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>controller17.image.tag</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>controller17.persistentVolumeClaims</td><td>list</td><td><code>`[]`</code></td><td></td></tr><tr style="" ><td>controller17.extraVolumes</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>controller17.extraVolumes[0]</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>controller17.ingressClass</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h2>controller18</h2>
<table style="color: red;">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>controller18</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>controller18.name</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>controller18.image</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>controller18.image.repository</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>controller18.image.tag</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>controller18.persistentVolumeClaims</td><td>list</td><td><code>`[]`</code></td><td></td></tr><tr style="" ><td>controller18.extraVolumes</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>controller18.extraVolumes[0]</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>controller18.ingressClass</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>

<h1>> nginx-ingress</h1><h1>services.waer</h1>
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>services.waer</td><td>dict</td><td><code>`{'controller19': {'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}}`</code></td><td></td></tr><tr style="" ><td>services.waer.controller19</td><td>dict</td><td><code>`{'name': 'controller', 'image': {'repository': 'nginx-ingress-controller', 'tag': '18.0831'}, 'persistentVolumeClaims': [], 'extraVolumes': [{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}], 'ingressClass': 'nginx'}`</code></td><td></td></tr><tr style="" ><td>services.waer.controller19.name</td><td>str</td><td><code>`controller`</code></td><td></td></tr><tr style="" ><td>services.waer.controller19.image</td><td>dict</td><td><code>`{'repository': 'nginx-ingress-controller', 'tag': '18.0831'}`</code></td><td></td></tr><tr style="" ><td>services.waer.controller19.image.repository</td><td>str</td><td><code>`nginx-ingress-controller`</code></td><td></td></tr><tr style="" ><td>services.waer.controller19.image.tag</td><td>str</td><td><code>`18.0831`</code></td><td></td></tr><tr style="" ><td>services.waer.controller19.persistentVolumeClaims</td><td>list</td><td><code>`[]`</code></td><td></td></tr><tr style="" ><td>services.waer.controller19.extraVolumes</td><td>list</td><td><code>`[{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}]`</code></td><td></td></tr><tr style="" ><td>services.waer.controller19.extraVolumes[0]</td><td>dict</td><td><code>`{'name': 'config-volume', 'configMap': {'name': 'nginx-ingress-config'}}`</code></td><td></td></tr><tr style="" ><td>services.waer.controller19.ingressClass</td><td>str</td><td><code>`nginx`</code></td><td></td></tr>
</table>



Autogenerated from chart metadata using [doxy-helm v1.0.1](https://github.com/tactful-ai/doxyhelm)
    