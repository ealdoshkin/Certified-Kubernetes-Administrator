# Task: Node Affinity

## Objective
Schedule pods on specific nodes using node affinity.

## Task 1: Label Node
```bash
# Add label to node
kubectl label nodes <node-name> accelerator=nvidia-tesla-p100

# Verify label
kubectl get nodes --show-labels
```

## Task 2: Create Pod with nodeSelector
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: cuda-test
spec:
  containers:
  - name: cuda-test
    image: k8s.gcr.io/cuda-vector-add:v0.1
  nodeSelector:
    accelerator: nvidia-tesla-p100
```

## Task 3: Create Pod with Node Affinity (Required)
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: affinity-pod
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: accelerator
            operator: In
            values:
            - nvidia-tesla-p100
  containers:
  - name: app
    image: nginx
```

## Task 4: Create Pod with Preferred Node Affinity
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: preferred-affinity-pod
spec:
  affinity:
    nodeAffinity:
      preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 100
        preference:
          matchExpressions:
          - key: accelerator
            operator: In
            values:
            - nvidia-tesla-p100
  containers:
  - name: app
    image: nginx
```

## Key Concepts
- **nodeSelector**: Simple node selection (key=value)
- **nodeAffinity**: Advanced node selection
- **requiredDuringScheduling**: Must match (hard requirement)
- **preferredDuringScheduling**: Should match (soft requirement)
- **matchExpressions**: Match using operators (In, NotIn, Exists, DoesNotExist)

## Operators
- **In**: Value in list
- **NotIn**: Value not in list
- **Exists**: Key exists
- **DoesNotExist**: Key doesn't exist
- **Gt**: Greater than (for numeric values)
- **Lt**: Less than (for numeric values)

## Verification
```bash
# Check node labels
kubectl get nodes --show-labels

# Check pod placement
kubectl get pod <pod-name> -o wide

# Describe pod to see affinity
kubectl describe pod <pod-name> | grep -i affinity
```

## Use Cases
- GPU workloads
- Specialized hardware
- Zone/region placement
- Node type selection
