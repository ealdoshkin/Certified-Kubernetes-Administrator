# CKA Lab Exercises

This directory contains hands-on lab exercises for CKA exam preparation.

## Structure

```
labs/
├── tasks/          # Lab task descriptions (25 tasks)
├── solutions/      # Solutions for all tasks
└── README.md       # This file
```

## Lab Setup

You can create a 1 master and 2 worker node cluster with kubeadm:

- [Kubeadm Installation Guide](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)
- [Play with Kubernetes](https://labs.play-with-k8s.com/) - Quick testing environment

## Lab Tasks

There are **25 lab tasks** covering all CKA exam domains:

### Troubleshooting (30%)
- Task 1-5: Basic troubleshooting scenarios
- Task 6-10: Cluster and node troubleshooting
- Task 11-15: Service and networking troubleshooting

### Cluster Architecture & Configuration (25%)
- Task 16-18: RBAC and cluster configuration
- Task 19-20: Cluster maintenance and upgrades

### Services & Networking (20%)
- Task 21-22: Services and networking configuration

### Workloads & Scheduling (15%)
- Task 23-24: Deployment and scheduling

### Storage (10%)
- Task 25: Persistent volumes and storage

## How to Use

1. **Read the task** in `tasks/TaskN/task.md`
2. **Attempt the solution** on your own
3. **Compare with solution** in `solutions/TaskN/solution/` (if available)
4. **Practice multiple times** until you can complete without referring to solutions

## Tips

- ⚠️ **Try solving on your own first** - Don't peek at solutions immediately
- 🔄 **Practice repeatedly** - Repetition builds muscle memory
- 📝 **Take notes** - Document commands and patterns that work
- ⏱️ **Time yourself** - Practice completing tasks within exam time limits
- 🎯 **Focus on weak areas** - Spend more time on domains you find challenging

## Task List

| Task | Topic | Difficulty |
|------|-------|------------|
| Task 1 | Storage (PVC) | Beginner |
| Task 2 | Pods & ConfigMaps | Beginner |
| Task 3 | Deployments | Intermediate |
| Task 4 | Services | Intermediate |
| Task 5 | Ingress | Intermediate |
| Task 6-25 | Various CKA Topics | Intermediate-Advanced |

---

**Note**: These are practice scenarios, not actual exam questions. Use them to build confidence and familiarity with Kubernetes operations.
