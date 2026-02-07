# Task: Create Secret for MySQL Deployment

## Objective
Create a Kubernetes secret to store MySQL username and password, and add credentials to a MySQL deployment.

## Requirements
- Secret named "configsecret" storing username and password
- MySQL deployment running 2 replicas
- Add credentials to MySQL deployment

## Solution

### Step 1: Create Secret
```bash
# Create secret from literals
kubectl create secret generic configsecret \
  --from-literal=username=mysqluser \
  --from-literal=password=mysqlpassword

# Or create from YAML
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Secret
metadata:
  name: configsecret
type: Opaque
data:
  username: bXlzcWx1c2Vy  # base64 encoded
  password: bXlzcWxwYXNzd29yZA==  # base64 encoded
EOF
```

### Step 2: Create MySQL Deployment with Secret
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mysql
spec:
  replicas: 2
  selector:
    matchLabels:
      app: mysql
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
      - name: mysql
        image: mysql:8.0
        env:
        - name: MYSQL_USER
          valueFrom:
            secretKeyRef:
              name: configsecret
              key: username
        - name: MYSQL_PASSWORD
          valueFrom:
            secretKeyRef:
              name: configsecret
              key: password
        - name: MYSQL_ROOT_PASSWORD
          valueFrom:
            secretKeyRef:
              name: configsecret
              key: password
```

## Key Concepts
- **Secret**: Store sensitive data (passwords, tokens)
- **secretKeyRef**: Reference secret key as environment variable
- **Base64 Encoding**: Secrets are base64 encoded (not encrypted)
- **Environment Variables**: Inject secret values as env vars

## Alternative: Using envFrom
```yaml
spec:
  containers:
  - name: mysql
    image: mysql:8.0
    envFrom:
    - secretRef:
        name: configsecret
```

## Verification
```bash
# Check secret exists
kubectl get secret configsecret

# Check deployment
kubectl get deployment mysql

# Check pods
kubectl get pods -l app=mysql

# Verify environment variables
kubectl exec <mysql-pod> -- env | grep MYSQL
```

## Best Practices
- Use descriptive secret names
- Store secrets in version control (encrypted)
- Rotate secrets regularly
- Use separate secrets for different environments
