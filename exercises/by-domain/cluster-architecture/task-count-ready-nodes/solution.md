# Task: Count Ready Worker Nodes

## Solution

### Method 1: Using kubectl and jq
```bash
# Get ready nodes without NoSchedule taint
kubectl get nodes -o json | \
  jq -r '.items[] | select(.status.conditions[] | select(.type=="Ready" and .status=="True")) | select(.spec.taints[]? | select(.effect=="NoSchedule") | not) | .metadata.name' | \
  wc -l > /opt/KUCC00104/kucc00104.txt
```

### Method 2: Using kubectl and grep
```bash
# Get ready nodes
kubectl get nodes --no-headers | \
  grep -v "NoSchedule" | \
  grep "Ready" | \
  wc -l > /opt/KUCC00104/kucc00104.txt
```

### Method 3: Using JSONPath
```bash
# Count ready nodes without NoSchedule taint
kubectl get nodes -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.conditions[?(@.type=="Ready")].status}{"\t"}{.spec.taints[*].effect}{"\n"}{end}' | \
  grep -v "NoSchedule" | \
  grep "True" | \
  wc -l > /opt/KUCC00104/kucc00104.txt
```

## Key Concepts
- **Node Status**: Check Ready condition
- **Taints**: Node taints affect scheduling
- **NoSchedule**: Taint that prevents pod scheduling
- **Worker Nodes**: Non-control-plane nodes

## Verification
```bash
# Check node status
kubectl get nodes

# Check node taints
kubectl describe nodes | grep -i taint

# Verify count
cat /opt/KUCC00104/kucc00104.txt

# Manual count
kubectl get nodes --no-headers | grep Ready | grep -v "NoSchedule" | wc -l
```

## Important Notes
- Only count Ready nodes
- Exclude nodes with NoSchedule taint
- Control plane nodes may have NoSchedule taint
- Count only worker nodes (not control-plane)
