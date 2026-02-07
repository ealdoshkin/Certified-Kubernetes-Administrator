# Task: DaemonSet

## Objective
Create a DaemonSet to ensure a single instance of a pod runs on each node.

## Requirements
- DaemonSet name: `ds-kusc00201`
- Image: `nginx`
- Ensure one pod per node
- Do not override existing taints

## Solution

### Create DaemonSet
```bash
kubectl create deployment ds-kusc00201 --image=nginx --dry-run=client -o yaml > daemonset.yaml
```

Edit daemonset.yaml to convert to DaemonSet:
```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: ds-kusc00201
spec:
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx
```

### Or Using Imperative Command
```bash
kubectl create daemonset ds-kusc00201 --image=nginx
```

## Key Concepts
- **DaemonSet**: Ensures one pod per node
- **Node Selection**: Automatically schedules on all nodes
- **Taints**: Respects node taints (won't schedule on tainted nodes unless toleration added)
- **Use Cases**: Logging agents, monitoring agents, network plugins

## DaemonSet with Tolerations
```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: ds-kusc00201
spec:
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      tolerations:
      - key: node-role.kubernetes.io/control-plane
        operator: Exists
        effect: NoSchedule
      containers:
      - name: nginx
        image: nginx
```

## Verification
```bash
# Check DaemonSet
kubectl get daemonset ds-kusc00201

# Check pods (should be one per node)
kubectl get pods -l app=nginx -o wide

# Verify pod distribution
kubectl get pods -l app=nginx -o wide | grep -c Running
kubectl get nodes | grep -v NAME | wc -l
```

## Common Use Cases
- Logging agents (fluentd, filebeat)
- Monitoring agents (node-exporter)
- Network plugins
- Storage daemons
- Security agents
