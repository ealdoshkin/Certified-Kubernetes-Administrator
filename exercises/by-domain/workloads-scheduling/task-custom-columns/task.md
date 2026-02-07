# Task: Custom Columns Output

## Objective
List pods with custom column formatting using kubectl custom-columns.

## Requirements
- List nginx pod with custom columns: POD_NAME and POD_STATUS

## Solution

### Using Custom Columns
```bash
kubectl get po -o=custom-columns="POD_NAME:.metadata.name, POD_STATUS:.status.containerStatuses[].state"
```

### Alternative Format
```bash
kubectl get po -o custom-columns=POD_NAME:.metadata.name,POD_STATUS:.status.phase
```

## Key Concepts
- **custom-columns**: Define custom output columns
- **JSONPath**: Use JSONPath expressions to extract values
- **Column Names**: Custom names for output columns
- **Multiple Columns**: Separate multiple columns with commas

## Common Custom Column Examples

### Pod Name and Status
```bash
kubectl get po -o custom-columns=NAME:.metadata.name,STATUS:.status.phase
```

### Pod Name and Node
```bash
kubectl get po -o custom-columns=NAME:.metadata.name,NODE:.spec.nodeName
```

### Pod Name and IP
```bash
kubectl get po -o custom-columns=NAME:.metadata.name,IP:.status.podIP
```

### Deployment with Replicas
```bash
kubectl get deploy -o custom-columns=NAME:.metadata.name,READY:.status.readyReplicas,TOTAL:.spec.replicas
```

## Verification
```bash
# Test custom columns
kubectl get po -o custom-columns=NAME:.metadata.name,STATUS:.status.phase

# Compare with default output
kubectl get po
```

## Use Cases
- Custom reports
- Specific data extraction
- Formatted output for scripts
- Display only relevant information
