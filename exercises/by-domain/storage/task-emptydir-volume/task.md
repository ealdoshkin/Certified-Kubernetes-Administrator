# Task: emptyDir Volume

## Objective
Create a pod with multiple containers sharing an emptyDir volume.

## Solution

### Create Pod with emptyDir Volume
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
  - name: busybox2
    image: busybox
    command: ["/bin/sh", "-c", "sleep 3600"]
    volumeMounts:
    - name: myvolume
      mountPath: /etc/foo
  volumes:
  - name: myvolume
    emptyDir: {}
```

### Create and Test
```bash
kubectl apply -f pod.yaml

# Connect to second container and write file
kubectl exec -it busybox -c busybox2 -- /bin/sh
cat /etc/passwd | cut -f 1 -d ':' > /etc/foo/passwd
cat /etc/foo/passwd
exit

# Connect to first container and read file
kubectl exec -it busybox -c busybox -- /bin/sh
mount | grep foo
cat /etc/foo/passwd
exit

# Cleanup
kubectl delete pod busybox
```

## Key Concepts
- **emptyDir**: Temporary storage shared between containers
- **Volume Mount**: Mount volume in container
- **Shared Storage**: Multiple containers can access same volume
- **Temporary**: Data lost when pod is deleted

## emptyDir Medium Types
```yaml
volumes:
- name: myvolume
  emptyDir:
    medium: Memory  # Use tmpfs (RAM)
    sizeLimit: 1Gi  # Optional size limit
```

## Use Cases
- Shared cache between containers
- Temporary file storage
- Inter-container communication
- Scratch space

## Verification
```bash
# Check volume mount
kubectl exec busybox -c busybox -- mount | grep foo

# List files in volume
kubectl exec busybox -c busybox -- ls -la /etc/foo

# Verify shared access
kubectl exec busybox -c busybox2 -- ls -la /etc/foo
```
