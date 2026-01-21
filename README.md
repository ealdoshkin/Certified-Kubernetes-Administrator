# Certified Kubernetes Administrator (CKA) Study Repository

This repository contains study materials, exercises, templates, and resources for preparing for the Certified Kubernetes Administrator (CKA) exam.

## 📚 Repository Structure

```
.
├── README.md                 # This file
├── domains/                  # Documentation organized by CKA exam domains
│   ├── troubleshooting/     # 30% of exam
│   ├── cluster-architecture/ # 25% of exam
│   ├── networking/          # 20% of exam
│   ├── workloads-scheduling/ # 15% of exam
│   └── storage/             # 10% of exam
├── docs/                     # General documentation and study guides
├── books/                    # Study books and PDFs
├── templates/                # Kubernetes resource templates
├── exercises/                # Practice exercises and labs
├── examples/                 # Example manifests and troubleshooting cases
├── tools/                    # Tool documentation (bash, jq, yq, vim, tmux)
├── cheatsheets/              # Quick reference commands
├── scripts/                  # Installation and utility scripts
└── tasks/                    # Study tasks and notes
```

## 📖 Exam Information

- **Kubernetes Version**: v1.34
- **Duration**: 2 hours
- **Questions**: ~17 questions (can be solved in any order)
- **Pass Mark**: 66%
- **Retakes**: 1 free retake if you don't pass on your first try
- **Browser**: Chrome required
- **Environment**: Remote-proctored (webcam and microphone required)
- **ID Required**: Government-issued ID or passport

### Exam domains

1. **Troubleshooting** - 30%

   - Troubleshoot clusters and nodes
   - Troubleshoot cluster components
   - Monitor cluster and application resource usage
   - Manage and evaluate container output streams
   - Troubleshoot services and networking

2. **Cluster Architecture, Installation & Configuration** - 25%

   - Manage role based access control (RBAC)
   - Prepare underlying infrastructure for installing a Kubernetes cluster
   - Create and manage Kubernetes clusters using kubeadm
   - Manage the lifecycle of Kubernetes clusters
   - Implement and configure a highly-available control plane
   - Use Helm and Kustomize to install cluster components
   - Understand extension interfaces (CNI, CSI, CRI, etc.)
   - Understand CRDs, install and configure operators

3. **Services & Networking** - 20%

   - Understand connectivity between Pods
   - Define and enforce Network Policies
   - Use ClusterIP, NodePort, LoadBalancer service types and endpoints
   - Use the Gateway API to manage Ingress traffic
   - Know how to use Ingress controllers and Ingress resources
   - Understand and use CoreDNS

4. **Workloads & Scheduling** - 15%

   - Understand application deployments and how to perform rolling update and rollbacks
   - Use ConfigMaps and Secrets to configure applications
   - Configure workload autoscaling
   - Understand the primitives used to create robust, self-healing, application deployments
   - Configure Pod admission and scheduling (limits, node affinity, etc.)

5. **Storage** - 10%
   - Implement storage classes and dynamic volume provisioning
   - Configure volume types, access modes and reclaim policies
   - Manage persistent volumes and persistent volume claims

## 🔗 Useful Links

- [PSI System Check](https://syscheck.bridge.psiexams.com/)
- [CKA Resource List](https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/)
- [Killer.sh Practice Environment](https://killer.sh/) - 2 attempts available (36 hours after activation)

## 📝 Study Tips

- Practice on weekday schedule (exam is typically on weekdays)
- Allow 30-35 minutes to connect to exam environment
- Have passport/government ID ready
- Review all domains, with focus on Troubleshooting (30%) and Cluster Architecture (25%)

## 🚀 Getting Started

1. **Review exam domains** in `domains/` - Start with highest weight domains (Troubleshooting 30%, Cluster Architecture 25%)
2. **Study domain documentation** - Each domain has detailed README with topics and commands
3. **Practice with exercises** in `exercises/` - Organized by domain in `exercises/by-topic/`
4. **Complete lab tasks** in `exercises/labs/` - 25 hands-on scenarios
5. **Study the books** in `books/` - Comprehensive study materials
6. **Use templates** in `templates/` - Quick resource creation
7. **Reference cheatsheets** in `cheatsheets/` - Common commands
8. **Review examples** in `examples/` - Troubleshooting scenarios

## 📂 Directory Details

- **domains/**: Documentation organized by CKA exam domains (30%, 25%, 20%, 15%, 10%)
  - Each domain contains README with topics, key commands, and study tips
  - domain-specific documentation and guides
- **docs/**: General documentation and study guides
- **books/**: PDF study materials and books
- **templates/**: Base Kubernetes resource YAML templates
- **exercises/**: Practice labs and exercises organized by domain
  - `labs/` - 25 hands-on lab tasks with solutions
  - `practice-exams/` - Practice exam questions
  - `by-topic/` - Exercises organized by exam domains
- **examples/**: Example manifests and error troubleshooting cases
- **tools/**: Documentation for useful tools (bash, jq, yq, vim, tmux)
- **cheatsheets/**: Quick reference commands and shortcuts
- **scripts/**: Installation scripts and utilities
- **tasks/**: Personal study tasks and notes

---

Good luck with your CKA exam preparation! 🎯
