# Solution for Task 7: Create PersistentVolumeClaim

1. Create a file named `app-data-pvc.yaml` with the following content:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: app-data
spec:
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 2Gi
  storageClassName: shared
```

2. Then apply the configuration:

```bash
# 1. Create PVC
kubectl apply -f app-data-pvc.yaml

# 2. Check PVC status
kubectl get pvc app-data

# 3. Check PV status (should be Bound)
kubectl get pv app-data
```
