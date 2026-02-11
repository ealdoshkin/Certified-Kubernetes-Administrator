# Task: NetworkPolicy - Allow All Traffic in Namespace

## Objective
Create a NetworkPolicy that allows all inbound and outbound traffic within a specific namespace.

## Requirements
- Namespace: "internal"
- Allow all inbound and outbound traffic within the namespace

## Solution

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-all-policy
  namespace: internal
spec:
  podSelector: {}  # Apply to all pods
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - {}  # Allow all ingress
  egress:
  - {}  # Allow all egress
```

## Key Concepts
- **Empty podSelector**: Applies to all pods in namespace
- **Empty ingress/egress rules**: Allow all traffic
- **Allow All**: Permissive policy (opposite of default deny)
- **Namespace Isolation**: Can still restrict cross-namespace traffic

## Alternative: Explicit Allow All
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-all-policy
  namespace: internal
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from: []  # Allow from anywhere
    ports: [] # Allow all ports
  egress:
  - to: []    # Allow to anywhere
    ports: [] # Allow all ports
```

## Use Cases
- Development environments
- Trusted namespaces
- When default deny is too restrictive
- Testing and debugging

## Verification
```bash
# Create NetworkPolicy
kubectl apply -f allow-all-policy.yaml

# Check NetworkPolicy
kubectl get netpol -n internal

# Test connectivity (should work)
kubectl run test-pod1 -n internal --image=nginx
kubectl run test-pod2 -n internal --image=nicolaka/netshoot --rm -it -- \
  curl test-pod1
```

## Important Notes
- This is a permissive policy (allows everything)
- Use with caution in production
- Consider more restrictive policies
- Can be used to override default deny policies
