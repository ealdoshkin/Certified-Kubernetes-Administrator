# Solution for Task 2: List Pods with Custom Columns

```bash
# List pod with custom columns
kubectl get po nginx -o=custom-columns="POD_NAME:.metadata.name,POD_STATUS:.status.phase"
```
