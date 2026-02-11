# Task: Create ClusterRole and ClusterRoleBinding

## Objective
Grant the 'cluster-admin' role to a user named 'cluster-admin' with permissions to manage nodes in the cluster.

## Requirements
Create a ClusterRole named 'cluster-admin' with:
- API group: [""]
- Resource: ["nodes"]
- Verbs: ["list", "get", "create", "delete"]

Bind the ClusterRole 'cluster-admin' to the user 'cluster-admin' using a ClusterRoleBinding named 'cluster-admin-role-binding'.
