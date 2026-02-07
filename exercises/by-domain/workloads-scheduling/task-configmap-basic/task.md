# Task: ConfigMap Basics

## Objective
Create and manage ConfigMaps using different methods.

## Tasks

### 1. Create ConfigMap from Literals
```bash
kubectl create configmap config --from-literal=foo=lala --from-literal=foo2=lolo
```

### 2. Display ConfigMap Values
```bash
kubectl get cm config -o yaml
# or
kubectl describe cm config
```

### 3. Create ConfigMap from File
```bash
# Create file
echo -e "foo3=lili\nfoo4=lele" > config.txt

# Create ConfigMap
kubectl create cm configmap2 --from-file=config.txt
kubectl get cm configmap2 -o yaml
```

### 4. Create ConfigMap from .env File
```bash
# Create .env file
echo -e "var1=val1\n# this is a comment\n\nvar2=val2\n#anothercomment" > config.env

# Create ConfigMap
kubectl create cm configmap3 --from-env-file=config.env
kubectl get cm configmap3 -o yaml
```

### 5. Create ConfigMap from File with Custom Key
```bash
# Create file
echo -e "var3=val3\nvar4=val4" > config4.txt

# Create ConfigMap with custom key
kubectl create cm configmap4 --from-file=special=config4.txt
kubectl describe cm configmap4
```

## Key Concepts
- **ConfigMap**: Store non-confidential configuration data
- **from-literal**: Create from key-value pairs
- **from-file**: Create from file (key is filename)
- **from-env-file**: Create from .env file format
- **Custom key**: Specify key name when using from-file

## Verification
```bash
# List all ConfigMaps
kubectl get configmaps

# Get specific ConfigMap
kubectl get cm config -o yaml

# Describe ConfigMap
kubectl describe cm config
```
