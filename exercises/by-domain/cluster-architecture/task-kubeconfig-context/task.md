# Task: Manage Kubeconfig Contexts

## Objective
Manage kubectl contexts for different users, namespaces, and clusters.

## Task 1: Set Default Namespace for Current Context
```bash
# Permanently save namespace for all subsequent kubectl commands
kubectl config set-context --current --namespace=ggcka-s2

# Verify
kubectl config view
```

## Task 2: Create and Use New Context
```bash
# Set context with specific user and namespace
kubectl config set-context gce --user=cluster-admin --namespace=default

# Use the context
kubectl config use-context gce

# Verify current context
kubectl config get-contexts
```

## Task 3: View and Manage Contexts
```bash
# List all contexts
kubectl config get-contexts

# View current context
kubectl config current-context

# View full kubeconfig
kubectl config view

# View specific context
kubectl config view --context=gce
```

## Key Concepts
- **Context**: Combination of cluster, user, and namespace
- **Current Context**: Active context used by kubectl
- **Namespace**: Default namespace for commands
- **kubeconfig**: Configuration file (~/.kube/config)

## Common Operations
```bash
# Switch contexts
kubectl config use-context <context-name>

# Rename context
kubectl config rename-context <old-name> <new-name>

# Delete context
kubectl config delete-context <context-name>
```
