# Task: Taints and Tolerations

## Objective
Control pod scheduling using node taints and pod tolerations.

## Task 1: Taint a Node
```bash
# Taint node with NoSchedule effect
kubectl taint node node1 tier=frontend:NoSchedule

# View taints
kubectl describe node node1 | grep -i taint
```

## Task 2: Create Pod with Toleration
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: frontend
spec:
  containers:
  - name: nginx
    image: nginx
  tolerations:
  - key: "tier"
    operator: "Equal"
    value: "frontend"
    effect: "NoSchedule"
```

## Task 3: Taint Control Plane Node
```bash
# Control plane nodes are typically tainted
kubectl taint node controlplane node-role.kubernetes.io/control-plane:NoSchedule

# Create pod with toleration for control plane
kubectl create pod --image=nginx --restart=Never --dry-run=client -o yaml > pod.yaml
```

Edit pod.yaml:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: frontend
spec:
  containers:
  - name: nginx
    image: nginx
  nodeSelector:
    kubernetes.io/hostname: controlplane
  tolerations:
  - key: "node-role.kubernetes.io/control-plane"
    operator: "Exists"
    effect: "NoSchedule"
```

## Taint Effects
- **NoSchedule**: Pods without toleration won't be scheduled
- **PreferNoSchedule**: Prefer not to schedule (soft)
- **NoExecute**: Evict existing pods without toleration

## Toleration Operators
- **Equal**: Key and value must match
- **Exists**: Key must exist (value ignored)

## Task 4: Remove Taint
```bash
# Remove taint
kubectl taint node node1 tier=frontend:NoSchedule-
```

## Key Concepts
- **Taint**: Node property that repels pods
- **Toleration**: Pod property that allows scheduling on tainted nodes
- **Effect**: What happens to pods without toleration
- **Operator**: How to match taint key/value

## Verification
```bash
# Check node taints
kubectl describe node node1 | grep -i taint

# Check pod tolerations
kubectl get pod <pod-name> -o yaml | grep -A 5 tolerations

# Verify pod placement
kubectl get pod <pod-name> -o wide
```

## Common Use Cases
- Dedicated nodes for specific workloads
- Control plane isolation
- Maintenance mode
- Specialized hardware
