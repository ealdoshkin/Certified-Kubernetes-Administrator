# Task: Deployment Rollout Management

## Objective
Create, update, and manage deployment rollouts.

## Task 1: Create Deployment
```bash
kubectl create deployment nginx --image=nginx:1.18.0 --replicas=2 --port=80
# or
kubectl create deployment nginx --image=nginx:1.18.0 --dry-run=client -o yaml > deploy.yaml
# Edit deploy.yaml to set replicas: 2 and add containerPort: 80
kubectl apply -f deploy.yaml
```

## Task 2: View Deployment Details
```bash
# View deployment YAML
kubectl get deploy nginx -o yaml

# View replica set
kubectl get rs -l app=nginx
kubectl get rs <rs-name> -o yaml

# View pods
kubectl get po -l app=nginx
kubectl get po <pod-name> -o yaml

# Check rollout status
kubectl rollout status deploy nginx
```

## Task 3: Update Deployment Image
```bash
# Update image
kubectl set image deploy nginx nginx=nginx:1.19.8
# or
kubectl edit deploy nginx  # change image in .spec.template.spec.containers[0].image

# Check rollout
kubectl rollout status deploy nginx
kubectl get rs  # new replica set created
kubectl get po  # new pods created
```

## Task 4: View Rollout History
```bash
# View history
kubectl rollout history deploy nginx

# View specific revision
kubectl rollout history deploy nginx --revision=2
```

## Task 5: Rollback Deployment
```bash
# Undo latest rollout
kubectl rollout undo deploy nginx

# Rollback to specific revision
kubectl rollout undo deploy nginx --to-revision=2

# Verify rollback
kubectl get po
kubectl describe po <pod-name> | grep -i image  # should show old image
```

## Task 6: Pause and Resume Rollout
```bash
# Pause rollout
kubectl rollout pause deploy nginx

# Update image (won't trigger rollout while paused)
kubectl set image deploy nginx nginx=nginx:1.19.9
kubectl get rs  # no new replica set

# Resume rollout
kubectl rollout resume deploy nginx
kubectl rollout status deploy nginx  # rollout happens now
```

## Key Concepts
- **Rollout**: Process of updating deployment
- **Rolling Update**: Default strategy (gradual replacement)
- **ReplicaSet**: Manages pod replicas
- **Revision**: Each rollout creates a new revision
- **Pause/Resume**: Control when rollout happens

## Verification
```bash
# Check deployment status
kubectl get deploy nginx

# Check replica sets
kubectl get rs -l app=nginx

# Check pods
kubectl get po -l app=nginx

# View rollout history
kubectl rollout history deploy nginx
```
