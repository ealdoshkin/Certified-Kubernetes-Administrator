# Task: NetworkPolicy - App to Database on Specific Port

## Objective
Allow ingress traffic from app namespace to db namespace pods, but only on port 3306 (MySQL).

## Requirements
- "app" namespace contains frontend pods
- "db" namespace contains database pods
- Allow ingress traffic from app pods to db pods only on port 3306

## Solution

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: app-db-policy
  namespace: db
spec:
  podSelector:
    matchLabels:
      app: database
  policyTypes:
  - Ingress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          name: app
      podSelector:
        matchLabels:
          app: frontend
    ports:
    - protocol: TCP
      port: 3306
```

## Key Concepts
- **Port Restriction**: Only allow specific port
- **Namespace + Pod Selector**: Combine namespace and pod selectors
- **Database Port**: 3306 is MySQL default port
- **Selective Access**: Limit access to specific port only

## Alternative: All Pods from App Namespace
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: app-db-policy
  namespace: db
spec:
  podSelector:
    matchLabels:
      app: database
  policyTypes:
  - Ingress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          name: app
    ports:
    - protocol: TCP
      port: 3306
```

## Verification
```bash
# Create NetworkPolicy
kubectl apply -f app-db-policy.yaml

# Check NetworkPolicy
kubectl get netpol -n db

# Test connectivity on port 3306 (should work)
kubectl run test-pod -n app --image=nicolaka/netshoot --rm -it -- \
  nc -zv database-service.db 3306

# Test connectivity on other port (should fail)
kubectl run test-pod -n app --image=nicolaka/netshoot --rm -it -- \
  nc -zv database-service.db 8080
```

## Best Practices
- Restrict to specific ports for databases
- Use namespace labels for organization
- Document allowed connections
- Test network policies thoroughly
