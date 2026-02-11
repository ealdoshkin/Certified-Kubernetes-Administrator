# Solution for Task 10: List Pods with JSONPath

```bash
# Method 1: Using JSONPath template with header
kubectl get pods -A -o=jsonpath='{"NAME\tNAMESPACE\n"}{range .items[*]}{.metadata.name}{"\t"}{.metadata.namespace}{"\n"}{end}'

# Method 2: Alternative JSONPath (without header)
kubectl get pods -A -o=jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.metadata.namespace}{"\n"}{end}'

# Method 3: Using custom columns (alternative approach)
kubectl get pods -A -o custom-columns=NAME:.metadata.name,NAMESPACE:.metadata.namespace
```

These commands will list all pods across all namespaces with their names and namespaces. The first method includes a header row, while the second one doesn't. The third method shows an alternative approach using custom columns.
