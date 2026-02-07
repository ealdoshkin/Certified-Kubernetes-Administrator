# Task: Troubleshoot Service Connectivity Issues

## Objective
Troubleshoot why a service is not accessible and fix connectivity issues.

## Scenario: Cannot Access Service via curl

```bash
# Create deployment and service
kubectl -n kb6656 apply -f https://raw.githubusercontent.com/chadmcrowell/acing-the-cka-exam/main/ch_08/deploy-and-svc.yaml

# Try to access the service
kubectl -n kb6656 get svc
curl <service-ip>:80
```

## Troubleshooting Steps

### 1. Check Service Status
```bash
# List services
kubectl -n kb6656 get svc

# Describe service
kubectl -n kb6656 describe svc <service-name>

# Check service endpoints
kubectl -n kb6656 get endpoints <service-name>
```

### 2. Check Pod Status
```bash
# List pods
kubectl -n kb6656 get pods

# Check pod labels match service selector
kubectl -n kb6656 get pods --show-labels
kubectl -n kb6656 get svc <service-name> -o jsonpath='{.spec.selector}'
```

### 3. Test Pod Connectivity
```bash
# Get pod IP
kubectl -n kb6656 get pods -o wide

# Test direct pod access
curl <pod-ip>:80

# Exec into pod and test
kubectl -n kb6656 exec -it <pod-name> -- curl localhost:80
```

### 4. Check Service Type and Ports
```bash
# Check service type
kubectl -n kb6656 get svc <service-name> -o yaml | grep -A 5 spec:

# Verify port mapping
kubectl -n kb6656 get svc <service-name> -o jsonpath='{.spec.ports[*]}'
```

### 5. Check Network Policies
```bash
# Check for network policies blocking traffic
kubectl -n kb6656 get networkpolicies

# Describe network policies
kubectl -n kb6656 describe networkpolicy <policy-name>
```

## Common Issues and Fixes

### Issue 1: No Endpoints
**Cause**: Pod labels don't match service selector

**Fix:**
```bash
# Check selector
kubectl -n kb6656 get svc <service-name> -o jsonpath='{.spec.selector}'

# Update pod labels to match
kubectl -n kb6656 label pod <pod-name> <key>=<value>
```

### Issue 2: Wrong Port
**Cause**: Service port doesn't match container port

**Fix:**
```bash
# Check container port
kubectl -n kb6656 get pod <pod-name> -o jsonpath='{.spec.containers[*].ports[*].containerPort}'

# Update service port
kubectl -n kb6656 edit svc <service-name>
```

### Issue 3: Network Policy Blocking
**Cause**: Network policy denying traffic

**Fix:**
```bash
# Delete or modify network policy
kubectl -n kb6656 delete networkpolicy <policy-name>
# or
kubectl -n kb6656 edit networkpolicy <policy-name>
```

### Issue 4: Service Type Issue
**Cause**: Wrong service type for access method

**Fix:**
```bash
# Change service type if needed
kubectl -n kb6656 patch svc <service-name> -p '{"spec":{"type":"NodePort"}}'
```

## Verification
```bash
# Test service access
curl <service-ip>:<port>

# Test from within cluster
kubectl run test-curl --image=nicolaka/netshoot -it --rm -- curl <service-name>.<namespace>.svc.cluster.local

# Check service endpoints are populated
kubectl -n kb6656 get endpoints <service-name>
```

## Key Concepts
- **Service Selector**: Must match pod labels
- **Endpoints**: Backend pods for the service
- **Service Port**: Port the service listens on
- **Target Port**: Port on the pod containers
- **Network Policies**: Can block service traffic
