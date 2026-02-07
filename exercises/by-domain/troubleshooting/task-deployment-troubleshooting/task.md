# Task: Troubleshoot Deployment Issues

## Objective
Troubleshoot deployment issues when pods are not running.

## Scenario: Deployment Pods Not Running After Scaling

```bash
# Create deployment
kubectl -n ee8881 create deployment prod-app --image=nginx

# List pods
kubectl -n ee8881 get pods

# Scale deployment
kubectl -n ee8881 scale deployment prod-app --replicas=3

# Check pod status
kubectl -n ee8881 get pods

# If pods are not running, troubleshoot:
```

## Troubleshooting Steps

### 1. Check Deployment Status
```bash
kubectl -n ee8881 get deployment prod-app
kubectl -n ee8881 describe deployment prod-app
```

### 2. Check ReplicaSet
```bash
kubectl -n ee8881 get rs
kubectl -n ee8881 describe rs <replicaset-name>
```

### 3. Check Pod Status
```bash
kubectl -n ee8881 get pods
kubectl -n ee8881 describe pod <pod-name>
```

### 4. Check Events
```bash
kubectl -n ee8881 get events --sort-by='.lastTimestamp'
```

### 5. Check Logs
```bash
kubectl -n ee8881 logs <pod-name>
```

## Common Issues

### Issue: Pods Stuck in Pending
**Possible Causes:**
- Resource constraints
- Node selector not matching
- Taints on nodes
- Scheduler issues

**Fix:**
```bash
# Check node resources
kubectl describe node <node-name>

# Check node selectors
kubectl get pod <pod-name> -o yaml | grep nodeSelector

# Check taints
kubectl describe node <node-name> | grep Taint
```

### Issue: Pods CrashLoopBackOff
**Possible Causes:**
- Application errors
- Missing configuration
- Wrong image
- Resource limits

**Fix:**
```bash
# View logs
kubectl logs <pod-name> --previous

# Check resource limits
kubectl describe pod <pod-name> | grep -A 5 Limits
```

## Verification
```bash
# Verify all pods are running
kubectl -n ee8881 get pods -l app=prod-app

# Check deployment status
kubectl -n ee8881 rollout status deployment/prod-app
```
