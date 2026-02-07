# Task: PersistentVolume and PersistentVolumeClaim

## Objective
Create PersistentVolume and PersistentVolumeClaim, and mount in a pod.

## Solution

### Step 1: Create PersistentVolume
```bash
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: PersistentVolume
metadata:
  name: myvolume
spec:
  storageClassName: normal
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
    - ReadWriteMany
  hostPath:
    path: /etc/foo
EOF
```

### Step 2: Verify PersistentVolume
```bash
# List PersistentVolumes
kubectl get pv

# Describe PersistentVolume
kubectl describe pv myvolume
```

### Step 3: Create PersistentVolumeClaim
```bash
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mypvc
spec:
  storageClassName: normal
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 4Gi
EOF
```

### Step 4: Verify Binding
```bash
# Check PVC status (should be Bound)
kubectl get pvc

# Check PV status (should be Bound)
kubectl get pv

# Describe binding
kubectl describe pvc mypvc
```

### Step 5: Create Pod with PVC
```bash
kubectl run busybox --image=busybox --restart=Never -o yaml --dry-run=client -- /bin/sh -c 'sleep 3600' > pod.yaml
```

Edit pod.yaml:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: busybox
spec:
  containers:
  - name: busybox
    image: busybox
    command: ["/bin/sh", "-c", "sleep 3600"]
    volumeMounts:
    - name: myvolume
      mountPath: /etc/foo
  volumes:
  - name: myvolume
    persistentVolumeClaim:
      claimName: mypvc
```

### Step 6: Test Persistent Storage
```bash
# Create pod
kubectl apply -f pod.yaml

# Write data
kubectl exec busybox -- cp /etc/passwd /etc/foo/passwd

# Verify data
kubectl exec busybox -- ls -la /etc/foo
kubectl exec busybox -- cat /etc/foo/passwd
```

## Key Concepts
- **PersistentVolume (PV)**: Cluster resource for storage
- **PersistentVolumeClaim (PVC)**: Request for storage
- **Binding**: PVC binds to matching PV
- **storageClassName**: Groups PVs by storage class
- **accessModes**: ReadWriteOnce, ReadWriteMany, ReadOnlyMany

## Access Modes
- **ReadWriteOnce (RWO)**: Single node read-write
- **ReadWriteMany (RWX)**: Multiple nodes read-write
- **ReadOnlyMany (ROX)**: Multiple nodes read-only

## Storage Classes
- **normal**: Standard storage class
- **fast**: Fast storage (SSD)
- **slow**: Slow storage (HDD)

## Verification
```bash
# Check PVs
kubectl get pv

# Check PVCs
kubectl get pvc

# Check pod
kubectl get pod busybox

# Verify mount
kubectl exec busybox -- mount | grep foo
```

## Cleanup
```bash
# Delete pod
kubectl delete pod busybox

# Delete PVC (PV becomes Released)
kubectl delete pvc mypvc

# Delete PV
kubectl delete pv myvolume
```

## Important Notes
- PVC must match PV in:
  - storageClassName
  - accessModes
  - storage size (PVC request <= PV capacity)
- hostPath volumes are node-specific
- For multi-node clusters, use network storage (NFS, etc.)
