# Task: Create RBAC Role and RoleBinding for User

## Objective
Set up Role-Based Access Control (RBAC) for the user 'pinku' within the 'argo' namespace with specific permissions.

## Requirements
Create a Role named 'pinku-role' in the 'argo' namespace with:
- API groups: [""], ["apps"], ["extensions"]
- Resources: ["pods"], ["deployments"], ["services"], ["ingress"]
- Verbs: ["get"], ["watch"], ["list"]

Bind the Role 'pinku-role' to the user 'pinku' using a RoleBinding named 'pinku-role-binding'.

## Solution

### Using Imperative Commands
```bash
# Step 1: Create the 'pinku-role' Role in the 'argo' namespace
kubectl create role pinku-role --namespace=argo \
  --verb=get,watch,list \
  --resource=pods,deployments,services,ingress

# Step 2: Bind the 'pinku-role' Role to the 'pinku' user
kubectl create rolebinding pinku-role-binding --namespace=argo \
  --role=pinku-role \
  --user=pinku

# Step 3: Test if access is working
kubectl auth can-i get pods --namespace argo --as pinku
kubectl auth can-i list services --namespace argo --as pinku
kubectl auth can-i watch deployments --namespace argo --as pinku
kubectl auth can-i create ingress --namespace argo --as pinku  # Should return "no"
```

### Using YAML
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pinku-role
  namespace: argo
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "watch", "list"]
- apiGroups: ["apps"]
  resources: ["deployments"]
  verbs: ["get", "watch", "list"]
- apiGroups: [""]
  resources: ["services"]
  verbs: ["get", "watch", "list"]
- apiGroups: ["extensions"]
  resources: ["ingress"]
  verbs: ["get", "watch", "list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: pinku-role-binding
  namespace: argo
subjects:
- kind: User
  name: pinku
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: pinku-role
  apiGroup: rbac.authorization.k8s.io
```

## Key Concepts
- **Role**: Namespace-scoped RBAC resource
- **RoleBinding**: Binds Role to subjects (users, groups, service accounts)
- **API Groups**: Different API versions for resources
- **Verbs**: Actions allowed (get, watch, list, create, update, delete)

## Verification
```bash
# Check role exists
kubectl get role pinku-role -n argo

# Check rolebinding exists
kubectl get rolebinding pinku-role-binding -n argo

# Test permissions
kubectl auth can-i get pods --namespace argo --as pinku
```
