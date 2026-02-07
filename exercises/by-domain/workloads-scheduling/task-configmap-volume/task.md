# Task: Mount ConfigMap as Volume

## Objective
Mount ConfigMap as a volume in a pod.

## Solution

### Create ConfigMap
```bash
kubectl create configmap cmvolume --from-literal=var8=val8 --from-literal=var9=val9
```

### Create Pod with ConfigMap Volume
```bash
kubectl run nginx --image=nginx --restart=Never --dry-run=client -o yaml > pod.yaml
```

Edit pod.yaml:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  volumes:  # add volumes list
  - name: myvolume  # volume name
    configMap:
      name: cmvolume  # name of your configmap
  containers:
  - image: nginx
    name: nginx
    volumeMounts:  # volume mounts
    - name: myvolume  # reference to volume name
      mountPath: /etc/lala  # path inside container
```

### Create and Verify
```bash
kubectl create -f pod.yaml
kubectl exec -it nginx -- /bin/sh
cd /etc/lala
ls  # will show var8 var9
cat var8  # will show val8
cat var9  # will show val9
exit
```

## Key Concepts
- **volumes**: Define volumes at pod level
- **volumeMounts**: Mount volumes in containers
- **configMap**: Volume type for ConfigMap
- **mountPath**: Path where ConfigMap is mounted
- Each key becomes a file in the mount path

## Verification
```bash
# Check volume mount
kubectl exec nginx -- ls -la /etc/lala

# Read ConfigMap values
kubectl exec nginx -- cat /etc/lala/var8
kubectl exec nginx -- cat /etc/lala/var9

# Describe pod to see volume configuration
kubectl describe pod nginx
```

## Use Cases
- Configuration files for applications
- Static configuration data
- Non-sensitive configuration
- Application settings
