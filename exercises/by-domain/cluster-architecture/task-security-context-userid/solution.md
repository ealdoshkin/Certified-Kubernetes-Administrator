# Task: Security Context - User ID Configuration

## Objective
Deploy a Pod with multiple containers and configure user IDs at pod and container levels.

## Requirements
- Pod name: 'user-id'
- Containers: 'sec-ctx-demo-2' and 'second-container'
- Image for 'sec-ctx-demo-2': 'gcr.io/google-samples/node-hello:1.0'
- Pod-level runAsUser: '1000'
- Container 'sec-ctx-demo-2' runAsUser: '2000' (overrides pod-level)
- Container 'sec-ctx-demo-2' should not allow privilege escalation

## Solution

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: user-id
spec:
  securityContext:
    runAsUser: 1000  # Pod-level user ID
  containers:
  - name: sec-ctx-demo-2
    image: gcr.io/google-samples/node-hello:1.0
    securityContext:
      runAsUser: 2000  # Container-level overrides pod-level
      allowPrivilegeEscalation: false
  - name: second-container
    image: busybox
    # Uses pod-level runAsUser: 1000
```

## Key Concepts
- **Pod Security Context**: Applies to all containers in pod
- **Container Security Context**: Overrides pod-level settings
- **runAsUser**: User ID to run container as
- **allowPrivilegeEscalation**: Prevents gaining additional privileges
- **Inheritance**: Container inherits pod settings unless overridden

## Security Context Fields
- **runAsUser**: User ID
- **runAsGroup**: Group ID
- **runAsNonRoot**: Must run as non-root user
- **allowPrivilegeEscalation**: Prevent privilege escalation
- **readOnlyRootFilesystem**: Mount root filesystem as read-only
- **capabilities**: Linux capabilities

## Verification
```bash
# Create pod
kubectl apply -f pod.yaml

# Check pod status
kubectl get pod user-id

# Verify security context
kubectl get pod user-id -o yaml | grep -A 15 securityContext

# Check user ID in container
kubectl exec user-id -c sec-ctx-demo-2 -- id
kubectl exec user-id -c second-container -- id
```

## Best Practices
- Use non-root users when possible
- Set allowPrivilegeEscalation: false
- Use specific user IDs instead of root (0)
- Document security context requirements
