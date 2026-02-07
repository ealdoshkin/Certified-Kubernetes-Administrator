# Task: Readiness Probe

## Objective
Create pods with readiness probes to control when pods receive traffic.

## Solution

### Create Pod with HTTP Readiness Probe
```bash
kubectl run nginx --image=nginx --dry-run=client -o yaml --restart=Never --port=80 > pod.yaml
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
    ports:
    - containerPort: 80
    readinessProbe:
      httpGet:
        path: /
        port: 80
      initialDelaySeconds: 5
      periodSeconds: 5
```

```bash
kubectl create -f pod.yaml
kubectl describe pod nginx | grep -i readiness
kubectl delete -f pod.yaml
```

## Key Concepts
- **readinessProbe**: Detects if container is ready to serve traffic
- **Not Ready**: Pod removed from Service endpoints
- **Ready**: Pod added to Service endpoints
- **Different from liveness**: Readiness doesn't restart container

## Readiness Probe Types
- **exec**: Execute command
- **httpGet**: HTTP GET request
- **tcpSocket**: TCP connection

## Example: Exec Readiness Probe
```yaml
readinessProbe:
  exec:
    command:
    - cat
    - /tmp/ready
  initialDelaySeconds: 5
  periodSeconds: 5
```

## Example: TCP Readiness Probe
```yaml
readinessProbe:
  tcpSocket:
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 5
```

## Combined Liveness and Readiness
```yaml
containers:
- image: nginx
  name: nginx
  livenessProbe:
    httpGet:
      path: /healthz
      port: 8080
    initialDelaySeconds: 10
    periodSeconds: 5
  readinessProbe:
    httpGet:
      path: /ready
      port: 8080
    initialDelaySeconds: 5
    periodSeconds: 5
```

## Verification
```bash
# Check readiness status
kubectl get pod nginx
# READY column shows 1/1 when ready

# Describe probe status
kubectl describe pod nginx | grep -A 10 Readiness

# Check if pod is in service endpoints
kubectl get endpoints <service-name>
```

## Use Cases
- Application startup time
- Database connection readiness
- Cache warmup
- Dependency availability
