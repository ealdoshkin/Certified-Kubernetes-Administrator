# Task: Ingress Path Rewriting

## Objective
Configure Ingress resource to rewrite the path "/app" to "/new-app" before routing traffic to the service.

## Requirements
- Web application named "my-web-app"
- Ingress should rewrite path "/app" to "/new-app"
- Route to "my-web-app" service

## Solution

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-web-app-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /new-app
spec:
  rules:
  - host: my-web-app.example.com
    http:
      paths:
      - path: /app
        pathType: Prefix
        backend:
          service:
            name: my-web-app
            port:
              number: 80
```

## Key Concepts
- **Path Rewriting**: Modify URL path before forwarding to backend
- **Annotations**: Ingress controller-specific configurations
- **rewrite-target**: Nginx ingress controller annotation for path rewriting
- **Path Matching**: Matches "/app" but forwards "/new-app"

## Ingress Controller Specific
Different ingress controllers use different annotations:

### Nginx Ingress Controller
```yaml
annotations:
  nginx.ingress.kubernetes.io/rewrite-target: /new-app
```

### Other Controllers
- Traefik: Uses different annotation format
- Istio: Uses VirtualService for advanced routing

## Verification
```bash
# Create ingress
kubectl apply -f my-web-app-ingress.yaml

# Check ingress
kubectl get ingress my-web-app-ingress

# Describe to see annotations
kubectl describe ingress my-web-app-ingress

# Test path rewriting
curl -H "Host: my-web-app.example.com" http://<ingress-ip>/app
# Should route to /new-app on backend
```

## Advanced Path Rewriting
```yaml
# Rewrite with capture groups (Nginx)
annotations:
  nginx.ingress.kubernetes.io/rewrite-target: /$2
spec:
  rules:
  - http:
      paths:
      - path: /app(/|$)(.*)
        pathType: ImplementationSpecific
```

## Best Practices
- Document path rewriting rules
- Test thoroughly with different paths
- Consider using Gateway API for advanced routing
- Understand ingress controller limitations
