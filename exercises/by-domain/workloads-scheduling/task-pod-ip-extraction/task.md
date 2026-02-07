# Task: Extract Pod IP Address

## Objective
Get the IP address of a pod using different methods.

## Solution

### Method 1: Using -o wide
```bash
kubectl get po nginx-dev -o wide
```

### Method 2: Using JSONPath
```bash
kubectl get pods -o=jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.podIP}{"\n"}{end}'
```

### Method 3: Get Specific Pod IP
```bash
kubectl get pod nginx-dev -o jsonpath='{.status.podIP}'
```

### Method 4: Using Custom Columns
```bash
kubectl get po -o custom-columns=NAME:.metadata.name,IP:.status.podIP
```

## Key Concepts
- **podIP**: IP address assigned to pod
- **JSONPath**: Extract specific fields from JSON
- **-o wide**: Shows additional columns including IP
- **Range**: Iterate over multiple items

## Extract IP for Multiple Pods
```bash
# All pods with IPs
kubectl get pods -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.podIP}{"\n"}{end}'

# Filter by label
kubectl get pods -l app=nginx -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.podIP}{"\n"}{end}'
```

## Verification
```bash
# Get pod IP
kubectl get pod nginx-dev -o jsonpath='{.status.podIP}'

# Compare with -o wide
kubectl get pod nginx-dev -o wide

# Verify IP is valid
kubectl get pod nginx-dev -o jsonpath='{.status.podIP}' | grep -E '^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$'
```

## Use Cases
- Network troubleshooting
- Service connectivity testing
- Pod-to-pod communication
- Debugging network issues
