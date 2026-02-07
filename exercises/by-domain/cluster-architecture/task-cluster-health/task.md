# Task: Check Cluster Health and Control Plane Status

## Objective
Check the health status of control plane components and cluster.

## Steps

### 1. Check Control Plane Health Endpoints

#### Livez Endpoint (Liveness)
```bash
# Using curl
curl -k https://localhost:6443/livez?verbose

# Using kubectl
kubectl get --raw='/livez?verbose'
```

#### Readyz Endpoint (Readiness)
```bash
# Using curl
curl -k https://localhost:6443/readyz?verbose

# Using kubectl
kubectl get --raw='/readyz?verbose'
```

#### Healthz Endpoint (General Health)
```bash
# Using curl
curl -k https://localhost:6443/healthz?verbose

# Using kubectl
kubectl get --raw='/healthz?verbose'
```

### 2. Check Component Status
```bash
# Check all component statuses
kubectl get componentstatuses
# or
kubectl get cs

# Check specific component
kubectl get componentstatuses scheduler
```

### 3. Check Node Status
```bash
# Get all nodes with status
kubectl get nodes

# Get detailed node information
kubectl describe node <node-name>

# Get node conditions
kubectl get nodes -o jsonpath='{.items[*].status.conditions}'
```

### 4. Check External IPs of Nodes
```bash
# Get external IP addresses of all nodes
kubectl get nodes -o jsonpath='{.items[*].status.addresses[?(@.type=="ExternalIP")].address}'
```

## Key Concepts
- **livez**: Liveness probe - is the component alive?
- **readyz**: Readiness probe - is the component ready to serve traffic?
- **healthz**: General health check endpoint
- **Component Status**: Status of control plane components

## Troubleshooting
- If endpoints return errors, check component logs
- Verify network connectivity to API server
- Check certificate validity
- Review component configuration
