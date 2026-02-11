# Task: ServiceAccount RBAC Configuration

## Objective
Implement RBAC for ServiceAccount 'sam-acct' with limited access to resources within the 'default' namespace.

## Requirements
1. Update existing Role 'sam-role' to grant read (get) access to 'pods' resource
2. Create new Role 'secret-reader-role' that allows get access to Secrets
3. Create RoleBinding 'secret-reader-binding' to bind 'secret-reader-role' to 'sam-acct' ServiceAccount
