# Exercises Organized by Domain

This directory contains exercises organized by CKA exam domains, with duplicate and incomplete tasks removed.

## Structure

```
by-domain/
├── storage/                  # 10% of exam
├── cluster-architecture/     # 25% of exam
├── networking/              # 20% of exam
├── workloads-scheduling/    # 15% of exam
└── troubleshooting/         # 30% of exam
```

## Domain Breakdown

### 1. Storage (10%) - 6 tasks
- `task-pvc-mount-patch` - PVC creation, mounting, and capacity patching
- `task-pv-hostpath` - Persistent Volume with hostPath (2Gi)
- `task-pv-hostpath-large` - Persistent Volume with hostPath (10Gi)
- `task-emptydir-volume` - emptyDir volume for multi-container pods
- `task-pv-pvc-basic` - PV and PVC basics
- `task-pvc-expansion` - Expand PersistentVolumeClaim capacity

### 2. Cluster Architecture, Installation & Configuration (25%) - 24 tasks
- `task-rbac-serviceaccount` - ServiceAccount and RBAC (ClusterRole/RoleBinding)
- `task-cluster-upgrade` - Cluster upgrade with kubeadm
- `task-etcd-backup` - etcd backup and restore
- `task-static-pod` - Static pod creation
- `task-custom-scheduler` - Custom scheduler creation and usage
- `task-csr-user-creation` - Create user with CSR
- `task-cluster-upgrade-kubeadm` - Upgrade control plane with kubeadm
- `task-rbac-roles` - Create RBAC roles
- `task-rbac-rolebindings` - Create RBAC role bindings
- `task-serviceaccount-secure` - Secure service account without token
- `task-kubeconfig-context` - Manage kubeconfig contexts
- `task-cluster-health` - Check cluster health status
- `task-etcd-snapshot-tls` - etcd snapshot with TLS certificates
- `task-kubeadm-cluster-setup` - kubeadm cluster setup (master and worker)
- `task-count-ready-nodes` - Count ready worker nodes excluding taints

### 3. Services & Networking (20%) - 12 tasks
- `task-ingress` - Ingress resource creation
- `task-networkpolicy` - NetworkPolicy configuration
- `task-service-nodeport` - Service creation (NodePort)
- `task-ingress-simple` - Simple Ingress resource
- `task-ingress-multi-path` - Ingress with multiple paths/hosts
- `task-ingress-path-rewrite` - Ingress path rewriting
- `task-networkpolicy-frontend-backend` - Frontend to backend NetworkPolicy
- `task-networkpolicy-database-admin` - Restrict database access
- `task-networkpolicy-egress-cidr` - Egress to CIDR range
- `task-networkpolicy-app-db` - App to database on specific port
- `task-networkpolicy-allow-all` - Allow all traffic in namespace
- `task-dns-lookup` - DNS lookup for services and pods

### 4. Workloads & Scheduling (15%) - 32 tasks
- `task-pod-cpu-monitoring` - Pod CPU usage monitoring
- `task-pod-node-selector` - Pod scheduling with node selector
- `task-deployment-rollback` - Deployment rollback operations
- `task-deployment-scale` - Deployment scaling
- `task-deployment-mixed` - Mixed deployment operations (scaling, pod creation, monitoring)
- `task-multi-container-pod` - Multi-container pod creation
- `task-node-drain` - Node drain and pod rescheduling
- `task-pod-namespace` - Pod creation in namespace
- `task-configmap` - Create and use ConfigMaps
- `task-secret` - Create secrets
- `task-node-affinity` - Pod scheduling with node affinity
- `task-init-container` - Init containers for pod setup
- `task-daemonset` - DaemonSet for one pod per node
- `task-custom-columns` - Custom columns output formatting
- `task-sort-resources` - Sort resources by fields
- `task-pod-ip-extraction` - Extract pod IP addresses
- `task-service-endpoints` - List pods implementing service

### 5. Troubleshooting (30%) - 16 tasks
- `task-sidecar-logging` - Sidecar container for logging
- `task-log-extraction` - Log monitoring and extraction
- `task-node-notready` - Node troubleshooting (NotReady state)
- `task-node-status-check` - Node status verification
- `task-pod-troubleshooting` - Troubleshoot pod issues
- `task-deployment-troubleshooting` - Troubleshoot deployment issues
- `task-scheduler-failure` - Troubleshoot scheduler failure
- `task-kubelet-failure` - Troubleshoot kubelet failure
- `task-kubeproxy-failure` - Troubleshoot kube-proxy failure
- `task-service-connectivity` - Troubleshoot service connectivity
- `task-find-failed-probe` - Find pods with failed liveness probes
- `task-cpu-usage-monitoring` - Find pod with highest CPU usage

## Task Organization

**Total Tasks**: 88 organized tasks (23 from cka-lab + 16 from exercises/1/ + 19 from exercises/2/ + 17 from CKAD-exercises/ + 13 from practice-exams/)

**Removed Tasks**:
- Task15 - Split into separate tasks (deployment-mixed)
- Task21 - Duplicate of Task13 (node troubleshooting)
- Task22 - Empty task
- Task24 - Incomplete task

## How to Use

1. **Start with highest weight domains**: Troubleshooting (30%) and Cluster Architecture (25%)
2. **Work through tasks systematically**: Each task directory contains:
   - `task.md` - Task description
   - `solution/` - Solution files (if available)
3. **Practice hands-on**: Don't just read, actually complete the tasks
4. **Review solutions**: Compare your approach with provided solutions
5. **Repeat difficult tasks**: Mastery comes from repetition

## Related Resources

- Domain Documentation: `../../domains/` - Detailed domain guides
- Practice Exams: `../practice-exams/` - Exam simulation
- Original Lab: `../cka-lab/` - Original 25 tasks (for reference)

---

**Note**: Tasks are organized by domain to align with CKA exam structure. Focus on domains with higher weights for better exam preparation.
