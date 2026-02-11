# Solution for Task 6: Create Persistent Volume

1. First, create a file named `app-data-pv.yaml` with the following content:

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: app-data
spec:
  capacity:
    storage: 2Gi
  accessModes:
    - ReadWriteMany
  storageClassName: shared
  hostPath:
    path: /srv/app-data
```

2. Then apply the configuration:

```bash
# 1. Create the PV
kubectl apply -f app-data-pv.yaml

# 2. Verify
kubectl get pv app-data
```
