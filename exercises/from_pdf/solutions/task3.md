# Solution for Task 3: Create Pod in New Namespace

```bash
# 1. Create namespace
kubectl create namespace my-website

# 2. Create pod in the namespace
kubectl run mongo --image=mongo --restart=Never -n my-website

# 3. Verify
kubectl get pods -n my-website
```
