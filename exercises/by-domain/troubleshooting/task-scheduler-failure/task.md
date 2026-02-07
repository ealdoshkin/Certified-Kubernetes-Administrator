# Task: Troubleshoot Scheduler Failure

## Objective
Troubleshoot and fix kube-scheduler component failure.

## Scenario: Scheduler Failure After Configuration Change

```bash
# Simulate scheduler failure by modifying manifest
curl https://raw.githubusercontent.com/chadmcrowell/acing-the-cka-exam/main/ch_08/kube-scheduler.yaml \
  --silent --output /etc/kubernetes/manifests/kube-scheduler.yaml

# Check if pods can be scheduled
kubectl get pods

# Check scheduler status
kubectl get componentstatuses scheduler
```

## Troubleshooting Steps

### 1. Check Scheduler Pod Status
```bash
# Check scheduler pod in kube-system
kubectl -n kube-system get pods | grep scheduler

# Describe scheduler pod
kubectl -n kube-system describe pod <scheduler-pod-name>
```

### 2. Check Scheduler Logs
```bash
# View scheduler logs
kubectl -n kube-system logs <scheduler-pod-name>

# Follow logs
kubectl -n kube-system logs -f <scheduler-pod-name>
```

### 3. Check Scheduler Manifest
```bash
# View scheduler manifest
cat /etc/kubernetes/manifests/kube-scheduler.yaml

# Check for syntax errors
kubectl -n kube-system get pod <scheduler-pod-name> -o yaml
```

### 4. Check Events
```bash
# Check cluster events
kubectl get events --all-namespaces --sort-by='.lastTimestamp' | grep scheduler
```

## Fix: Restore Scheduler

### Option 1: Move Manifest to Restore Default
```bash
# Move problematic manifest
mv /etc/kubernetes/manifests/kube-scheduler.yaml /tmp/kube-scheduler.yaml

# Scheduler will automatically restart with default configuration
```

### Option 2: Fix Manifest
```bash
# Edit the manifest
vi /etc/kubernetes/manifests/kube-scheduler.yaml

# Fix any errors and save
# Scheduler will automatically reload
```

## Verification
```bash
# Check scheduler is running
kubectl -n kube-system get pods | grep scheduler

# Test pod scheduling
kubectl run test-pod --image nginx
kubectl get pod test-pod

# Check scheduler component status
kubectl get componentstatuses scheduler
```

## Key Concepts
- **Static Pod**: Scheduler runs as static pod managed by kubelet
- **Manifest Location**: `/etc/kubernetes/manifests/`
- **Auto-restart**: kubelet automatically restarts static pods
- **Configuration**: Scheduler configuration in manifest

## Common Issues
- Syntax errors in manifest
- Missing command arguments
- Wrong image version
- Resource constraints
