# Task: Create RBAC Roles

## Objective
Create various RBAC roles for different use cases.

## Task 1: Create Role for Pod Reading

### Using kubectl command line
```bash
# Create a role that allows get, watch, and list on pods and pod logs
kubectl create role pod-reader --verb=get,watch,list --resource=pods,pods/log
```

### Using YAML file
```bash
# Create role.yaml
cat <<EOF > role.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: default
  name: pod-reader
rules:
- apiGroups: [""]
  resources: ["pods", "pods/log"]
  verbs: ["get", "watch", "list"]
EOF

# Apply the role
kubectl apply -f role.yaml
```

## Task 2: Create Role for Service Account Creation
```bash
# Create role that allows creating service accounts
kubectl create role sa-creator --verb=create --resource=sa
```

## Task 3: Create Role for Deployment Reading
```bash
# Create namespace
kubectl create ns cka-20834

# Create role in namespace for deployment reading
kubectl -n cka-20834 create role deployment-reader --verb=get,list --resource=deploy --api-group=apps
```

## Verification
```bash
# Test permissions with auth can-i
kubectl auth can-i get pods --as=system:serviceaccount:default:pod-reader
kubectl auth can-i create sa --as=system:serviceaccount:default:sa-creator
```

## Key Concepts
- **Role**: Namespace-scoped RBAC resource
- **ClusterRole**: Cluster-scoped RBAC resource
- **Verbs**: Actions (get, list, watch, create, update, delete, patch)
- **Resources**: Kubernetes resources (pods, services, deployments, etc.)
