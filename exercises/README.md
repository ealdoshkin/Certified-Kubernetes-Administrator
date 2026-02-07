# CKA Practice Exercises

This directory contains practice exercises and labs organized for effective CKA exam preparation.

## 📁 Directory Structure

```
exercises/
├── by-domain/              # Exercises organized by CKA exam domains ⭐ RECOMMENDED
│   ├── storage/           # 10% - 3 tasks
│   ├── cluster-architecture/ # 25% - 5 tasks
│   ├── networking/       # 20% - 3 tasks
│   ├── workloads-scheduling/ # 15% - 8 tasks
│   └── troubleshooting/  # 30% - 4 tasks
├── cka-lab/              # Original 25 lab tasks (for reference)
├── practice-exams/       # Practice exam questions
├── CKAD-exercises/       # CKAD exercises (additional practice)
├── 1/                    # Domain-specific exercises
├── 2/                    # Additional exercises by topic
└── tasks/                # Study tasks and notes
```

## 🎯 Recommended Study Path

### Start Here: `by-domain/` ⭐

**Organized by exam domains with comprehensive coverage:**
- 88 organized tasks total
  - 23 from cka-lab (original lab tasks)
  - 16 from exercises/1/ (domain-specific exercises)
  - 19 from exercises/2/ (security, networking, secrets)
  - 17 from CKAD-exercises/ (ConfigMaps, Deployments, Jobs, Probes, Storage)
  - 13 from practice-exams/ (Init containers, DaemonSet, DNS, etcd, kubeadm, troubleshooting)
- Clear domain categorization
- Each domain has README with task descriptions
- YAML example files included for reference
- No duplicate or similar tasks

### Domain Priority

1. **Troubleshooting (30%)** - Start here! Highest weight
   - 4 tasks covering logging, node issues, debugging
   
2. **Cluster Architecture (25%)** - Second priority
   - 5 tasks covering RBAC, upgrades, backups, etcd

3. **Networking (20%)** - Important
   - 3 tasks covering services, ingress, network policies

4. **Workloads & Scheduling (15%)** - Core concepts
   - 8 tasks covering deployments, pods, scheduling

5. **Storage (10%)** - Smallest domain
   - 3 tasks covering PVs, PVCs, storage classes

## 📚 Other Resources

### `cka-lab/`
Original 25 lab tasks. Use for reference, but `by-domain/` is better organized.

### `practice-exams/`
Practice exam questions converted from PDFs:
- cka_0.md through cka_8.md
- CKAD.md

### `CKAD-exercises/`
CKAD exercises useful for CKA preparation:
- Core concepts
- Pod design
- Configuration
- Observability
- State persistence

## 🚀 How to Use

1. **Start with `by-domain/troubleshooting/`** - 30% of exam
2. **Move to `by-domain/cluster-architecture/`** - 25% of exam
3. **Complete remaining domains** - Based on your weak areas
4. **Take practice exams** - Simulate real exam conditions
5. **Review solutions** - Compare your approach

## 💡 Study Tips

- **Practice hands-on**: Don't just read, actually complete tasks
- **Time yourself**: Practice completing tasks within time limits
- **Review solutions**: Learn from provided solutions
- **Repeat difficult tasks**: Mastery comes from repetition
- **Focus on high-weight domains**: Troubleshooting and Cluster Architecture

## 📊 Task Summary

| Domain | Weight | Tasks | Priority |
|--------|--------|-------|----------|
| Troubleshooting | 30% | 16 | ⭐⭐⭐ |
| Cluster Architecture | 25% | 24 | ⭐⭐⭐ |
| Networking | 20% | 12 | ⭐⭐ |
| Workloads & Scheduling | 15% | 32 | ⭐⭐ |
| Storage | 10% | 6 | ⭐ |
| **Total** | **100%** | **88** | |

---

**Note**: Tasks in `by-domain/` are organized and deduplicated. Original tasks remain in `cka-lab/` for reference.
