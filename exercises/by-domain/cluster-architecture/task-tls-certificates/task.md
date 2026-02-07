# Task: TLS Certificate Management

## Objective
Understand and work with TLS certificates for Kubernetes authentication.

## Certificate Creation Process

### 1. Certificate Authority (CA) Creation
```bash
# Generate CA private key
openssl genrsa -out ca.key 2048

# Create CA certificate signing request
openssl req -new -key ca.key -subj "/CN=KUBERNETES-CA" -out ca.csr

# Sign the CA certificate
openssl x509 -req -in ca.csr -signkey ca.key -out ca.crt
```

### 2. Admin User Certificate Creation
```bash
# Generate admin private key
openssl genrsa -out admin.key 2048

# Create admin certificate signing request
openssl req -new -key admin.key -subj "/CN=kube-admin" -out admin.csr

# Sign admin certificate using CA
openssl x509 -req -in admin.csr -CA ca.crt -CAkey ca.key -out admin.crt
```

## Certificate API (Kubernetes CSR)

### Create Certificate Signing Request
```bash
# Convert CSR to base64 in one line
cat sandra.csr | base64 -w 0

# Create CSR resource
cat <<EOF | kubectl apply -f -
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: sandra
spec:
  request: <base64-encoded-csr>
  signerName: kubernetes.io/kube-apiserver-client
  usages:
  - client auth
EOF
```

### Approve Certificate
```bash
# List CSRs
kubectl get csr

# Approve certificate
kubectl certificate approve sandra

# Extract approved certificate
kubectl get csr sandra -o jsonpath='{.status.certificate}' | base64 -d > sandra.crt
```

## Certificate Inspection

### Check Certificate Details
```bash
# View certificate details
openssl x509 -in admin.crt -text -noout

# Check certificate subject (CN)
openssl x509 -in admin.crt -text -noout | grep Subject

# Check certificate issuer
openssl x509 -in admin.crt -text -noout | grep Issuer
```

### Find API Server Certificates
```bash
# Check manifests for certificate paths
cat /etc/kubernetes/manifests/kube-apiserver.yaml | grep -i cert

# Common certificate locations:
# - /etc/kubernetes/pki/ca.crt
# - /etc/kubernetes/pki/apiserver.crt
# - /etc/kubernetes/pki/apiserver.key
```

### Check Kubelet Client Certificate
```bash
# Kubelet client certificate location
ls /var/lib/kubelet/pki/

# View kubelet client certificate
openssl x509 -in /var/lib/kubelet/pki/kubelet-client-current.pem -text -noout
```

## Certificate Groups
```bash
# Check groups in CSR
kubectl get csr sandra -o yaml | grep groups

# Groups are specified in CSR spec
spec:
  groups:
  - system:authenticated
  - developers
```

## Troubleshooting
```bash
# If API server is down, check Docker logs
docker logs <api-server-container>

# Check certificate expiration
openssl x509 -in cert.crt -noout -dates

# Verify certificate chain
openssl verify -CAfile ca.crt admin.crt
```

## Key Concepts
- **CA (Certificate Authority)**: Signs all certificates
- **CN (Common Name)**: Identity in certificate (username for users)
- **CSR (Certificate Signing Request)**: Request for certificate from Kubernetes CA
- **Certificate API**: Kubernetes API for managing certificates
- **SignerName**: Type of certificate (client auth, server auth, etc.)

## Authentication Mechanisms
- Static username and passwords
- Username and token
- Service accounts
- TLS certificates (most common)
