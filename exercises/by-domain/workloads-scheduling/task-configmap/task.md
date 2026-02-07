# Task: Create and Use ConfigMaps

## Objective
Create ConfigMaps and use them in deployments as volumes and environment variables.

## Task 1: Create ConfigMap with Single and Multi-line Values

```bash
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-configmap
data:
  single: "This is a single line value"
  multi: |
    This is a multi-line value.
    It spans multiple lines.
    You can include as many lines as needed.
EOF

# View the configmap
kubectl describe cm my-configmap
```

## Task 2: Use ConfigMap as Volume

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-nginx-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        volumeMounts:
        - name: config-volume
          mountPath: /etc/config
          readOnly: true
      volumes:
      - name: config-volume
        configMap:
          name: my-configmap
```

## Task 3: Use ConfigMap as Environment Variables

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mynginx-deploy
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        env:
        - name: SINGLE_VALUE
          valueFrom:
            configMapKeyRef:
              name: my-configmap
              key: single
        - name: MULTI_VALUE
          valueFrom:
            configMapKeyRef:
              name: my-configmap
              key: multi
```

## Key Concepts
- **ConfigMap**: Store non-sensitive configuration data
- **Volume Mount**: Mount ConfigMap as files in container
- **Environment Variables**: Inject ConfigMap values as env vars
- **readOnly**: ConfigMap volumes are read-only by default

## Verification
```bash
# Check ConfigMap
kubectl get configmap my-configmap

# View ConfigMap data
kubectl get configmap my-configmap -o yaml

# Check if mounted in pod
kubectl exec <pod-name> -- ls /etc/config

# Check environment variables
kubectl exec <pod-name> -- env | grep VALUE
```
