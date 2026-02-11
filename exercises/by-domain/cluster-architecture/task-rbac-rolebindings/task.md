# Task: Create RBAC RoleBindings

## Objective

Create a Role named pod-reader in the default namespace with permissions
to get and list pods and view pod logs, then create a RoleBinding named
pod-reader-binding to bind this Role to user dev, and verify that user dev
can get pods and view pod logs but cannot create or delete pods.
