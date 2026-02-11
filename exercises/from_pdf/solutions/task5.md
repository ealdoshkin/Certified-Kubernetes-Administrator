# Solution for Task 5: Drain Node

```bash
# 1. Mark node as unschedulable
kubectl cordon ek8s-node-1

# 2. Drain the node (evict pods)
kubectl drain ek8s-node-1 --ignore-daemonsets --delete-emptydir-data

# 3. Verify node status
kubectl get nodes

# 4. To make node schedulable again (optional)
kubectl uncordon ek8s-node-1
```
