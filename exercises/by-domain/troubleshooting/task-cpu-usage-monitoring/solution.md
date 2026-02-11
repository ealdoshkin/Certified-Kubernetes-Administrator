# Task: Find Pod with Highest CPU Usage

## Objective
Find pods with high CPU workloads and identify the pod consuming the most CPU.

## Requirements
- Find pods with label `name=cpu-utilizer`
- Identify pod consuming most CPU
- Write pod name to `/opt/KUTR00102/KUTR00102.txt`

## Solution

### Step 1: Get Pods with Label
```bash
kubectl get pods -l name=cpu-utilizer
```

### Step 2: Get CPU Usage (Requires metrics-server)
```bash
# Get CPU usage for pods
kubectl top pods -l name=cpu-utilizer --sort-by=cpu

# Extract pod with highest CPU
kubectl top pods -l name=cpu-utilizer --sort-by=cpu --no-headers | \
  head -1 | \
  awk '{print $1}' > /opt/KUTR00102/KUTR00102.txt
```

### Alternative: Using JSON Output
```bash
# Get top pods and extract highest CPU pod
kubectl top pods -l name=cpu-utilizer --sort-by=cpu -o json | \
  jq -r '.items[0].metadata.name' > /opt/KUTR00102/KUTR00102.txt
```

## Key Concepts
- **kubectl top**: Shows resource usage (requires metrics-server)
- **--sort-by**: Sort by CPU or memory usage
- **Label Selector**: Filter pods by labels
- **CPU Usage**: Current CPU consumption

## Prerequisites
- Metrics-server must be installed and running
- Pods must have resource requests/limits defined

## Verification
```bash
# Check metrics-server is running
kubectl get pods -n kube-system | grep metrics-server

# Check CPU usage
kubectl top pods -l name=cpu-utilizer

# Verify result
cat /opt/KUTR00102/KUTR00102.txt

# Confirm pod exists
kubectl get pod $(cat /opt/KUTR00102/KUTR00102.txt)
```

## Important Notes
- Requires metrics-server for kubectl top
- CPU usage is current consumption
- Sort by CPU to find highest usage
- May need to wait for metrics to be available
