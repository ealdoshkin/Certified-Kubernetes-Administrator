To create the pv from the manifest file

`$ kubectl create -f pv.yml`

To cross check

`$ kubectl get pv`


```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: my-vol
spec:
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: /test/path
```
