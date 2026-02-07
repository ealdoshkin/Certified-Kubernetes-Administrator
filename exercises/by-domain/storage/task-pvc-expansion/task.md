# Task: Expand PersistentVolumeClaim

## Objective
Create a PVC, mount it in a pod, and then expand the PVC capacity.

## Requirements
- PVC name: `pv-volume`
- Storage class: `csi-hostpath-sc`
- Initial capacity: 10 Mi
- Expanded capacity: 70 Mi
- Pod name: `web-server`
- Image: `nginx`
- Mount path: `/usr/share/nginx/html`
- Access mode: ReadWriteOnce

## Solution

### Step 1: Create PVC
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pv-volume
spec:
  accessModes:
    - ReadWriteOnce
  volumeMode: Filesystem
  resources:
    requests:
      storage: 10Mi
  storageClassName: csi-hostpath-sc
```

```bash
kubectl apply -f pvc.yaml
```

### Step 2: Create Pod with PVC
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: web-server
spec:
  containers:
  - name: web-server
    image: nginx
    volumeMounts:
    - mountPath: "/usr/share/nginx/html"
      name: my-volume
  volumes:
  - name: my-volume
    persistentVolumeClaim:
      claimName: pv-volume
```

```bash
kubectl apply -f pod.yaml
```

### Step 3: Expand PVC
```bash
# Method 1: Using kubectl edit
kubectl edit pvc pv-volume
# Change storage: 10Mi to storage: 70Mi

# Method 2: Using kubectl patch
kubectl patch pvc pv-volume -p '{"spec":{"resources":{"requests":{"storage":"70Mi"}}}}'

# Method 3: Using YAML
kubectl get pvc pv-volume -o yaml > pvc-expanded.yaml
# Edit storage: 10Mi to storage: 70Mi
kubectl apply -f pvc-expanded.yaml
```

## Key Concepts
- **PVC Expansion**: Increase PVC size after creation
- **Storage Class**: Must support volume expansion
- **Volume Expansion**: Requires storage class with allowVolumeExpansion: true
- **Online Expansion**: Some storage classes support online expansion

## Prerequisites
- Storage class must support expansion
- Storage class should have `allowVolumeExpansion: true`

## Verification
```bash
# Check PVC capacity
kubectl get pvc pv-volume

# Describe PVC to see expansion status
kubectl describe pvc pv-volume

# Check pod can still access volume
kubectl exec web-server -- df -h /usr/share/nginx/html
```

## Important Notes
- Not all storage classes support expansion
- Expansion may require pod restart
- Some storage classes support online expansion
- Expansion is one-way (can't shrink)
