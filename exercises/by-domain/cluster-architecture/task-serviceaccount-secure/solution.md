# Task: Create Service Account Without Token Mount

## Objective
Create a service account and pod that does NOT mount the service account token.

## Steps

### 1. Create Service Account
```bash
# Create service account YAML with dry-run
kubectl -n default create sa secure-sa --dry-run=client -o yaml > sa.yaml

# Add automountServiceAccountToken: false
echo "automountServiceAccountToken: false" >> sa.yaml

# Create the service account
kubectl create -f sa.yaml

# Verify
kubectl -n default get sa secure-sa
```

### 2. Create Pod Using the Service Account
```bash
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: secure-pod
spec:
  serviceAccountName: secure-sa
  containers:
  - image: nginx
    name: secure-pod
EOF

# Wait for pod to be running
kubectl get po -w
```

### 3. Verify Token Was Not Mounted
```bash
# Try to access the token (should fail)
kubectl exec secure-pod -- cat /var/run/secrets/kubernetes.io/serviceaccount/token
```

**Expected Output:**
```
cat: /var/run/secrets/kubernetes.io/serviceaccount/token: No such file or directory
```

## Key Concepts
- **Service Account**: Identity for pods to authenticate to API server
- **Service Account Token**: Mounted at `/var/run/secrets/kubernetes.io/serviceaccount/token`
- **automountServiceAccountToken**: Controls automatic token mounting
- **Security**: Disabling token mount reduces attack surface

## Use Cases
- Pods that don't need API server access
- Security-sensitive applications
- Reducing token exposure
