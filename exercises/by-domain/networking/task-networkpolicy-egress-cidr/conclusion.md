# Task: NetworkPolicy - Egress to CIDR Range

## Objective
Allow egress traffic from frontend namespace to a specific IP address range.

## Requirements
- Namespace: "frontend"
- Allow egress traffic to IP range 10.20.30.0/24

## Solution

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: frontend-egress-cidr
  namespace: frontend
spec:
  podSelector: {}  # Apply to all pods in namespace
  policyTypes:
  - Egress
  egress:
  - to:
    - ipBlock:
        cidr: 10.20.30.0/24
    ports:
    - protocol: TCP
      port: 443  # HTTPS
    - protocol: TCP
      port: 80   # HTTP
```

## Key Concepts
- **Egress**: Outgoing traffic rules
- **ipBlock**: CIDR block for IP address ranges
- **cidr**: IP address range in CIDR notation
- **Empty podSelector**: Applies to all pods in namespace

## Allow All Egress to CIDR
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: frontend-egress-cidr
  namespace: frontend
spec:
  podSelector: {}
  policyTypes:
  - Egress
  egress:
  - to:
    - ipBlock:
        cidr: 10.20.30.0/24
    # No ports = all ports allowed
```

## Exclude IPs from CIDR Block
```yaml
egress:
- to:
  - ipBlock:
      cidr: 10.20.30.0/24
      except:
      - 10.20.30.1  # Exclude specific IP
      - 10.20.30.2
```

## Verification
```bash
# Create NetworkPolicy
kubectl apply -f frontend-egress-cidr.yaml

# Check NetworkPolicy
kubectl get netpol -n frontend

# Test egress connectivity
kubectl run test-pod -n frontend --image=nicolaka/netshoot --rm -it -- \
  curl 10.20.30.10
```

## Common Use Cases
- Allow access to external APIs
- Restrict access to specific data centers
- Control outbound internet access
- Isolate network segments
