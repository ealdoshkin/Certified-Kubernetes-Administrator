# Task: Liveness Probe

## Objective
Create pods with liveness probes to detect and restart unhealthy containers.

## Task 1: Create Pod with Basic Liveness Probe
```bash
kubectl run nginx --image=nginx --restart=Never --dry-run=client -o yaml > pod.yaml
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
    livenessProbe:
      exec:
        command:
        - ls
    resources: {}
```

```bash
kubectl create -f pod.yaml
kubectl describe pod nginx | grep -i liveness
kubectl delete -f pod.yaml
```

## Task 2: Create Pod with Configured Liveness Probe
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - image: nginx
    name: nginx
    livenessProbe:
      initialDelaySeconds: 5  # wait 5 seconds before first probe
      periodSeconds: 5  # probe every 5 seconds
      exec:
        command:
        - ls
```

## Task 3: HTTP Liveness Probe
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - image: nginx
    name: nginx
    ports:
    - containerPort: 80
    livenessProbe:
      httpGet:
        path: /
        port: 80
      initialDelaySeconds: 10
      periodSeconds: 5
```

## Task 4: TCP Liveness Probe
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - image: nginx
    name: nginx
    ports:
    - containerPort: 80
    livenessProbe:
      tcpSocket:
        port: 80
      initialDelaySeconds: 10
      periodSeconds: 5
```

## Key Concepts
- **livenessProbe**: Detects if container is alive
- **exec**: Execute command in container
- **httpGet**: HTTP GET request
- **tcpSocket**: TCP connection check
- **initialDelaySeconds**: Wait before first probe
- **periodSeconds**: Time between probes
- **timeoutSeconds**: Probe timeout
- **failureThreshold**: Consecutive failures before restart

## Probe Types
- **exec**: Run command (exit code 0 = success)
- **httpGet**: HTTP request (2xx, 3xx = success)
- **tcpSocket**: TCP connection (connection = success)

## Verification
```bash
# Check probe status
kubectl describe pod nginx | grep -A 10 Liveness

# Check pod events
kubectl get events | grep nginx

# View pod status
kubectl get pod nginx
```

## Common Issues
- **Container restarts**: Probe failing repeatedly
- **Startup time**: initialDelaySeconds too short
- **False positives**: Probe too aggressive
