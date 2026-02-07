# Task: Image Security - Private Registry Authentication

## Objective
Create a secret to authenticate with a private Docker registry and use it in pods.

## Solution

### Create Docker Registry Secret
```bash
# Create secret for private registry
kubectl create secret docker-registry regcred \
  --docker-server=${SERVER_URL} \
  --docker-username=${REGISTRY_USERNAME} \
  --docker-password=${REGISTRY_PASSWORD} \
  --docker-email=${REGISTRY_EMAIL}

# Example:
kubectl create secret docker-registry regcred \
  --docker-server=registry.example.com \
  --docker-username=myuser \
  --docker-password=mypassword \
  --docker-email=myuser@example.com
```

### Use Secret in Pod
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: private-reg-pod
spec:
  containers:
  - name: app
    image: registry.example.com/myapp:latest
  imagePullSecrets:
  - name: regcred
```

### Use Secret in Deployment
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-deployment
spec:
  template:
    spec:
      imagePullSecrets:
      - name: regcred
      containers:
      - name: app
        image: registry.example.com/myapp:latest
```

## Key Concepts
- **imagePullSecrets**: Secret used to authenticate with private registry
- **docker-registry secret type**: Special secret type for registry authentication
- **Private Registry**: Docker registry requiring authentication
- **Image Pull**: Kubernetes uses secret to pull images from private registry

## Verification
```bash
# Check secret exists
kubectl get secret regcred

# Describe secret (won't show password)
kubectl describe secret regcred

# Test pod creation with private image
kubectl run test-pod --image=registry.example.com/private-image:latest --image-pull-secret=regcred
```

## Common Issues
- **ImagePullBackOff**: Wrong credentials or secret not referenced
- **Unauthorized**: Invalid username/password
- **Secret not found**: Secret name doesn't match imagePullSecrets

## Best Practices
- Use separate secrets for different registries
- Rotate credentials regularly
- Use service accounts with imagePullSecrets for automatic mounting
- Store secrets securely (consider external secret management)
