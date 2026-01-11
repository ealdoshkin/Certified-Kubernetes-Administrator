# CKA Practice Exercises & Labs

This directory contains comprehensive practice materials organized for effective CKA exam preparation.

## 📁 Directory Structure

```
exercises/
├── labs/                    # Hands-on lab exercises (25 tasks)
│   ├── tasks/              # Lab task descriptions
│   └── solutions/         # Solutions for all tasks
│
├── practice-exams/         # Practice exam questions (converted from PDFs)
│   ├── cka_0.md
│   ├── cka_1.md
│   ├── cka_4.md
│   ├── cka_6.md
│   ├── cka_8.md
│   └── CKAD.md
│
├── by-topic/              # Exercises organized by CKA exam domains
│   ├── troubleshooting/   # 30% of exam
│   ├── cluster-architecture/  # 25% of exam
│   ├── networking/        # 20% of exam
│   ├── workloads-scheduling/  # 15% of exam
│   └── storage/          # 10% of exam
│
└── reference/            # Quick reference guides and cheat sheets
```

## 🎯 Recommended Study Path

### Phase 1: Foundation (Weeks 1-2)
1. **Start with `by-topic/`** - Learn concepts by domain
   - Begin with `workloads-scheduling/core-concepts/` for basics
   - Progress through each domain systematically

2. **Practice with `labs/`** - Apply what you learned
   - Complete tasks 1-10 (beginner to intermediate)
   - Try solving without looking at solutions first

### Phase 2: Advanced Practice (Weeks 3-4)
1. **Continue with `labs/`** - Complete all 25 tasks
   - Focus on troubleshooting tasks (highest exam weight)
   - Practice cluster architecture scenarios

2. **Deep dive into `by-topic/`** - Strengthen weak areas
   - Review exercises in your weakest domain
   - Practice until you're comfortable

### Phase 3: Exam Simulation (Weeks 5-6)
1. **Take `practice-exams/`** - Simulate real exam conditions
   - Set 2-hour timer
   - Use only allowed resources
   - Complete multiple practice exams

2. **Final review** - Go through `reference/` materials
   - Memorize common kubectl patterns
   - Review quick reference guides

## 📊 Exam Domain Focus

| Domain | Weight | Priority | Location |
|------|--------|----------|----------|
| Troubleshooting | 30% | ⭐⭐⭐ | `by-topic/troubleshooting/`, `labs/tasks/` |
| Cluster Architecture | 25% | ⭐⭐⭐ | `by-topic/cluster-architecture/` |
| Networking | 20% | ⭐⭐ | `by-topic/networking/` |
| Workloads & Scheduling | 15% | ⭐⭐ | `by-topic/workloads-scheduling/` |
| Storage | 10% | ⭐ | `by-topic/storage/` |

## 🛠️ Lab Setup

### Option 1: Local Cluster (Recommended)
```bash
# Create cluster with kubeadm
# Follow: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/
```

### Option 2: Online Labs
- [Play with Kubernetes](https://labs.play-with-k8s.com/) - Free, temporary clusters
- [Killer.sh](https://killer.sh/) - CKA practice environment (paid)

### Option 3: Cloud Providers
- AWS EKS, GCP GKE, Azure AKS (free tier available)

## 📚 Additional Resources

### Original Exercise Sources
- `CKA-study-guide-exercises/` - Comprehensive study guide (organized in `by-topic/`)
- `CKA-Exercises/` - Domain-specific exercises (reference materials)
- `CKAD-exercises/` - CKAD exercises (useful for CKA prep)
- `CKA-Certified-Kubernetes-Administrator/` - Certification materials

### Quick Links
- [CKA Exam Information](https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)

## 💡 Study Tips

1. **Practice Daily** - Consistency beats intensity
2. **Time Yourself** - Practice completing tasks within time limits
3. **Use Documentation** - Familiarize yourself with kubernetes.io/docs
4. **Take Notes** - Document patterns and commands that work
5. **Review Mistakes** - Learn from errors, don't just move on
6. **Simulate Exam** - Practice in exam-like conditions regularly

## 🎓 Exam Day Checklist

- [ ] Chrome browser installed
- [ ] Webcam and microphone working
- [ ] Government ID ready
- [ ] Quiet environment prepared
- [ ] System check completed (PSI Bridge)
- [ ] kubectl commands memorized
- [ ] Documentation bookmarks ready

---

**Good luck with your CKA exam preparation!** 🚀

Remember: The exam is hands-on. Reading isn't enough - you must practice!
