# Task: Cluster Backup

## Solution

### Backup All Resources
```bash
# Backup all resources in all namespaces to YAML
kubectl get all --all-namespaces -o yaml > all-resources.yaml

# Backup specific resource types
kubectl get deployments --all-namespaces -o yaml > deployments.yaml
kubectl get services --all-namespaces -o yaml > services.yaml
kubectl get configmaps --all-namespaces -o yaml > configmaps.yaml
kubectl get secrets --all-namespaces -o yaml > secrets.yaml
```

### Backup Specific Namespace
```bash
# Backup all resources in a namespace
kubectl get all -n <namespace> -o yaml > <namespace>-backup.yaml

# Backup everything including non-standard resources
kubectl get all,configmaps,secrets -n <namespace> -o yaml > <namespace>-complete.yaml
```

## Restore from Backup
```bash
# Restore resources from YAML
kubectl apply -f all-resources.yaml
