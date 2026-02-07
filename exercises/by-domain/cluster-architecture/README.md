# Cluster Architecture, Installation & Configuration (25%)

Exercises covering RBAC, cluster management, upgrades, backups, and cluster components.

## Tasks

1. **task-rbac-serviceaccount** - ServiceAccount and RBAC configuration
   - Create ServiceAccount
   - Create ClusterRole
   - Create RoleBinding/ClusterRoleBinding

2. **task-cluster-upgrade** - Cluster upgrade with kubeadm
   - Upgrade control plane components
   - Drain and uncordon nodes
   - Update kubelet and kubeadm

3. **task-etcd-backup** - etcd backup and restore
   - Create etcd snapshot
   - Use etcdctl with TLS certificates
   - Backup etcd data

4. **task-static-pod** - Static pod creation
   - Create static pod manifest
   - Place in appropriate directory

5. **task-custom-scheduler** - Custom scheduler creation
   - Create custom scheduler
   - Schedule pods using custom scheduler

6. **task-csr-user-creation** - Create user with Certificate Signing Request
   - Generate private key and CSR
   - Create and approve CSR resource
   - Add user to kubeconfig

7. **task-cluster-upgrade-kubeadm** - Upgrade control plane with kubeadm
   - Plan and execute upgrade
   - Upgrade kubeadm if needed
   - Verify upgrade completion

8. **task-rbac-roles** - Create RBAC roles
   - Create roles for pod reading
   - Create roles for service account creation
   - Create roles for deployment reading

9. **task-rbac-rolebindings** - Create RBAC role bindings
   - Bind roles to users
   - Bind roles to service accounts
   - Test permissions with auth can-i

10. **task-serviceaccount-secure** - Create secure service account
    - Create service account without token mount
    - Verify token is not mounted

11. **task-kubeconfig-context** - Manage kubeconfig contexts
    - Set default namespace
    - Create and switch contexts
    - Manage context configurations

12. **task-cluster-health** - Check cluster health
    - Check control plane health endpoints
    - Verify component status
    - Check node status

13. **task-rbac-pinku-user** - RBAC for user in namespace
    - Create Role with multiple API groups
    - Create RoleBinding for user
    - Test permissions

14. **task-clusterrole-binding** - ClusterRole and ClusterRoleBinding
    - Create ClusterRole for node management
    - Bind ClusterRole to user
    - Cluster-scoped permissions

15. **task-serviceaccount-sam** - ServiceAccount RBAC
    - Create ServiceAccount
    - Create multiple Roles
    - Bind Roles to ServiceAccount

16. **task-tls-certificates** - TLS certificate management
    - Create CA certificates
    - Create user certificates
    - Use Certificate API (CSR)
    - Inspect certificates

17. **task-image-security-registry** - Private registry authentication
    - Create docker-registry secret
    - Use imagePullSecrets in pods
    - Authenticate with private registries

18. **task-security-context-capabilities** - Security context with capabilities
    - Configure user ID
    - Grant Linux capabilities
    - SYS_TIME and NET_ADMIN capabilities

19. **task-security-context-userid** - Security context user ID configuration
    - Pod-level and container-level user IDs
    - Prevent privilege escalation
    - Multi-container pod security

20. **task-cluster-backup** - Cluster backup
    - Backup all resources to YAML
    - Backup etcd
    - Disaster recovery procedures

21. **task-crd-basic** - CustomResourceDefinition
    - Create CRD
    - Create custom resources
    - List and manage CRDs

22. **task-etcd-snapshot-tls** - etcd snapshot with TLS
    - Create etcd snapshot
    - Use TLS certificates
    - Secure etcd backup

23. **task-kubeadm-cluster-setup** - kubeadm cluster setup
    - Initialize master node
    - Join worker nodes
    - Install CNI plugin

24. **task-count-ready-nodes** - Count ready worker nodes
    - Count ready nodes
    - Exclude NoSchedule taints
    - Filter worker nodes

## Key Concepts

- **RBAC**: Role-Based Access Control (Roles, ClusterRoles, RoleBindings)
- **kubeadm**: Cluster installation and management tool
- **etcd**: Cluster state store (backup/restore critical)
- **Static Pods**: Pods managed by kubelet directly
- **Scheduler**: Pod scheduling logic

## Practice Tips

- Master RBAC - very commonly tested
- Practice etcd backup/restore procedures
- Understand kubeadm upgrade process
- Know static pod locations and configuration

---

**Exam Weight**: 25% - Second highest priority
