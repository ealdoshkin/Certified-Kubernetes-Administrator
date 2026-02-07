# Task: Troubleshoot Kube-Proxy Failure

## Objective
Troubleshoot and fix kube-proxy component failure.

## Scenario: Kube-Proxy Pod in Error State

```bash
# Simulate kube-proxy issue
kubectl replace -f https://raw.githubusercontent.com/chadmcrowell/acing-the-cka-exam/main/ch_08/kube-proxy-configmap.yaml --force

# Delete kube-proxy pod (will recreate)
kubectl -n kube-system delete pod -l k8s-app=kube-proxy

# Check pod status
kubectl -n kube-system get pods | grep kube-proxy
```

## Troubleshooting Steps

### 1. Check Kube-Proxy Pod Status
```bash
# List kube-proxy pods
kubectl -n kube-system get pods -l k8s-app=kube-proxy

# Describe pod
kubectl -n kube-system describe pod <kube-proxy-pod-name>
```

### 2. Check Kube-Proxy Logs
```bash
# View logs
kubectl -n kube-system logs <kube-proxy-pod-name>

# View previous logs if pod restarted
kubectl -n kube-system logs <kube-proxy-pod-name> --previous
```

### 3. Check ConfigMap
```bash
# Check kube-proxy configmap
kubectl -n kube-system get configmap kube-proxy -o yaml

# Describe configmap
kubectl -n kube-system describe configmap kube-proxy
```

### 4. Check DaemonSet
```bash
# Check kube-proxy daemonset
kubectl -n kube-system get daemonset kube-proxy

# Describe daemonset
kubectl -n kube-system describe daemonset kube-proxy
```

## Fix: Restore Kube-Proxy ConfigMap

### Option 1: Restore from Backup
```bash
# Backup current configmap
kubectl -n kube-system get configmap kube-proxy -o yaml > /tmp/kube-proxy-backup.yaml

# Restore correct configmap
kubectl -n kube-system apply -f https://raw.githubusercontent.com/kubernetes/kubernetes/master/cmd/kubeadm/app/phases/addons/proxy/kube-proxy.yaml

# Or manually fix the configmap
kubectl -n kube-system edit configmap kube-proxy
```

### Option 2: Delete and Recreate
```bash
# Delete problematic configmap
kubectl -n kube-system delete configmap kube-proxy

# Restart daemonset (will recreate configmap)
kubectl -n kube-system rollout restart daemonset kube-proxy
```

## Verification
```bash
# Check pod is running
kubectl -n kube-system get pods -l k8s-app=kube-proxy

# Check all kube-proxy pods on all nodes
kubectl -n kube-system get pods -l k8s-app=kube-proxy -o wide

# Test service connectivity
kubectl get svc
curl <service-ip>:<port>
```

## Key Concepts
- **Kube-Proxy**: Network proxy for services
- **DaemonSet**: Runs on every node
- **ConfigMap**: Configuration for kube-proxy
- **Service Connectivity**: Kube-proxy enables service IP routing

## Common Issues
- ConfigMap syntax errors
- Network plugin conflicts
- IPVS/iptables mode issues
- Node network problems
