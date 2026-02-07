# Task: Resource Quota

## Objective
Create and manage ResourceQuota to limit resource usage in namespaces.

## Solution

### Create Namespace
```bash
kubectl create namespace one
```

### Create ResourceQuota
```bash
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: ResourceQuota
metadata:
  name: my-rq
  namespace: one
spec:
  hard:
    requests.cpu: "1"
    requests.memory: 1Gi
    limits.cpu: "2"
    limits.memory: 2Gi
EOF
```

Or using imperative command:
```bash
kubectl create quota my-rq --namespace=one --hard=requests.cpu=1,requests.memory=1Gi,limits.cpu=2,limits.memory=2Gi
```

### Verify ResourceQuota
```bash
# Get ResourceQuota
kubectl get quota -n one

# Describe ResourceQuota
kubectl describe quota my-rq -n one
```

### Create Pod Within Quota
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  namespace: one
spec:
  containers:
  - image: nginx
    name: nginx
    resources:
      requests:
        cpu: "0.5"
        memory: 1Gi
      limits:
        cpu: "1"
        memory: 2Gi
```

### Attempt to Exceed Quota (Will Fail)
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-large
  namespace: one
spec:
  containers:
  - image: nginx
    name: nginx
    resources:
      requests:
        cpu: "2"  # exceeds quota
        memory: 3Gi  # exceeds quota
      limits:
        cpu: "3"  # exceeds quota
        memory: 4Gi  # exceeds quota
```

This will fail with error: "exceeded quota"

## Key Concepts
- **ResourceQuota**: Limits total resources in namespace
- **hard**: Enforced limits
- **requests.cpu/memory**: Total requests allowed
- **limits.cpu/memory**: Total limits allowed
- **Namespace-scoped**: Applies to entire namespace

## ResourceQuota Scopes
```yaml
spec:
  scopes:
  - BestEffort  # pods without requests
  - NotBestEffort  # pods with requests
  - Terminating  # pods with activeDeadlineSeconds
  - NotTerminating  # pods without activeDeadlineSeconds
```

## Verification
```bash
# List ResourceQuotas
kubectl get resourcequota -n one

# Describe ResourceQuota
kubectl describe resourcequota my-rq -n one

# Check quota usage
kubectl describe namespace one
```

## Use Cases
- Multi-tenant clusters
- Resource isolation
- Cost control
- Prevent resource exhaustion
