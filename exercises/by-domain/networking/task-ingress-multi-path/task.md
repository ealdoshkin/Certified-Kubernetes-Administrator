# Task: Create Ingress with Multiple Paths and Hosts

## Objective
Configure Ingress resources to route traffic for multiple web applications using different paths and domains.

## Requirements
- Service "app-a" accessible at path "/appA" on domain "app-a.example.com"
- Service "app-b" accessible at path "/appB" on domain "app-b.example.com"

## Solution

### Option 1: Separate Ingress Resources
```yaml
# app-a-ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-a-ingress
spec:
  rules:
  - host: app-a.example.com
    http:
      paths:
      - path: /appA
        pathType: Prefix
        backend:
          service:
            name: app-a
            port:
              number: 80
---
# app-b-ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-b-ingress
spec:
  rules:
  - host: app-b.example.com
    http:
      paths:
      - path: /appB
        pathType: Prefix
        backend:
          service:
            name: app-b
            port:
              number: 80
```

### Option 2: Single Ingress with Multiple Rules
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: multi-app-ingress
spec:
  rules:
  - host: app-a.example.com
    http:
      paths:
      - path: /appA
        pathType: Prefix
        backend:
          service:
            name: app-a
            port:
              number: 80
  - host: app-b.example.com
    http:
      paths:
      - path: /appB
        pathType: Prefix
        backend:
          service:
            name: app-b
            port:
              number: 80
```

### Using Imperative Commands
```bash
# Create ingress for app-a
kubectl create ingress app-a-ingress \
  --rule="app-a.example.com/appA=app-a:80"

# Create ingress for app-b
kubectl create ingress app-b-ingress \
  --rule="app-b.example.com/appB=app-b:80"
```

### Multiple Paths Same Host
```bash
# Create ingress with multiple paths on same host
kubectl create ingress my-ingress --class=default \
  --rule="example.com/=service1:80" \
  --rule="example.com/admin/=service2:8080"
```

## Key Concepts
- **Multiple Rules**: Different hosts in same Ingress
- **Multiple Paths**: Different paths for same host
- **Path Types**: Prefix, Exact, ImplementationSpecific
- **Host-based Routing**: Route based on domain name

## Verification
```bash
# List all ingresses
kubectl get ingress

# Describe specific ingress
kubectl describe ingress app-a-ingress

# Test routing
curl -H "Host: app-a.example.com" http://<ingress-ip>/appA
curl -H "Host: app-b.example.com" http://<ingress-ip>/appB
```
