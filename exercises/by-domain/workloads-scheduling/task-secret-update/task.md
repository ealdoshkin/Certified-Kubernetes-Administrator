# Task: Update Existing Secret

## Objective
Update an existing Kubernetes Secret and ensure changes propagate to running Pods without redeployment.

## Requirements
- Existing Secret named 'database-creds' with username and password
- Update password in the Secret
- Changes should propagate to running Pods without redeployment

## Solution

### Method 1: Update Secret (Pods need restart)
```bash
# Create updated secret YAML
kubectl create secret generic database-creds \
  --from-literal=username=dbuser \
  --from-literal=password=newpassword \
  --dry-run=client -o yaml > updated-secret.yaml

# Apply the changes
kubectl apply -f updated-secret.yaml

# Restart pods to pick up new secret (if using env vars)
kubectl rollout restart deployment <deployment-name>
```

### Method 2: Patch Secret
```bash
# Encode new password
echo -n "newpassword" | base64

# Patch secret
kubectl patch secret database-creds -p '{"data":{"password":"<base64-encoded-password>"}}'
```

## Important Notes
- **Environment Variables**: Pods using secrets as env vars need restart
- **Volume Mounts**: Pods using secrets as volumes automatically update
- **No Automatic Propagation**: Secrets don't automatically update in running pods

## Solution for Automatic Updates

### Using Volume Mounts (Auto-updates)
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  template:
    spec:
      containers:
      - name: app
        image: nginx
        volumeMounts:
        - name: secret-volume
          mountPath: /etc/secrets
      volumes:
      - name: secret-volume
        secret:
          secretName: database-creds
```

### Using Init Container to Reload
```yaml
spec:
  initContainers:
  - name: reload-secrets
    image: busybox
    command: ["sh", "-c", "kill -HUP 1"]
  containers:
  - name: app
    image: my-app
    env:
    - name: PASSWORD
      valueFrom:
        secretKeyRef:
          name: database-creds
          key: password
```

## Verification
```bash
# Check secret updated
kubectl get secret database-creds -o yaml

# Decode password to verify
kubectl get secret database-creds -o jsonpath='{.data.password}' | base64 -d

# Check if pods need restart
kubectl get pods

# Restart deployment if needed
kubectl rollout restart deployment <deployment-name>
```

## Best Practices
- Use volume mounts for secrets that need auto-updates
- Document secret update procedures
- Test secret updates in non-production first
- Consider using external secret management for automatic sync
