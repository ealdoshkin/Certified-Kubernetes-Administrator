```
$ kubectl create -f pvc.yml

$ kubectl create -f pod.yml

$ kubectl delete pod my-nginx-pod --grace-period=0 --force

$ kubectl patch pvc pvc-q1 -p '{ "spec": { "resources": { "requests": { "storage": "70Mi" }}}}'

(or)

$ kubectl edit pvc.yaml

--> Update the storage size

$ kubectl create -f my-nginx.yaml

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
spec:
  volumes:
    - name: task-pv-storage
      persistentVolumeClaim:
        claimName: my-pvc
  containers:
    - name: my-nginx-pod
      image: nginx
      volumeMounts:
        - mountPath: "usr/share/html"
          name: task-pv-storageapiVersion: v1

```

```yaml
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  storageClassName: k8s-csi-plugin
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 10Gi
```
