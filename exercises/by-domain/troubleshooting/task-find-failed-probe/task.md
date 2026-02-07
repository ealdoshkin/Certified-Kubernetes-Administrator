# Task: Find Pods with Failed Liveness Probes

## Objective
Find all pods with failed liveness probes across multiple namespaces and extract their information.

## Requirements
- Find pods with failed liveness probes in namespaces: `qa`, `alan`, `test`, `production`
- Store pod name and namespace in format: `<namespace>/<pod-name>` to `/opt/KDOB00401/broken.txt`
- Store error events to `/opt/KDOB00401/error.txt`

## Solution

### Step 1: Find Pods with Failed Liveness Probes
```bash
# Extract pods with failed liveness probes
kubectl get events --all-namespaces -o json | \
  jq -r '.items[] | select(.message | contains("Liveness probe failed")) | .involvedObject | .namespace + "/" + .name' | \
  sort -u > /opt/KDOB00401/broken.txt
```

### Step 2: Extract Error Events
```bash
# Get error events with -o wide for full details
kubectl get events --all-namespaces -o wide | \
  grep -i "liveness probe failed" > /opt/KDOB00401/error.txt
```

### Alternative Method
```bash
# Using kubectl and grep
kubectl get events --all-namespaces | \
  grep -i "liveness probe failed" | \
  awk '{print $2"/"$8}' | \
  sort -u > /opt/KDOB00401/broken.txt

# Error events
kubectl get events --all-namespaces -o wide | \
  grep -i "liveness probe failed" > /opt/KDOB00401/error.txt
```

## Key Concepts
- **Events**: Kubernetes events show what happened
- **Liveness Probe Failure**: Indicates unhealthy containers
- **Event Filtering**: Filter events by message content
- **Namespace Scope**: Search across multiple namespaces

## Verification
```bash
# Check broken pods file
cat /opt/KDOB00401/broken.txt

# Check error events
cat /opt/KDOB00401/error.txt

# Verify pods exist
while IFS='/' read -r ns pod; do
  kubectl get pod $pod -n $ns
done < /opt/KDOB00401/broken.txt
```

## Common Liveness Probe Failures
- Container not responding
- Health check endpoint down
- Application crashed
- Timeout issues
- Wrong probe configuration
