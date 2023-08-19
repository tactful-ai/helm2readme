- after any configmap you should left a space
```yaml
# -- (tpl/dict) Define this for extra config map to be included in django-shared-config
# @notationType -- tpl
extraConfigMap: |
# file_1: conf content

# -- (tpl/array) Define this for extra volume mounts in the pod
# @notationType -- tpl
extraVolumeMounts: |
# You may potentially mount a config map/secret
#  - name: custom-config
#    mountPath: /docker-entrypoint.sh
#    subPath: docker-entrypoint.sh
#    readOnly: true

```





- if you want to separate sone key and all its child you should use `-- [table]` before the key
```yaml
# -- [table]
controller2:
# -- [waer] ksjdkjskdjsk
  name: controller
  image:
    repository: nginx-ingress-controller
    tag: "18.0831"
```


- if you want to add custom css for specific table you can write '-- {css code}' before the table this is also valid for key that will be rows
```yaml
# -- {color:red}
controller2:
# -- [waer] ksjdkjskdjsk
  name: controller
  image:
    repository: nginx-ingress-controller
    tag: "18.0831"
```


- if you want to add global css for all tables you can write '-- @global {css code}' at start of the file
```yaml
# -- @global {color:red}
controller2:
# -- [waer] ksjdkjskdjsk
  name: controller
  image:
    repository: nginx-ingress-controller
    tag: "18.0831"
```


- if you want to add global css for all tables you can write '-- @[] {css code}' at start of the file
```yaml
# -- @global {color:red}
controller2:
# -- [waer] ksjdkjskdjsk
  name: controller
  image:
    repository: nginx-ingress-controller
    tag: "18.0831"
```



- render direct markdown inside the description





- testing -> Done
- documentation
- github pipeline
- package the applincatio by byinstaller
