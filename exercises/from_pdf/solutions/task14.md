# Solution for Task 14: Schedule Pod with Node Selector

## Method 1: Using `kubectl run` with `--overrides`

```bash
# 1. Create the pod with node selector
kubectl run nginx-kusc00101 --image=nginx --restart=Never \
  --overrides='{"spec": {"nodeSelector": {"disk": "ssd"}}}'

# 2. Verify pod status (should be Pending if no nodes have disk=ssd)
kubectl get pod nginx-kusc00101 -o wide

# 3. Check events to see scheduling issues (if any)
kubectl describe pod nginx-kusc00101 | grep -A 10 Events
```

## Method 2: Using YAML manifest

1. Create a file named `nginx-pod.yaml`:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-kusc00101
spec:
  containers:
  - name: nginx
    image: nginx
  nodeSelector:
    disk: ssd
```

2. Apply the configuration:

```bash
kubectl apply -f nginx-pod.yaml
```

## To make the pod schedule successfully:

1. First, check available nodes:
```bash
kubectl get nodes
```

2. Add the label to a node (replace <node-name> with your node name):
```bash
kubectl label nodes <node-name> disk=ssd
```

3. Verify the label was added:
```bash
kubectl get nodes --show-labels | grep disk=ssd
```

4. The pod should now be scheduled on the labeled node:
```bash
kubectl get pod nginx-kusc00101 -o wide
```

## To clean up:
```bash
# Delete the pod
kubectl delete pod nginx-kusc00101

# Remove the label (if needed)
kubectl label nodes <node-name> disk-
```

Note: If no nodes have the label `disk=ssd`, the pod will remain in Pending state until a matching node is available.
