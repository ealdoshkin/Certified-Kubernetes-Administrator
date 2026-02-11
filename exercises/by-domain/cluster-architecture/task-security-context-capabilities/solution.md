# Task: Security Context - Linux Capabilities

## Objective
Deploy a Pod with security context that grants specific Linux capabilities.

## Requirements
- Pod name: 'user-id'
- Container name: 'sec-ctx-demo-2'
- Image: 'gcr.io/google-samples/node-hello:1.0'
- Run container with user ID '1000'
- Grant capabilities for:
  - Manipulating system time (SYS_TIME)
  - Network administration (NET_ADMIN)

## Solution

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: user-id
spec:
  securityContext:
    runAsUser: 1000
  containers:
  - name: sec-ctx-demo-2
    image: gcr.io/google-samples/node-hello:1.0
    securityContext:
      capabilities:
        add:
        - SYS_TIME
        - NET_ADMIN
```

## Key Concepts
- **Security Context**: Security settings for pod or container
- **runAsUser**: User ID to run container as
- **Capabilities**: Linux capabilities to grant to container
- **SYS_TIME**: Capability to set system time
- **NET_ADMIN**: Capability for network administration

## Common Capabilities
- **NET_ADMIN**: Network administration
- **SYS_TIME**: System time manipulation
- **SYS_ADMIN**: System administration
- **CHOWN**: Change file ownership
- **DAC_OVERRIDE**: Override file permissions

## Verification
```bash
# Create pod
kubectl apply -f pod.yaml

# Check pod is running
kubectl get pod user-id

# Verify security context
kubectl get pod user-id -o yaml | grep -A 10 securityContext

# Test capabilities (exec into pod)
kubectl exec -it user-id -- sh
# Inside pod, test capabilities
```

## Best Practices
- Grant minimum required capabilities
- Use specific capabilities instead of ALL
- Avoid running as root when possible
- Document why capabilities are needed
