# Task: Troubleshoot Pod Issues

## Objective
Troubleshoot various pod issues and get them running.

## Scenario 1: MySQL Deployment Not Running

```bash
# Create deployment
kubectl -n db08328 create deployment mysql --image=mysql:8

# List pods
kubectl -n db08328 get pods

# Check pod status
kubectl -n db08328 describe pod <pod-name>

# View logs
kubectl -n db08328 logs <pod-name>

# Common issues:
# - Missing environment variables (MYSQL_ROOT_PASSWORD)
# - Wrong image version
# - Resource constraints
```

## Scenario 2: Testbox Pod Not Running

```bash
# Create pod
kubectl run testbox --image busybox --command 'sleep 3600'

# Check pod status
kubectl get pod testbox

# Describe pod
kubectl describe pod testbox

# View events
kubectl get events --sort-by='.lastTimestamp'

# Common troubleshooting steps:
# 1. Check pod status
# 2. Check events
# 3. Check logs
# 4. Check resource limits
# 5. Check node resources
```

## Scenario 3: Busybox Container Failing

```bash
# Create pod
kubectl run busybox2 --image busybox:1.35.0

# Check status
kubectl get pod busybox2

# Describe pod
kubectl describe pod busybox2

# View logs
kubectl logs busybox2

# Fix: Add command to keep container running
kubectl run busybox2 --image busybox:1.35.0 --command -- sleep 3600
```

## Scenario 4: Curlpod Not Running

```bash
# Create pod with shell
kubectl run curlpod2 --image nicolaka/netshoot -it --rm -- /bin/sh

# Inside pod, test DNS
nslookup kubernetes

# Exit and check why container stopped
kubectl get pod curlpod2
kubectl describe pod curlpod2

# Fix: Add command to keep running
kubectl run curlpod2 --image nicolaka/netshoot --command -- sleep 3600
```

## Troubleshooting Decision Tree

1. **Check Pod Status**
   ```bash
   kubectl get pod <pod-name>
   kubectl describe pod <pod-name>
   ```

2. **Check Events**
   ```bash
   kubectl get events --sort-by='.lastTimestamp'
   kubectl get events --field-selector involvedObject.name=<pod-name>
   ```

3. **Check Logs**
   ```bash
   kubectl logs <pod-name>
   kubectl logs <pod-name> -c <container-name>  # Multi-container pods
   ```

4. **Check Resource Constraints**
   ```bash
   kubectl top pod <pod-name>
   kubectl describe node <node-name>
   ```

5. **Check Image Issues**
   ```bash
   kubectl describe pod <pod-name> | grep -i image
   kubectl get pod <pod-name> -o jsonpath='{.spec.containers[*].image}'
   ```

## Common Issues and Fixes

- **ImagePullBackOff**: Wrong image name, private registry auth, network issues
- **CrashLoopBackOff**: Application error, missing config, wrong command
- **Pending**: Resource constraints, node selector issues, taints
- **Error**: Container failed to start, command error
