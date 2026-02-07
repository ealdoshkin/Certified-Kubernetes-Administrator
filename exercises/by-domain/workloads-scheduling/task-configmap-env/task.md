# Task: Use ConfigMap as Environment Variables

## Objective
Load ConfigMap values as environment variables in pods.

## Task 1: Single Key as Environment Variable

### Create ConfigMap
```bash
kubectl create cm options --from-literal=var5=val5
```

### Create Pod with ConfigMap Key as Env Var
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
  containers:
  - image: nginx
    name: nginx
    env:
    - name: option  # name of the env variable
      valueFrom:
        configMapKeyRef:
          name: options  # name of config map
          key: var5      # name of the key in config map
```

```bash
kubectl create -f pod.yaml
kubectl exec -it nginx -- env | grep option  # will show 'option=val5'
```

## Task 2: All Keys as Environment Variables

### Create ConfigMap
```bash
kubectl create configmap anotherone --from-literal=var6=val6 --from-literal=var7=val7
```

### Create Pod with All ConfigMap Keys
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
  containers:
  - image: nginx
    name: nginx
    envFrom:  # different from 'env'
    - configMapRef:  # different from 'configMapKeyRef'
        name: anotherone  # name of the config map
```

```bash
kubectl create -f pod.yaml
kubectl exec -it nginx -- env  # will show var6 and var7
```

## Key Concepts
- **env**: Single environment variable from ConfigMap key
- **envFrom**: All keys from ConfigMap as environment variables
- **configMapKeyRef**: Reference specific key
- **configMapRef**: Reference entire ConfigMap

## Verification
```bash
# Check environment variables
kubectl exec nginx -- env | grep -E "option|var6|var7"

# Describe pod to see env configuration
kubectl describe pod nginx
```
