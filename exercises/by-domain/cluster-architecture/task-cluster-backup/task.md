# Task: Cluster Backup

## Objective
Backup all cluster resources to YAML files for disaster recovery.

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

### Backup etcd (Control Plane)
```bash
# Backup etcd (requires access to control plane)
ETCDCTL_API=3 etcdctl snapshot save /backup/etcd-snapshot.db \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key
```

## Key Concepts
- **Resource Backup**: Export Kubernetes resources as YAML
- **etcd Backup**: Backup cluster state store
- **Disaster Recovery**: Restore cluster from backups
- **Namespace Backup**: Backup resources in specific namespace

## Best Practices
- Regular automated backups
- Store backups in secure location
- Test restore procedures
- Backup etcd separately (contains cluster state)
- Include all resource types, not just "all"

## Restore from Backup
```bash
# Restore resources from YAML
kubectl apply -f all-resources.yaml

# Restore etcd from snapshot
ETCDCTL_API=3 etcdctl snapshot restore /backup/etcd-snapshot.db \
  --data-dir=/var/lib/etcd-backup
```

## Additional Backup Commands
```bash
# Backup with custom resources
kubectl get all,configmaps,secrets,persistentvolumeclaims --all-namespaces -o yaml > complete-backup.yaml

# Backup specific resource by name
kubectl get deployment my-app -o yaml > my-app-deployment.yaml

# Backup with labels
kubectl get all -l app=myapp -o yaml > myapp-resources.yaml
```
