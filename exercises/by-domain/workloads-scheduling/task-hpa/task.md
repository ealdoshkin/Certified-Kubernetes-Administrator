# Task: Horizontal Pod Autoscaler (HPA)

## Objective
Create and manage Horizontal Pod Autoscaler for automatic scaling.

## Prerequisites
- Metrics Server must be installed and running
- Deployment must have resource requests defined

## Task 1: Create Deployment with Resource Requests
```bash
kubectl create deployment nginx --image=nginx --replicas=2
```

Edit deployment to add resource requests:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
spec:
  replicas: 2
  template:
    spec:
      containers:
      - image: nginx
        name: nginx
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
```

## Task 2: Create Horizontal Pod Autoscaler
```bash
# Create HPA
kubectl autoscale deployment nginx --min=5 --max=10 --cpu-percent=80

# Or using YAML
cat <<EOF | kubectl apply -f -
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: nginx
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: nginx
  minReplicas: 5
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 80
EOF
```

## Task 3: Check HPA Status
```bash
# Get HPA
kubectl get hpa nginx

# Describe HPA
kubectl describe hpa nginx

# Check current metrics
kubectl top pods -l app=nginx
```

## Task 4: Test Autoscaling
```bash
# Generate load (in another terminal)
kubectl run -i --tty load-generator --rm --image=busybox --restart=Never -- /bin/sh -c "while true; do wget -q -O- http://nginx-service; done"

# Watch HPA
watch kubectl get hpa nginx

# Watch pods
watch kubectl get pods -l app=nginx
```

## Task 5: Delete HPA
```bash
kubectl delete hpa nginx
```

## Key Concepts
- **HPA**: Automatically scales pods based on metrics
- **minReplicas**: Minimum number of pods
- **maxReplicas**: Maximum number of pods
- **targetCPUUtilization**: Target CPU percentage
- **Metrics Server**: Required for CPU/memory metrics

## HPA Metrics
- **CPU Utilization**: Most common metric
- **Memory Utilization**: Can also be used
- **Custom Metrics**: External metrics from custom APIs

## Verification
```bash
# Check HPA
kubectl get hpa

# Check deployment replicas
kubectl get deploy nginx

# Check pods
kubectl get pods -l app=nginx

# Check metrics
kubectl top pods -l app=nginx
```

## Important Notes
- HPA requires metrics-server
- Deployment must have resource requests
- HPA adjusts replicas based on average utilization
- Scaling happens gradually (not instant)
