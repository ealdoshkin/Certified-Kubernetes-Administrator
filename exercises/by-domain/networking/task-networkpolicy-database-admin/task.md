# Task: NetworkPolicy - Restrict Database Access to Admin Pod

## Objective
Restrict all inbound traffic to database pods except from a specific admin pod.

## Requirements
- Namespace: "data"
- Database pods running in "data" namespace
- Restrict all inbound traffic except from pod named "admin"

## Solution

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: database-admin-policy
  namespace: data
spec:
  podSelector:
    matchLabels:
      app: database
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          name: admin
    ports:
    - protocol: TCP
      port: 3306  # MySQL default port
```

## Key Concepts
- **Default Deny**: NetworkPolicy with only ingress rules denies all other traffic
- **podSelector**: Select specific pods by labels
- **Restrictive Policy**: Only allow specific source pods
- **Database Security**: Protect sensitive database pods

## Verification
```bash
# Create NetworkPolicy
kubectl apply -f database-admin-policy.yaml

# Check NetworkPolicy
kubectl get netpol -n data

# Test from admin pod (should work)
kubectl exec -it admin-pod -n data -- curl database-service:3306

# Test from other pod (should fail)
kubectl run test-pod -n data --image=nicolaka/netshoot --rm -it -- curl database-service:3306
```

## Alternative: Allow All Ports from Admin
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: database-admin-policy
  namespace: data
spec:
  podSelector:
    matchLabels:
      app: database
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          name: admin
    # No ports specified = all ports allowed
```

## Best Practices
- Use labels consistently for pod selection
- Document which pods can access databases
- Test network policies before production
- Consider egress policies for additional security
