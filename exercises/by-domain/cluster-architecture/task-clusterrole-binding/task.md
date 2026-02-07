# Task: Create ClusterRole and ClusterRoleBinding

## Objective
Grant the 'cluster-admin' role to a user named 'cluster-admin' with permissions to manage nodes in the cluster.

## Requirements
Create a ClusterRole named 'cluster-admin' with:
- API group: [""]
- Resource: ["nodes"]
- Verbs: ["list", "get", "create", "delete"]

Bind the ClusterRole 'cluster-admin' to the user 'cluster-admin' using a ClusterRoleBinding named 'cluster-admin-role-binding'.

## Solution

### Using Imperative Commands
```bash
# Step 1: Create the 'cluster-admin' ClusterRole
kubectl create clusterrole cluster-admin --verb=list,get,create,delete --resource=nodes

# Step 2: Bind the ClusterRole to the user
kubectl create clusterrolebinding cluster-admin-role-binding \
  --clusterrole=cluster-admin \
  --user=cluster-admin

# Step 3: Test the access
kubectl auth can-i list nodes --as cluster-admin
kubectl auth can-i get nodes --as cluster-admin
kubectl auth can-i create nodes --as cluster-admin
kubectl auth can-i delete nodes --as cluster-admin
```

### Using YAML
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: cluster-admin
rules:
- apiGroups: [""]
  resources: ["nodes"]
  verbs: ["list", "get", "create", "delete"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: cluster-admin-role-binding
subjects:
- kind: User
  name: cluster-admin
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: cluster-admin
  apiGroup: rbac.authorization.k8s.io
```

## Key Concepts
- **ClusterRole**: Cluster-scoped RBAC resource (applies to all namespaces)
- **ClusterRoleBinding**: Binds ClusterRole to subjects cluster-wide
- **Nodes**: Cluster-level resource (not namespaced)
- **API Groups**: Empty string "" for core API group

## Verification
```bash
# Check clusterrole exists
kubectl get clusterrole cluster-admin

# Check clusterrolebinding exists
kubectl get clusterrolebinding cluster-admin-role-binding

# Test permissions
kubectl auth can-i list nodes --as cluster-admin
```

## Additional Commands
```bash
# Get API groups for resources
kubectl api-resources | grep nodes

# Count clusterrolebindings
kubectl get clusterrolebindings --no-headers | wc -l
```
