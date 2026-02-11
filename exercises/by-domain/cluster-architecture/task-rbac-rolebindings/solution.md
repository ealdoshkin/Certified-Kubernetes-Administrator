# Task: Create RBAC RoleBindings

## Objective
Create RoleBindings to bind roles to users or service accounts.

## Task 1: Bind Role to User

### Using YAML
```bash
# Create role-binding.yaml
cat <<EOF > role-binding.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: pod-reader
  namespace: default
subjects:
- kind: User
  name: dev
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
EOF

# Apply the role binding
kubectl apply -f role-binding.yaml
```

### Test the Role Binding
```bash
# Check if user "dev" can list pods
kubectl auth can-i get pods --namespace=default --as=dev

# Check if user "dev" can view pod logs
kubectl auth can-i get pods/log --namespace=default --as=dev

# Verify user "dev" cannot create pods
kubectl auth can-i create pods --namespace=default --as=dev
```

## Task 2: Bind Role to User (Command Line)
```bash
# Create role binding for user sandra
kubectl create rolebinding sa-creator-binding --role=sa-creator --user=sandra

# Verify permission
kubectl auth can-i create sa --as sandra
```

## Task 3: Bind Role to Service Account
```bash
# Create service account
kubectl -n cka-20834 create sa demo-sa

# Create role binding for service account
kubectl -n cka-20834 create rolebinding deployment-reader-binding --role=deployment-reader --serviceaccount=cka-20834:demo-sa

# Verify permissions
kubectl auth can-i get deployments --as=system:serviceaccount:cka-20834:demo-sa -n cka-20834
kubectl auth can-i list deployments --as=system:serviceaccount:cka-20834:demo-sa -n cka-20834
```

## Key Concepts
- **RoleBinding**: Binds a Role to subjects (users, groups, service accounts) in a namespace
- **ClusterRoleBinding**: Binds a ClusterRole to subjects cluster-wide
- **Subjects**: Users, groups, or service accounts
- **roleRef**: Reference to the role being bound
