
# django



![Version: 0.2.1](https://img.shields.io/badge/Version-0.2.1-informational?style=flat-square) ![Type: ](https://img.shields.io/badge/Type--informational?style=flat-square) ![AppVersion: 3.1](https://img.shields.io/badge/AppVersion-3.1-informational?style=flat-square)



Generic chart for basic Django-based web app



**Homepage:** <https://www.djangoproject.com/>



## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| Rizky Maulana Nugraha | <lana.pcfre@gmail.com> |  |




## Source Code

* <https://github.com/django/django>




## Values



<h1>-> global</h1><h2>extraConfigMap</h2> (tpl/dict) Define this for extra config map to be included in django-shared-config
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>

</table>


</table>

<h2>extraPodEnv</h2> (tpl/array) Define this for extra Django environment variables
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>

</table>


</table>

<h2>extraPodSpec</h2> (tpl/object) This will be evaluated as pod spec
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>

</table>


</table>

<h2>extraSecret</h2> (tpl/dict) Define this for extra secrets to be included in django-shared-secret secret
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>

</table>


</table>

<h2>extraVolume</h2> (tpl/array) Define this for extra volume (in pair with extraVolumeMounts)
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>

</table>


</table>

<h2>extraVolumeMounts</h2> (tpl/array) Define this for extra volume mounts in the pod
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>

</table>


</table>

<h2>global</h2> This key name is used for service interconnection between subcharts and parent charts.
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>global</td><td>dict</td><td><code>`{'nameOverride': 'django', 'existingSecret': '', 'sharedSecretName': 'django-shared-secret', 'siteName': 'django', 'djangoCommand': '["/opt/django/scripts/docker-entrypoint.sh"]', 'djangoArgs': '["uwsgi","--chdir=${REPO_ROOT}","--module=${MAIN_APP_NAME}.wsgi","--socket=:8000","--http=0.0.0.0:8080","--processes=5","--buffer-size=8192"]', 'adminUser': 'admin', 'adminPassword': {'value': None, 'valueFrom': {'secretKeyRef': {'name': None, 'key': 'admin-password'}}}, 'adminEmail': 'admin@localhost', 'djangoSecretKey': {'value': None, 'valueFrom': {'secretKeyRef': {'name': None, 'key': 'django-secret'}}}, 'databaseUsername': 'django_db_user', 'databasePassword': {'value': None, 'valueFrom': {'secretKeyRef': {'name': None, 'key': 'database-password'}}}, 'databaseName': 'django', 'databaseHost': 'postgis', 'databasePort': 5432, 'debug': 'False', 'mainAppName': 'django', 'djangoSettingsModule': 'django.settings', 'rootURLConf': 'django.urls', 'staticRoot': '/opt/django/static', 'mediaRoot': '/opt/django/media'}`</code></td><td><code> This key name is used for service interconnection between subcharts and parent charts.</code></td></tr><tr style="" ><td>global.nameOverride</td><td>str</td><td><code>`django`</code></td><td></td></tr><tr style="" ><td>global.existingSecret</td><td>tpl/string</td><td><code>``</code></td><td><code> (tpl/string) Name of existing secret</code></td></tr><tr style="" ><td>global.sharedSecretName</td><td>string</td><td><code>`django-shared-secret`</code></td><td><code> (string) Name of shared secret store that will be generated</code></td></tr><tr style="" ><td>global.siteName</td><td>string</td><td><code>`django`</code></td><td><code> (string) The site name. It will be used to construct url such as http://django/</code></td></tr><tr style="" ><td>global.djangoCommand</td><td>tpl/array</td><td><code>`["/opt/django/scripts/docker-entrypoint.sh"]`</code></td><td><code> (tpl/array) The django entrypoint command to execute</code></td></tr><tr style="" ><td>global.djangoArgs</td><td>tpl/array</td><td><code>`["uwsgi","--chdir=${REPO_ROOT}","--module=${MAIN_APP_NAME}.wsgi","--socket=:8000","--http=0.0.0.0:8080","--processes=5","--buffer-size=8192"]`</code></td><td><code> (tpl/array) The django command args to be passed to entrypoint command</code></td></tr><tr style="" ><td>global.adminUser</td><td>string</td><td><code>`admin`</code></td><td><code> (string) Default super user admin username</code></td></tr><tr style="" ><td>global.adminPassword</td><td>dict</td><td><code>`{'value': None, 'valueFrom': {'secretKeyRef': {'name': None, 'key': 'admin-password'}}}`</code></td><td></td></tr><tr style="" ><td>global.adminPassword.value</td><td>string</td><td><code>`None`</code></td><td><code> (string) Specify this password value. If not, it will be autogenerated everytime chart upgraded</code></td></tr><tr style="" ><td>global.adminPassword.valueFrom</td><td>dict</td><td><code>`{'secretKeyRef': {'name': None, 'key': 'admin-password'}}`</code></td><td></td></tr><tr style="" ><td>global.adminPassword.valueFrom.secretKeyRef</td><td>dict</td><td><code>`{'name': None, 'key': 'admin-password'}`</code></td><td></td></tr><tr style="" ><td>global.adminPassword.valueFrom.secretKeyRef.name</td><td>NoneType</td><td><code>`None`</code></td><td></td></tr><tr style="" ><td>global.adminPassword.valueFrom.secretKeyRef.key</td><td>str</td><td><code>`admin-password`</code></td><td></td></tr><tr style="" ><td>global.adminEmail</td><td>string/email</td><td><code>`admin@localhost`</code></td><td><code> (string/email) Default admin email sender</code></td></tr><tr style="" ><td>global.djangoSecretKey</td><td>dict</td><td><code>`{'value': None, 'valueFrom': {'secretKeyRef': {'name': None, 'key': 'django-secret'}}}`</code></td><td></td></tr><tr style="" ><td>global.djangoSecretKey.value</td><td>string</td><td><code>`None`</code></td><td><code> (string) Specify this Django Secret string value. If not, it will be autogenerated everytime chart upgraded</code></td></tr><tr style="" ><td>global.djangoSecretKey.valueFrom</td><td>dict</td><td><code>`{'secretKeyRef': {'name': None, 'key': 'django-secret'}}`</code></td><td></td></tr><tr style="" ><td>global.djangoSecretKey.valueFrom.secretKeyRef</td><td>dict</td><td><code>`{'name': None, 'key': 'django-secret'}`</code></td><td></td></tr><tr style="" ><td>global.djangoSecretKey.valueFrom.secretKeyRef.name</td><td>NoneType</td><td><code>`None`</code></td><td></td></tr><tr style="" ><td>global.djangoSecretKey.valueFrom.secretKeyRef.key</td><td>str</td><td><code>`django-secret`</code></td><td></td></tr><tr style="" ><td>global.databaseUsername</td><td>string</td><td><code>`django_db_user`</code></td><td><code> (string) Database username backend to connect to. If you use external backend, provide the value</code></td></tr><tr style="" ><td>global.databasePassword</td><td>dict</td><td><code>`{'value': None, 'valueFrom': {'secretKeyRef': {'name': None, 'key': 'database-password'}}}`</code></td><td></td></tr><tr style="" ><td>global.databasePassword.value</td><td>string</td><td><code>`None`</code></td><td><code> (string) Specify this password value. If not, it will be autogenerated everytime chart upgraded. If you use external backend, you must provide the value</code></td></tr><tr style="" ><td>global.databasePassword.valueFrom</td><td>dict</td><td><code>`{'secretKeyRef': {'name': None, 'key': 'database-password'}}`</code></td><td></td></tr><tr style="" ><td>global.databasePassword.valueFrom.secretKeyRef</td><td>dict</td><td><code>`{'name': None, 'key': 'database-password'}`</code></td><td></td></tr><tr style="" ><td>global.databasePassword.valueFrom.secretKeyRef.name</td><td>NoneType</td><td><code>`None`</code></td><td></td></tr><tr style="" ><td>global.databasePassword.valueFrom.secretKeyRef.key</td><td>str</td><td><code>`database-password`</code></td><td></td></tr><tr style="" ><td>global.databaseName</td><td>string</td><td><code>`django`</code></td><td><code> (string) Django database name</code></td></tr><tr style="" ><td>global.databaseHost</td><td>string</td><td><code>`postgis`</code></td><td><code> (string) Django database host location. By default this chart can generate standard postgres chart. So you can leave it as default. If you use external backend,  you must provide the value</code></td></tr><tr style="" ><td>global.databasePort</td><td>int</td><td><code>`5432`</code></td><td><code> (int) Django database port. By default this chart can generate standard postgres chart. So you can leave it as default. If you use external backend,  you must provide the value</code></td></tr><tr style="" ><td>global.debug</td><td>string</td><td><code>`False`</code></td><td><code> (string) Python boolean literal, this will correspond to `DEBUG` environment variable inside the Django container. Useful as a debug switch.</code></td></tr><tr style="" ><td>global.mainAppName</td><td>string</td><td><code>`django`</code></td><td><code> (string) The main app name to execute. Affects which settings, wsgi, and rootURL to use.</code></td></tr><tr style="" ><td>global.djangoSettingsModule</td><td>string</td><td><code>`django.settings`</code></td><td><code> (string) Django settings module to be used</code></td></tr><tr style="" ><td>global.rootURLConf</td><td>string</td><td><code>`django.urls`</code></td><td><code> (string) Django root URL conf to be used</code></td></tr><tr style="" ><td>global.staticRoot</td><td>path</td><td><code>`/opt/django/static`</code></td><td><code> (path) Location to the static directory</code></td></tr><tr style="" ><td>global.mediaRoot</td><td>path</td><td><code>`/opt/django/media`</code></td><td><code> (path) Location to the media directory</code></td></tr>
</table>


</table>

<h2>image</h2> Image map
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>image</td><td>dict</td><td><code>`{'registry': 'docker.io', 'repository': 'lucernae/django-sample', 'tag': '3.1', 'pullPolicy': 'IfNotPresent'}`</code></td><td><code> Image map</code></td></tr><tr style="" ><td>image.registry</td><td>str</td><td><code>`docker.io`</code></td><td><code> Image registry</code></td></tr><tr style="" ><td>image.repository</td><td>str</td><td><code>`lucernae/django-sample`</code></td><td><code> Image repository</code></td></tr><tr style="" ><td>image.tag</td><td>str</td><td><code>`3.1`</code></td><td><code> Image tag</code></td></tr><tr style="" ><td>image.pullPolicy</td><td>str</td><td><code>`IfNotPresent`</code></td><td><code> Image pullPolicy</code></td></tr>
</table>


</table>

<h2>ingress</h2>
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>ingress</td><td>dict</td><td><code>`{'enabled': False, 'host': '', 'annotations': {}, 'labels': {}, 'tls': {'enabled': False, 'secretName': 'django-tls'}}`</code></td><td></td></tr><tr style="" ><td>ingress.enabled</td><td>bool</td><td><code>`False`</code></td><td><code> (bool) Set to true to generate Ingress resource</code></td></tr><tr style="" ><td>ingress.host</td><td>tpl/string</td><td><code>``</code></td><td><code> (tpl/string) Set custom host name. (DNS name convention)</code></td></tr><tr style="" ><td>ingress.annotations</td><td>dict</td><td><code>`{}`</code></td><td><code> (dict) Custom Ingress annotations</code></td></tr><tr style="" ><td>ingress.labels</td><td>dict</td><td><code>`{}`</code></td><td><code> (dict) Custom Ingress labels</code></td></tr><tr style="" ><td>ingress.tls</td><td>dict</td><td><code>`{'enabled': False, 'secretName': 'django-tls'}`</code></td><td></td></tr><tr style="" ><td>ingress.tls.enabled</td><td>bool</td><td><code>`False`</code></td><td><code> (bool) Set to true to enable HTTPS</code></td></tr><tr style="" ><td>ingress.tls.secretName</td><td>string</td><td><code>`django-tls`</code></td><td><code> (string) You must provide a secret name where the TLS cert is stored</code></td></tr>
</table>


</table>

<h2>labels</h2> (map) The deployment label
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>labels</td><td>map</td><td><code>`{'user/workload': 'true', 'client-name': 'my-boss', 'project-name': 'awesome-project'}`</code></td><td><code> (map) The deployment label</code></td></tr><tr style="" ><td>labels.user/workload</td><td>str</td><td><code>`true`</code></td><td></td></tr><tr style="" ><td>labels.client-name</td><td>str</td><td><code>`my-boss`</code></td><td></td></tr><tr style="" ><td>labels.project-name</td><td>str</td><td><code>`awesome-project`</code></td><td></td></tr>
</table>


</table>

<h2>persistence</h2>
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>persistence</td><td>dict</td><td><code>`{'staticDir': {'enabled': True, 'existingClaim': False, 'mountPath': '/opt/django/static', 'subPath': 'static', 'size': '8Gi', 'accessModes': ['ReadWriteOnce'], 'annotations': {}}, 'mediaDir': {'enabled': True, 'existingClaim': False, 'mountPath': '/opt/django/media', 'subPath': 'media', 'size': '8Gi', 'accessModes': ['ReadWriteOnce'], 'annotations': {}}}`</code></td><td></td></tr><tr style="" ><td>persistence.staticDir</td><td>dict</td><td><code>`{'enabled': True, 'existingClaim': False, 'mountPath': '/opt/django/static', 'subPath': 'static', 'size': '8Gi', 'accessModes': ['ReadWriteOnce'], 'annotations': {}}`</code></td><td></td></tr><tr style="" ><td>persistence.staticDir.enabled</td><td>bool</td><td><code>`True`</code></td><td><code> (bool) Allow persistence</code></td></tr><tr style="" ><td>persistence.staticDir.existingClaim</td><td>bool</td><td><code>`False`</code></td><td></td></tr><tr style="" ><td>persistence.staticDir.mountPath</td><td>str</td><td><code>`/opt/django/static`</code></td><td></td></tr><tr style="" ><td>persistence.staticDir.subPath</td><td>str</td><td><code>`static`</code></td><td></td></tr><tr style="" ><td>persistence.staticDir.size</td><td>str</td><td><code>`8Gi`</code></td><td></td></tr><tr style="" ><td>persistence.staticDir.accessModes</td><td>k8s/storage/persistent-volume/access-modes</td><td><code>`['ReadWriteOnce']`</code></td><td><code> (k8s/storage/persistent-volume/access-modes) Static Dir access modes</code></td></tr><tr style="" ><td>persistence.staticDir.accessModes[0]</td><td>str</td><td><code>`ReadWriteOnce`</code></td><td></td></tr><tr style="" ><td>persistence.staticDir.annotations</td><td>dict</td><td><code>`{}`</code></td><td></td></tr><tr style="" ><td>persistence.mediaDir</td><td>dict</td><td><code>`{'enabled': True, 'existingClaim': False, 'mountPath': '/opt/django/media', 'subPath': 'media', 'size': '8Gi', 'accessModes': ['ReadWriteOnce'], 'annotations': {}}`</code></td><td></td></tr><tr style="" ><td>persistence.mediaDir.enabled</td><td>bool</td><td><code>`True`</code></td><td><code> (bool) Allow persistence</code></td></tr><tr style="" ><td>persistence.mediaDir.existingClaim</td><td>bool</td><td><code>`False`</code></td><td></td></tr><tr style="" ><td>persistence.mediaDir.mountPath</td><td>str</td><td><code>`/opt/django/media`</code></td><td></td></tr><tr style="" ><td>persistence.mediaDir.subPath</td><td>str</td><td><code>`media`</code></td><td></td></tr><tr style="" ><td>persistence.mediaDir.size</td><td>str</td><td><code>`8Gi`</code></td><td></td></tr><tr style="" ><td>persistence.mediaDir.accessModes</td><td>list</td><td><code>`['ReadWriteOnce']`</code></td><td></td></tr><tr style="" ><td>persistence.mediaDir.accessModes[0]</td><td>str</td><td><code>`ReadWriteOnce`</code></td><td></td></tr><tr style="" ><td>persistence.mediaDir.annotations</td><td>dict</td><td><code>`{}`</code></td><td></td></tr>
</table>


</table>

<h2>postgis</h2>
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>postgis</td><td>dict</td><td><code>`{'enabled': True, 'existingSecret': '{{ include "common.sharedSecretName" . \\| quote -}}'}`</code></td><td></td></tr><tr style="" ><td>postgis.enabled</td><td>bool</td><td><code>`True`</code></td><td><code> (bool) Enable postgis as database backend by default. Set to false if using different external backend.</code></td></tr><tr style="" ><td>postgis.existingSecret</td><td>tpl/string</td><td><code>`{{ include "common.sharedSecretName" . \| quote -}}`</code></td><td><code> (tpl/string) Existing secret to be used</code></td></tr>
</table>


</table>

<h2>probe</h2> (tpl/object) Probe can be overridden
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>

</table>


</table>

<h2>sampleYaml</h2>
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>sampleYaml</td><td>dict</td><td><code>`{}`</code></td><td></td></tr>
</table>


</table>

<h2>service</h2>
<table style="">
    <tr>
        <th>Key</th>
        <th>Type</th>
        <th>Default</th>
        <th>Description</th>
    </tr>
<tr style="" ><td>service</td><td>dict</td><td><code>`{'type': 'ClusterIP', 'clusterIP': '', 'externalIPs': '', 'port': 80, 'nodePort': None, 'annotations': {}}`</code></td><td></td></tr><tr style="" ><td>service.type</td><td>string</td><td><code>`ClusterIP`</code></td><td><code> (string) Define k8s service for Django.</code></td></tr><tr style="" ><td>service.clusterIP</td><td>string</td><td><code>``</code></td><td><code> (string) Specify `None` for headless service. Otherwise, leave them be.</code></td></tr><tr style="" ><td>service.externalIPs</td><td>tpl/array</td><td><code>``</code></td><td><code> (tpl/array) Specify for LoadBalancer service type</code></td></tr><tr style="" ><td>service.port</td><td>int</td><td><code>`80`</code></td><td><code> (int) Specify service port</code></td></tr><tr style="" ><td>service.nodePort</td><td>int</td><td><code>`None`</code></td><td><code> (int) Specify node port, for NodePort service type</code></td></tr><tr style="" ><td>service.annotations</td><td>dict</td><td><code>`{}`</code></td><td><code> (dict) Extra service annotations</code></td></tr>
</table>


</table>


</table>



Autogenerated from chart metadata using [doxy-helm v1.0.1](https://github.com/tactful-ai/doxyhelm)
    