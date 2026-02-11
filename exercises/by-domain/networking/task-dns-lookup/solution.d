# Task: DNS Lookup for Services and Pods

## Objective
Create a deployment with service and perform DNS lookups for both service and pod DNS records.

## Requirements
- Deployment name: `nginx-random`
- Service name: `nginx-random`
- Service and pod should be accessible via DNS records
- Use nslookup to lookup DNS records
- Save service DNS output to `/opt/KUNW00601/service.dns`
- Save pod DNS output to `/opt/KUNW00601/pod.dns`

## Solution

### Step 1: Create Deployment
```bash
kubectl create deployment nginx-random --image=nginx
```

### Step 2: Create Service
```bash
kubectl expose deployment nginx-random --port=80 --target-port=80 --name=nginx-random
```

### Step 3: Get Pod Name
```bash
POD_NAME=$(kubectl get pods -l app=nginx-random -o jsonpath='{.items[0].metadata.name}')
```

### Step 4: Perform DNS Lookups
```bash
# Service DNS lookup
kubectl run dns-test --image=busybox --rm -it --restart=Never -- nslookup nginx-random.default.svc.cluster.local > /opt/KUNW00601/service.dns

# Pod DNS lookup (format: <pod-ip>.<namespace>.pod.cluster.local)
POD_IP=$(kubectl get pod $POD_NAME -o jsonpath='{.status.podIP}')
kubectl run dns-test --image=busybox --rm -it --restart=Never -- nslookup ${POD_IP//./-}.default.pod.cluster.local > /opt/KUNW00601/pod.dns
```

## Key Concepts
- **Service DNS**: `<service-name>.<namespace>.svc.cluster.local`
- **Pod DNS**: `<pod-ip-replaced-dots-with-dashes>.<namespace>.pod.cluster.local`
- **Cluster DNS**: CoreDNS provides DNS resolution
- **FQDN**: Fully Qualified Domain Name

## DNS Formats

### Service DNS
- Short name: `nginx-random` (same namespace)
- Namespace: `nginx-random.default`
- FQDN: `nginx-random.default.svc.cluster.local`

### Pod DNS
- Format: `<pod-ip-with-dashes>.<namespace>.pod.cluster.local`
- Example: `10-244-1-5.default.pod.cluster.local` (for IP 10.244.1.5)

## Verification
```bash
# Check service exists
kubectl get svc nginx-random

# Check deployment
kubectl get deploy nginx-random

# Test service DNS
kubectl run test --image=busybox --rm -it --restart=Never -- nslookup nginx-random

# Test pod DNS
kubectl run test --image=busybox --rm -it --restart=Never -- nslookup <pod-ip-formatted>
```

## Important Notes
- Pod DNS requires pod IP with dots replaced by dashes
- Service DNS works with short name in same namespace
- DNS resolution requires CoreDNS to be running
- Pod DNS may not work in all cluster configurations
