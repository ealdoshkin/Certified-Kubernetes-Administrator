# Task: Multi-Container Pod with Secret Volumes

## Objective
Create a Kubernetes Secret and a Pod with multiple containers that use the secret in different ways.

## Requirements
- Secret named 'app-secrets' storing API key and password
- Pod named 'app-pod' with two containers:
  - 'web-app': Uses environment variables from secret
  - 'secrets-init': Mounts secret as volumes and copies to /secrets directory

## Solution

### Step 1: Create Secret
```bash
# Create secret
kubectl create secret generic app-secrets \
  --from-literal=api-key=my-api-key-123 \
  --from-literal=password=my-password-456
```

### Step 2: Create Pod with Secret
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-pod
spec:
  containers:
  - name: web-app
    image: nginx
    env:
    - name: API_KEY
      valueFrom:
        secretKeyRef:
          name: app-secrets
          key: api-key
    - name: PASSWORD
      valueFrom:
        secretKeyRef:
          name: app-secrets
          key: password
  - name: secrets-init
    image: busybox
    command: ["sh", "-c", "cp /secrets/api-key /secrets/password /secrets/ && sleep 3600"]
    volumeMounts:
    - name: secret-volume
      mountPath: /secrets
      readOnly: true
  volumes:
  - name: secret-volume
    secret:
      secretName: app-secrets
```

## Key Concepts
- **Multi-Container Pod**: Pod with multiple containers sharing volumes
- **Secret as Volume**: Mount secret as files in container
- **Secret as Env Var**: Inject secret as environment variables
- **Volume Sharing**: Containers in same pod can share volumes

## Alternative: Using envFrom
```yaml
spec:
  containers:
  - name: web-app
    image: nginx
    envFrom:
    - secretRef:
        name: app-secrets
```

## Verification
```bash
# Check secret
kubectl get secret app-secrets

# Check pod
kubectl get pod app-pod

# Verify environment variables in web-app
kubectl exec app-pod -c web-app -- env | grep -E "API_KEY|PASSWORD"

# Verify files in secrets-init
kubectl exec app-pod -c secrets-init -- ls -la /secrets
kubectl exec app-pod -c secrets-init -- cat /secrets/api-key
```

## Secret Commands
```bash
# Create secret from literals
kubectl create secret generic db-secret \
  --from-literal=DB_Host=sql01 \
  --from-literal=DB_User=root \
  --from-literal=DB_Password=password123

# Get secret YAML
kubectl create secret generic db-secret \
  --from-literal=DB_Host=sql01 \
  --dry-run=client -o yaml
```
