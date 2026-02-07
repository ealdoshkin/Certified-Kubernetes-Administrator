# Task: Pod Logs

## Objective
View and follow pod logs for troubleshooting.

## Solution

### Create Pod with Logging
```bash
kubectl run busybox --image=busybox --restart=Never -- /bin/sh -c 'i=0; while true; do echo "$i: $(date)"; i=$((i+1)); sleep 1; done'
```

### View Logs
```bash
# View logs
kubectl logs busybox

# Follow logs (like tail -f)
kubectl logs busybox -f

# View last N lines
kubectl logs busybox --tail=50

# View logs since timestamp
kubectl logs busybox --since=10m

# View logs from specific time
kubectl logs busybox --since-time="2024-01-01T00:00:00Z"
```

### Multi-Container Pod Logs
```bash
# View logs from specific container
kubectl logs busybox -c <container-name>

# View logs from all containers
kubectl logs busybox --all-containers=true
```

### Previous Container Logs
```bash
# View logs from previous container instance (if restarted)
kubectl logs busybox --previous
```

## Key Concepts
- **logs**: View container stdout/stderr
- **-f**: Follow logs (stream)
- **--tail**: Last N lines
- **--since**: Logs since duration
- **--previous**: Previous container instance

## Log Commands
```bash
# Basic log viewing
kubectl logs <pod-name>

# Follow logs
kubectl logs -f <pod-name>

# Last 100 lines
kubectl logs <pod-name> --tail=100

# Logs from last 10 minutes
kubectl logs <pod-name> --since=10m

# Previous container
kubectl logs <pod-name> --previous
```

## Verification
```bash
# Check pod is running
kubectl get pod busybox

# View logs
kubectl logs busybox

# Follow logs in real-time
kubectl logs busybox -f
```

## Use Cases
- Application debugging
- Error investigation
- Performance monitoring
- Audit trails
