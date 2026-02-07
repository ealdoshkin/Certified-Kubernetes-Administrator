# Task: Deployment Rollback and Troubleshooting

## Objective
Handle failed rollouts and rollback to previous versions.

## Task 1: Simulate Failed Rollout
```bash
# Update with wrong image
kubectl set image deploy nginx nginx=nginx:1.91
# or
kubectl edit deploy nginx  # change image to nginx:1.91
```

## Task 2: Verify Failed Rollout
```bash
# Check rollout status
kubectl rollout status deploy nginx  # will hang or show error

# Check pods
kubectl get po  # will show 'ErrImagePull' or 'ImagePullBackOff'

# Check events
kubectl get events | grep -i error
```

## Task 3: Rollback to Previous Version
```bash
# Undo to previous revision
kubectl rollout undo deploy nginx

# Verify rollback
kubectl get po
kubectl describe po <pod-name> | grep -i image  # should show previous working image
```

## Task 4: Rollback to Specific Revision
```bash
# View history
kubectl rollout history deploy nginx

# View specific revision details
kubectl rollout history deploy nginx --revision=2

# Rollback to specific revision
kubectl rollout undo deploy nginx --to-revision=2

# Verify
kubectl get po
kubectl describe po <pod-name> | grep -i image
```

## Task 5: Check Revision Details
```bash
# List all revisions
kubectl rollout history deploy nginx

# View specific revision
kubectl rollout history deploy nginx --revision=4
```

## Key Concepts
- **Rollback**: Revert to previous deployment version
- **Revision**: Each rollout creates a new revision
- **Failed Rollout**: Image pull errors, container crashes
- **Rollout History**: Track all deployment changes
- **Revision Number**: Sequential number for each rollout

## Common Rollout Issues
- **ErrImagePull**: Image doesn't exist or wrong name
- **ImagePullBackOff**: Retrying failed image pull
- **CrashLoopBackOff**: Container crashes immediately
- **Invalid Image**: Wrong image tag or format

## Verification
```bash
# Check deployment
kubectl get deploy nginx

# Check replica sets
kubectl get rs -l app=nginx

# Check pods
kubectl get po -l app=nginx

# Check rollout history
kubectl rollout history deploy nginx
```

## Best Practices
- Test images before deploying
- Use semantic versioning
- Keep rollout history
- Monitor rollout status
- Have rollback plan ready
