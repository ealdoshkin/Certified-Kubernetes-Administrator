# Solution for Task 4: Deployment Rolling Update & Rollback

```bash
# 1. Create deployment
kubectl create deployment nginx-app --image=nginx:1.11.10-alpine --replicas=3

# 2. Verify deployment
kubectl get deployments
kubectl get pods -l app=nginx-app

# 3. Perform rolling update
kubectl set image deployment/nginx-app nginx=nginx:1.11.13-alpine

# 4. Check rollout status
kubectl rollout status deployment/nginx-app

# 5. Check history
kubectl rollout history deployment/nginx-app

# 6. Rollback to previous version
kubectl rollout undo deployment/nginx-app

# 7. Verify rollback
kubectl describe deployment nginx-app | grep Image
```
