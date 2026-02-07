# Task: Create User with Certificate Signing Request (CSR)

## Objective
Create a new user named "Sandra" by:
1. Creating a private key
2. Creating a certificate signing request (CSR)
3. Using the CSR resource in Kubernetes to generate the client certificate
4. Adding the user to kubeconfig

## Steps

### 1. Create Private Key
```bash
# Create a private key using openssl with 2048-bit encryption
openssl genrsa -out sandra.key 2048
```

### 2. Create Certificate Signing Request
```bash
# Create a certificate signing request
openssl req -new -key sandra.key -subj "/CN=sandra" -out sandra.csr

# Store the CSR in an environment variable (base64 encoded)
export REQUEST=$(cat sandra.csr | base64 -w 0)
```

### 3. Create CSR Kubernetes Resource
```bash
cat <<EOF | kubectl apply -f -
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: sandra
spec:
  groups:
  - developers
  request: $REQUEST
  signerName: kubernetes.io/kube-apiserver-client
  usages:
  - client auth
EOF
```

### 4. Approve the CSR
```bash
# List CSRs
kubectl get csr

# Approve the CSR
kubectl certificate approve sandra

# Extract the client certificate
kubectl get csr sandra -o jsonpath='{.status.certificate}' | base64 -d > sandra.crt
```

### 5. Add User to Kubeconfig
```bash
# Set credentials in kubeconfig
kubectl config set-credentials sandra --client-key=sandra.key --client-certificate=sandra.crt --embed-certs

# View kubeconfig
kubectl config view

# Set context for sandra
kubectl config set-context sandra --user=sandra --cluster=kubernetes

# Switch to sandra context
kubectl config use-context sandra
```

## Verification
```bash
# Verify you're using the sandra context
kubectl config get-contexts

# Test access
kubectl get pods
```

## Key Concepts
- **CSR (Certificate Signing Request)**: Request for certificate from Kubernetes CA
- **Private Key**: Used for authentication
- **Client Certificate**: Signed by Kubernetes CA for user authentication
- **kubeconfig**: Configuration file for kubectl
