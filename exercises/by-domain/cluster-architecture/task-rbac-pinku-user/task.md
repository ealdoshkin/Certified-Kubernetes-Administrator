# Task: Create RBAC Role and RoleBinding for User

## Objective
Set up Role-Based Access Control (RBAC) for the user 'pinku' within the 'argo' namespace with specific permissions.

## Requirements
Create a Role named 'pinku-role' in the 'argo' namespace with:
- API groups: [""], ["apps"], ["extensions"]
- Resources: ["pods"], ["deployments"], ["services"], ["ingress"]
- Verbs: ["get"], ["watch"], ["list"]

Bind the Role 'pinku-role' to the user 'pinku' using a RoleBinding named 'pinku-role-binding'.
