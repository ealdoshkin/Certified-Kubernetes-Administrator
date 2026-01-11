# CKA Exam Domains

This directory contains documentation organized by the five CKA exam domains.

## Domain Structure

```
Domains/
├── troubleshooting/          # 30% of exam
├── cluster-architecture/     # 25% of exam
├── networking/               # 20% of exam
├── workloads-scheduling/     # 15% of exam
└── storage/                 # 10% of exam
```

## Exam Domain Breakdown

### 1. Troubleshooting (30%) ⭐⭐⭐
**Location**: `troubleshooting/`

**Topics:**
- Troubleshoot clusters and nodes
- Troubleshoot cluster components
- Monitor cluster and application resource usage
- Manage and evaluate container output streams
- Troubleshoot services and networking

**Focus**: This is the highest-weighted domain. Spend significant time practicing troubleshooting scenarios.

### 2. Cluster Architecture, Installation & Configuration (25%) ⭐⭐⭐
**Location**: `cluster-architecture/`

**Topics:**
- Manage role based access control (RBAC)
- Prepare underlying infrastructure for installing a Kubernetes cluster
- Create and manage Kubernetes clusters using kubeadm
- Manage the lifecycle of Kubernetes clusters
- Implement and configure a highly-available control plane
- Use Helm and Kustomize to install cluster components
- Understand extension interfaces (CNI, CSI, CRI, etc.)
- Understand CRDs, install and configure operators

**Focus**: Second highest weight. Critical for understanding how Kubernetes works.

### 3. Services & Networking (20%) ⭐⭐
**Location**: `networking/`

**Topics:**
- Understand connectivity between Pods
- Define and enforce Network Policies
- Use ClusterIP, NodePort, LoadBalancer service types and endpoints
- Use the Gateway API to manage Ingress traffic
- Know how to use Ingress controllers and Ingress resources
- Understand and use CoreDNS

**Focus**: Networking is fundamental to Kubernetes operations.

### 4. Workloads & Scheduling (15%) ⭐⭐
**Location**: `workloads-scheduling/`

**Topics:**
- Understand application deployments and how to perform rolling update and rollbacks
- Use ConfigMaps and Secrets to configure applications
- Configure workload autoscaling
- Understand the primitives used to create robust, self-healing, application deployments
- Configure Pod admission and scheduling (limits, node affinity, etc.)

**Focus**: Core concepts for running applications on Kubernetes.

### 5. Storage (10%) ⭐
**Location**: `storage/`

**Topics:**
- Implement storage classes and dynamic volume provisioning
- Configure volume types, access modes and reclaim policies
- Manage persistent volumes and persistent volume claims

**Focus**: Smallest domain but still important for stateful applications.

## Study Strategy

1. **Start with highest weight**: Focus on Troubleshooting (30%) and Cluster Architecture (25%)
2. **Practice hands-on**: Use exercises in `../exercises/by-topic/` for each domain
3. **Review documentation**: Read domain-specific docs before practicing
4. **Track progress**: Mark topics as mastered as you progress

## Related Resources

- **Exercises**: `../exercises/by-topic/` - Practice exercises organized by domain
- **Labs**: `../exercises/labs/` - Hands-on lab scenarios
- **Templates**: `../templates/` - Kubernetes resource templates
- **Examples**: `../examples/` - Troubleshooting examples

---

**Note**: See `struct.md` in this directory for complete exam structure and requirements.
