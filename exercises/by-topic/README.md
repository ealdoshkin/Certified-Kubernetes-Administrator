# Exercises by Topic

This directory contains exercises organized by CKA exam domains.

## Structure

```
by-topic/
├── troubleshooting/        # Troubleshooting (30% of exam)
├── cluster-architecture/   # Cluster Architecture, Installation & Configuration (25%)
├── networking/             # Services & Networking (20%)
├── workloads-scheduling/   # Workloads & Scheduling (15%)
└── storage/                # Storage (10%)
```

## Exam Domain Breakdown

### 1. Troubleshooting (30%)
**Location**: `troubleshooting/`

- Troubleshoot clusters and nodes
- Troubleshoot cluster components
- Monitor cluster and application resource usage
- Manage and evaluate container output streams
- Troubleshoot services and networking

### 2. Cluster Architecture, Installation & Configuration (25%)
**Location**: `cluster-architecture/`

- Manage role based access control (RBAC)
- Prepare underlying infrastructure for installing a Kubernetes cluster
- Create and manage Kubernetes clusters using kubeadm
- Manage the lifecycle of Kubernetes clusters
- Implement and configure a highly-available control plane
- Use Helm and Kustomize to install cluster components
- Understand extension interfaces (CNI, CSI, CRI, etc.)
- Understand CRDs, install and configure operators

### 3. Services & Networking (20%)
**Location**: `networking/`

- Understand connectivity between Pods
- Define and enforce Network Policies
- Use ClusterIP, NodePort, LoadBalancer service types and endpoints
- Use the Gateway API to manage Ingress traffic
- Know how to use Ingress controllers and Ingress resources
- Understand and use CoreDNS

### 4. Workloads & Scheduling (15%)
**Location**: `workloads-scheduling/`

- Understand application deployments and how to perform rolling update and rollbacks
- Use ConfigMaps and Secrets to configure applications
- Configure workload autoscaling
- Understand the primitives used to create robust, self-healing, application deployments
- Configure Pod admission and scheduling (limits, node affinity, etc.)

### 5. Storage (10%)
**Location**: `storage/`

- Implement storage classes and dynamic volume provisioning
- Configure volume types, access modes and reclaim policies
- Manage persistent volumes and persistent volume claims

## How to Use

1. **Start with your weakest domain** - Focus more time on areas you're less confident
2. **Work through exercises systematically** - Each directory contains README files with exercises
3. **Practice hands-on** - Don't just read, actually run the commands
4. **Review solutions** - Compare your approach with provided solutions
5. **Repeat difficult exercises** - Mastery comes from repetition

## Study Strategy

- **Week 1-2**: Focus on Troubleshooting (30%) - Highest weight
- **Week 3**: Cluster Architecture (25%) - Second highest
- **Week 4**: Networking (20%) and Workloads (15%)
- **Week 5**: Storage (10%) and Review all topics
- **Week 6**: Practice exams and final review

---

**Remember**: The exam is hands-on. Reading alone isn't enough - you must practice!
