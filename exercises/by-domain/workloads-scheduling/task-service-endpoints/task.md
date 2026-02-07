# Task: List Pods Implementing a Service

## Objective
List all pods that implement a service (pods selected by service).

## Requirements
- Service name: `baz`
- Namespace: `development`
- Output format: One pod name per line
- Save to file: `/opt/KUCC00302/kucc00302.txt`

## Solution

### Method 1: Using Service Selector
```bash
# Get service to find selector
kubectl get svc baz -n development -o jsonpath='{.spec.selector}'

# Use selector to find pods
kubectl get pods -n development --selector=app=baz -o name | cut -d/ -f2 > /opt/KUCC00302/kucc00302.txt
```

### Method 2: Using Service Endpoints
```bash
# Get endpoints (shows pods backing the service)
kubectl get endpoints baz -n development -o jsonpath='{.subsets[*].addresses[*].targetRef.name}' | tr ' ' '\n' > /opt/KUCC00302/kucc00302.txt
```

### Method 3: Using Service Labels
```bash
# If service uses labels, find pods with same labels
kubectl get svc baz -n development -o jsonpath='{.spec.selector}' | jq -r 'to_entries | .[] | "\(.key)=\(.value)"' | xargs -I {} kubectl get pods -n development -l {} -o name | cut -d/ -f2 > /opt/KUCC00302/kucc00302.txt
```

## Key Concepts
- **Service Selector**: Labels used to select pods
- **Endpoints**: Pods that match service selector
- **Target References**: Pod names in endpoint addresses
- **Label Matching**: Pods must match all service selector labels

## Verification
```bash
# Check service selector
kubectl get svc baz -n development -o yaml | grep -A 5 selector

# Check endpoints
kubectl get endpoints baz -n development

# Verify pod names in file
cat /opt/KUCC00302/kucc00302.txt

# Verify pods exist
kubectl get pods -n development -l <selector-from-service>
```

## Common Use Cases
- Troubleshooting service connectivity
- Finding pods behind a service
- Service discovery
- Load balancing verification
