# Task: Pod Debugging

## Objective
Debug pod issues by examining pod status, events, and errors.

## Task 1: Debug Pod with Command Error
```bash
# Create pod with error
kubectl run busybox --restart=Never --image=busybox -- /bin/sh -c 'ls /notexist'

# Check pod status
kubectl get pod busybox

# View logs (will show error)
kubectl logs busybox

# Describe pod (shows events with error)
kubectl describe po busybox

# Check events
kubectl get events | grep -i error

# Cleanup
kubectl delete po busybox
```

## Task 2: Debug Pod with Non-existent Command
```bash
# Create pod with non-existent command
kubectl run busybox --restart=Never --image=busybox -- notexist

# Check pod status
kubectl get pod busybox

# View logs (will be empty - container never started)
kubectl logs busybox

# Describe pod (events section shows error)
kubectl describe po busybox

# Check events for errors
kubectl get events | grep -i error

# Force delete
kubectl delete po busybox --force --grace-period=0
```

## Task 3: Check Node Resource Usage
```bash
# Get CPU/memory utilization (requires metrics-server)
kubectl top nodes

# Get pod resource usage
kubectl top pods

# Get specific pod usage
kubectl top pod <pod-name>
```

## Task 4: List Failed Liveness Probes
```bash
# List pods with failed liveness probes across namespaces
kubectl get events -o json | jq -r '.items[] | select(.message | contains("Liveness probe failed")).involvedObject | .namespace + "/" + .name'
```

## Key Concepts
- **describe**: Detailed pod information including events
- **events**: Cluster events showing what happened
- **logs**: Container stdout/stderr
- **status**: Pod phase and conditions
- **top**: Resource usage (requires metrics-server)

## Common Pod States
- **Pending**: Waiting to be scheduled
- **Running**: Pod is running
- **Succeeded**: Container completed successfully
- **Failed**: Container failed
- **Unknown**: Node communication issues

## Common Errors
- **ErrImagePull**: Cannot pull image
- **ImagePullBackOff**: Retrying image pull
- **CrashLoopBackOff**: Container crashes repeatedly
- **OOMKilled**: Out of memory
- **Error**: Container error

## Debugging Steps
1. Check pod status: `kubectl get pod <name>`
2. View logs: `kubectl logs <pod-name>`
3. Describe pod: `kubectl describe pod <name>`
4. Check events: `kubectl get events`
5. Check resource usage: `kubectl top pod <name>`

## Verification
```bash
# Check pod status
kubectl get pod <pod-name>

# View detailed information
kubectl describe pod <pod-name>

# View logs
kubectl logs <pod-name>

# Check events
kubectl get events --field-selector involvedObject.name=<pod-name>
```
