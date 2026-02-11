# Solution for Task 11: Check Image Version without Describe

```bash
# 1. Create test pod if needed
kubectl run nginx --image=nginx:1.14.2 --restart=Never

# 2. Check image version using JSONPath (recommended)
kubectl get pod nginx -o jsonpath='{.spec.containers[0].image}'

# 3. Alternative using yq (if installed)
kubectl get pod nginx -o yaml | yq '.spec.containers[0].image'

# 4. Using jq (if installed)
kubectl get pod nginx -o json | jq -r '.spec.containers[0].image'
```

These commands will output the full image name and tag (e.g., `nginx:1.14.2`) without using `kubectl describe`. The first method using JSONPath is the most straightforward if you just need the image name.
