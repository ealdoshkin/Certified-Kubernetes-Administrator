# Reference Materials

Quick reference guides and cheat sheets for CKA exam preparation.

## Contents

- `Quick-kubectl.md` - Quick kubectl command reference
- Domain-specific guides from CKA-Exercises

## Quick Access

### Essential kubectl Commands

```bash
# Generate YAML without creating
kubectl run pod-name --image=nginx --dry-run=client -o yaml

# Get resources with custom columns
kubectl get pods -o custom-columns=NAME:.metadata.name,STATUS:.status.phase

# Describe resource
kubectl describe pod <pod-name>

# Execute commands in pod
kubectl exec -it <pod-name> -- <command>

# View logs
kubectl logs <pod-name> -f

# Port forward
kubectl port-forward <pod-name> 8080:80
```

### Common Patterns

- **Dry-run**: Always use `--dry-run=client -o yaml` to generate templates
- **Custom columns**: Use `-o custom-columns=` for specific output
- **JSONPath**: Use `-o jsonpath='{.items[*].metadata.name}'` for scripting
- **Watch**: Use `-w` or `watch kubectl get pods` for real-time updates

## Documentation Access

During the exam, you have access to:
- [Kubernetes Official Documentation](https://kubernetes.io/docs/)
- [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)

**Tip**: Bookmark common pages and practice finding information quickly!
