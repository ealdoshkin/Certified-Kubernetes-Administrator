# CKA Exam Changes - Effective February 18, 2025

*Converted from cka-exam-changes-feb18-2025.pdf*

---

## Exam Weight Distribution
- **25%** - Cluster Architecture, Installation, and Configuration
- **15%** - Workloads and Scheduling
- **20%** - Services and Networking
- **10%** - Storage
- **30%** - Troubleshooting

---

## 1. Cluster Architecture, Installation, and Configuration (25%)

### Before November 25
- Manage role-based access control (RBAC)
- Implement and configure a highly-available control plane
- Use Kubeadm to install a basic cluster
- Prepare underlying infrastructure for installing a Kubernetes cluster
- Manage a highly-available Kubernetes cluster
- Create and manage Kubernetes clusters using kubeadm
- Provision underlying infrastructure to deploy a Kubernetes cluster
- Use Helm and Kustomize to install cluster components
- Perform a version upgrade on a Kubernetes cluster using Kubeadm
- Implement etcd backup and restore

### On or After February 18
- Manage role-based access control (RBAC)
- Manage the lifecycle of Kubernetes clusters
- Use Kubeadm to install a basic cluster
- Understand extension interfaces (CNI, CSI, CRI, etc.)
- Understand CRDs, install and configure operators

---

## 2. Workloads and Scheduling (15%)

### Before November 25
- Understand deployments and how to perform rolling update and rollbacks
- Use ConfigMaps and Secrets to configure applications
- Know how to scale applications
- Understand the primitives used to create robust, self-healing, application deployments
- Understand how resource limits can affect Pod scheduling
- Awareness of manifest management and common templating tools

### On or After February 18
- Understand application deployments and how to perform rolling update and rollbacks
- Use ConfigMaps and Secrets to configure applications
- Configure workload autoscaling
- Understand the primitives used to create robust, self-healing, application deployments
- Configure Pod admission and scheduling (limits, node affinity, etc.)

---

## 3. Services and Networking (20%)

### Before November 25
- Understand host networking configuration on the cluster nodes
- Understand connectivity between Pods
- Use ClusterIP, NodePort, LoadBalancer service types and endpoints
- Know how to use Ingress controllers and Ingress resources
- Know how to configure and use CoreDNS
- Choose an appropriate container network interface plugin

### On or After February 18
- Understand connectivity between Pods
- Define and enforce Network Policies
- Understand ClusterIP, NodePort, LoadBalancer service types and endpoints
- Use the Gateway API to manage Ingress traffic
- Know how to use Ingress controllers and Ingress resources
- Understand and use CoreDNS

---

## 4. Storage (10%)

### Before February 10
- Understand storage classes, persistent volumes
- Understand volume mode, access modes and reclaim policies for volumes
- Understand persistent volume claims primitive
- Know how to configure applications with persistent storage

### On or After February 18
- Implement storage classes and dynamic volume provisioning
- Configure volume types, access modes and reclaim policies
- Manage persistent volumes and persistent volume claims

---

## 5. Troubleshooting (30%)

### Before November 25
- Evaluate cluster and node logging
- Understand how to monitor applications
- Manage container stdout & stderr logs
- Troubleshoot application failure
- Troubleshoot cluster component failure
- Troubleshoot networking

### On or After February 18
- Implement storage classes and dynamic volume provisioning
- Configure volume types, access modes and reclaim policies
- Manage persistent volumes and persistent volume claims

---

**Note**: The storage-related troubleshooting objectives appear to be duplicated under the Troubleshooting section in the new exam format. Focus on these storage troubleshooting skills for the 30% weight.
