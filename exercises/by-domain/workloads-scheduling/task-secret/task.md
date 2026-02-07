# Task: Create Secrets

## Objective
Create secrets with base64 encoded values.

## Steps

### 1. Encode Values
```bash
# Create base64 encoded strings
echo -n 'secret' | base64
# Output: c2VjcmV0

echo -n 'anothersecret' | base64
# Output: YW5vdGhlcnNlY3JldA==
```

### 2. Create Secret YAML
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: my-secret
type: Opaque
data:
  secretkey1: c2VjcmV0  # base64 encoded 'secret'
  secretkey2: YW5vdGhlcnNlY3JldA==  # base64 encoded 'anothersecret'
```

### 3. Apply Secret
```bash
# Create the secret
kubectl create -f secret.yaml

# Verify
kubectl get secret my-secret
kubectl describe secret my-secret
```

## Alternative: Create Secret from Command Line
```bash
# Create secret from literal values (automatically base64 encoded)
kubectl create secret generic my-secret \
  --from-literal=secretkey1=secret \
  --from-literal=secretkey2=anothersecret

# Create secret from file
kubectl create secret generic my-secret \
  --from-file=secretkey1=./file1.txt \
  --from-file=secretkey2=./file2.txt
```

## Decode Secret Values
```bash
# View secret (base64 encoded)
kubectl get secret my-secret -o yaml

# Decode a specific key
kubectl get secret my-secret -o jsonpath='{.data.secretkey1}' | base64 -d
```

## Key Concepts
- **Secret**: Store sensitive data (passwords, tokens, keys)
- **Opaque**: Default secret type for arbitrary user data
- **Base64 Encoding**: Secrets are base64 encoded (not encrypted)
- **Type**: Different secret types (Opaque, kubernetes.io/tls, etc.)

## Security Notes
- Secrets are base64 encoded, not encrypted
- Use RBAC to restrict secret access
- Consider using external secret management for production
- Never commit secrets to version control
