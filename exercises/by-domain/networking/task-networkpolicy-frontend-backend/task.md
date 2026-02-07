# Task: NetworkPolicy - Frontend to Backend Communication

## Objective
Allow ingress traffic from frontend pods to backend pods on port 8080 across namespaces.

## Requirements
- "frontend" namespace contains frontend pods
- "backend" namespace contains backend pods
- Allow ingress traffic from frontend pods to backend pods on port 8080

## Solution

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: frontend-backend-policy
  namespace: backend
spec:
  podSelector:
    matchLabels:
      app: backend
  policyTypes:
  - Ingress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          name: frontend
    ports:
    - protocol: TCP
      port: 8080
```

## Key Concepts
- **NetworkPolicy**: Controls network traffic to/from pods
- **Ingress**: Incoming traffic rules
- **namespaceSelector**: Select pods from specific namespace
- **podSelector**: Select pods within namespace
- **Port**: Specific port for traffic

## Verification
```bash
# Create NetworkPolicy
kubectl apply -f frontend-backend-policy.yaml

# Check NetworkPolicy
kubectl get netpol -n backend

# Describe NetworkPolicy
kubectl describe netpol frontend-backend-policy -n backend

# Test connectivity
kubectl run test-pod -n frontend --image=nicolaka/netshoot --rm -it -- curl backend-service.backend:8080
```

## Alternative: Using podSelector
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: frontend-backend-policy
  namespace: backend
spec:
  podSelector:
    matchLabels:
      app: backend
  policyTypes:
  - Ingress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          name: frontend
      podSelector:
        matchLabels:
          app: frontend
    ports:
    - protocol: TCP
      port: 8080
```
