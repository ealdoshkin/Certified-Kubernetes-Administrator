# Task: Resource Requests and Limits

## Objective
Configure CPU and memory requests and limits for pods.

## Solution

### Create Pod with Resource Requests and Limits
```bash
kubectl run nginx --image=nginx --dry-run=client -o yaml > pod.yaml
```

Edit pod.yaml:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - image: nginx
    name: nginx
    resources:
      requests:
        memory: "256Mi"
        cpu: "100m"
      limits:
        memory: "512Mi"
        cpu: "200m"
```

```bash
kubectl apply -f pod.yaml
```

## Key Concepts
- **requests**: Minimum resources guaranteed
- **limits**: Maximum resources allowed
- **CPU**: Measured in cores (100m = 0.1 core)
- **Memory**: Measured in bytes (Mi, Gi, etc.)

## CPU Units
- `100m` = 0.1 CPU
- `1` = 1 CPU
- `500m` = 0.5 CPU

## Memory Units
- `128Mi` = 128 Mebibytes
- `1Gi` = 1 Gibibyte
- `512Mi` = 512 Mebibytes

## Resource Guarantees
- **Requests**: Pod is guaranteed these resources
- **Limits**: Pod cannot exceed these resources
- **OOMKilled**: Pod killed if exceeds memory limit
- **Throttled**: CPU throttled if exceeds CPU limit

## Verification
```bash
# Check pod resources
kubectl describe pod nginx | grep -A 5 "Limits\|Requests"

# Check resource usage (requires metrics-server)
kubectl top pod nginx

# View pod YAML
kubectl get pod nginx -o yaml | grep -A 10 resources
```

## Best Practices
- Always set requests and limits
- Set requests based on actual usage
- Set limits slightly higher than requests
- Monitor resource usage
- Use resource quotas for namespaces
