# Task: Sort Resources

## Objective
List and sort Kubernetes resources using kubectl's built-in sorting functionality.

## Task 1: Sort Pods by Name
```bash
kubectl get pods --sort-by=.metadata.name
```

## Task 2: Sort PersistentVolumes by Capacity
```bash
# Sort PVs by capacity and save to file
kubectl get pv --sort-by=.spec.capacity.storage > /opt/KUCC00102/volume_list
```

## Key Concepts
- **--sort-by**: Sort resources by specified field
- **JSONPath**: Use JSONPath to specify sort field
- **Built-in Sorting**: Use kubectl's native sorting (don't manipulate output)

## Common Sort Examples

### Sort Pods by Creation Time
```bash
kubectl get pods --sort-by=.metadata.creationTimestamp
```

### Sort Nodes by Name
```bash
kubectl get nodes --sort-by=.metadata.name
```

### Sort Deployments by Replicas
```bash
kubectl get deploy --sort-by=.spec.replicas
```

### Sort Services by Name
```bash
kubectl get svc --sort-by=.metadata.name
```

## Verification
```bash
# Sort pods by name
kubectl get pods --sort-by=.metadata.name

# Sort PVs by capacity
kubectl get pv --sort-by=.spec.capacity.storage

# Verify sorted output
kubectl get pv --sort-by=.spec.capacity.storage -o yaml > /opt/KUCC00102/volume_list
```

## Important Notes
- Use kubectl's built-in sorting (--sort-by)
- Don't use external tools like sort or awk
- JSONPath expressions for sort fields
- Works with all resource types
