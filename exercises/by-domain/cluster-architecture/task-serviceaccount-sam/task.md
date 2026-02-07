# Task: ServiceAccount RBAC Configuration

## Objective
Implement RBAC for ServiceAccount 'sam-acct' with limited access to resources within the 'default' namespace.

## Requirements
1. Update existing Role 'sam-role' to grant read (get) access to 'pods' resource
2. Create new Role 'secret-reader-role' that allows get access to Secrets
3. Create RoleBinding 'secret-reader-binding' to bind 'secret-reader-role' to 'sam-acct' ServiceAccount

## Solution

### Using Imperative Commands
```bash
# Step 1: Create the service account
kubectl create serviceaccount sam-acct

# Step 2: Create/update the role with pod get permission
kubectl create role sam-role --verb=create,delete,list,get --resource=pods,deployments,secrets,configmaps --namespace=default

# Step 3: Create role binding for sam-role
kubectl create rolebinding sam-rolebinding --role=sam-role --serviceaccount=default:sam-acct

# Step 4: Create secret-reader-role
kubectl create role secret-reader-role --verb=get --resource=secrets --namespace=default

# Step 5: Create role binding for secret-reader-role
kubectl create rolebinding secret-reader-binding --role=secret-reader-role --serviceaccount=default:sam-acct

# Step 6: Test permissions
kubectl auth can-i create pods --as=system:serviceaccount:default:sam-acct
kubectl auth can-i get pods --as=system:serviceaccount:default:sam-acct
kubectl auth can-i get secrets --as=system:serviceaccount:default:sam-acct
```

## Key Concepts
- **ServiceAccount**: Identity for pods to authenticate to API server
- **ServiceAccount Format**: `system:serviceaccount:<namespace>:<serviceaccount-name>`
- **RoleBinding**: Binds Role to ServiceAccount
- **Multiple Roles**: ServiceAccount can have multiple roles bound

## ServiceAccount in Deployment
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-deployment
spec:
  template:
    spec:
      serviceAccountName: sam-acct  # Use service account
      containers:
      - name: app
        image: nginx
```

## ServiceAccount Commands
```bash
# Create service account
kubectl create serviceaccount developer

# Create service account with dry-run
kubectl create serviceaccount pvviewer --dry-run=client -o yaml > svc-act.yaml

# Set service account for deployment
kubectl set serviceaccount deploy/my-deployment my-sa

# Create token for service account
kubectl create token sam-acct
```

## Verification
```bash
# Check service account
kubectl get serviceaccount sam-acct

# Check roles
kubectl get role sam-role secret-reader-role

# Check role bindings
kubectl get rolebinding sam-rolebinding secret-reader-binding

# Test permissions
kubectl auth can-i get pods --as=system:serviceaccount:default:sam-acct
```
