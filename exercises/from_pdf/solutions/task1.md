# Solution for Task 1: Create Pod with Environment Variables

```bash
# 1. Create the pod
kubectl run nginx --image=nginx --restart=Never --env=var1=value1

# 2. Verify method 1: Check all environment variables
kubectl exec -it nginx -- env | grep var1

# 3. Verify method 2: Echo the variable
kubectl exec -it nginx -- sh -c 'echo $var1'

# 4. Verify method 3: Describe pod and grep
kubectl describe po nginx | grep value1
```
