# Task: Create Simple Ingress Resource

## Objective
Deploy a web application and create an Ingress resource to route traffic to it.

## Requirements
- Web application named "my-web-app" listening on port 80
- Create Ingress resource to route traffic to the service
- Accessible using domain "my-web-app.example.com"

## Solution

### Using Imperative Command
```bash
# Create Ingress resource
kubectl create ingress my-web-app-ingress \
  --rule="my-web-app.example.com/*=my-web-app:80"
```

### Using YAML
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-web-app-ingress
spec:
  rules:
  - host: my-web-app.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: my-web-app
            port:
              number: 80
```

## Prerequisites
```bash
# Ensure service exists
kubectl create service clusterip my-web-app --tcp=80:80

# Or if deployment exists, expose it
kubectl expose deployment my-web-app --port=80 --target-port=80
```

## Key Concepts
- **Ingress**: HTTP/HTTPS routing to services
- **Host**: Domain name for routing
- **Path**: URL path for routing
- **Backend**: Service and port to route to
- **Ingress Controller**: Required to implement Ingress

## Verification
```bash
# Check Ingress
kubectl get ingress my-web-app-ingress

# Describe Ingress
kubectl describe ingress my-web-app-ingress

# Test access (if ingress controller is configured)
curl -H "Host: my-web-app.example.com" http://<ingress-ip>/
```

## Common Ingress Commands
```bash
# Create ingress with single rule
kubectl create ingress <name> --rule="<host>/<path>=<service>:<port>"

# Create ingress with class
kubectl create ingress <name> --class=nginx --rule="<host>/<path>=<service>:<port>"
```
