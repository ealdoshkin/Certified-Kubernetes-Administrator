# Task: CustomResourceDefinition (CRD)

## Solution

### Step 1: Create CRD

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: operators.stable.example.com
spec:
  group: stable.example.com
  versions:
    - name: v1
      served: true
      storage: true
      schema:
        openAPIV3Schema:
          type: object
          properties:
            spec:
              type: object
              properties:
                email:
                  type: string
                name:
                  type: string
                age:
                  type: integer
  scope: Namespaced
  names:
    plural: operators
    singular: operator
    kind: Operator
    shortNames:
      - op
```

```bash
kubectl apply -f operator-crd.yaml
```

### Step 2: Verify CRD

```bash
# List CRDs
kubectl get crd

# Describe CRD
kubectl describe crd operators.stable.example.com

# Get CRD YAML
kubectl get crd operators.stable.example.com -o yaml
```

### Step 3: Create Custom Resource

```yaml
apiVersion: stable.example.com/v1
kind: Operator
metadata:
  name: operator-sample
spec:
  email: operator-sample@stable.example.com
  name: "operator sample"
  age: 30
```

```bash
kubectl apply -f operator.yaml
```

### Step 4: List Custom Resources

```bash
# Using plural form
kubectl get operators

# Using singular form
kubectl get operator

# Using short name
kubectl get op

# Get specific resource
kubectl get operator operator-sample -o yaml
```

## Key Concepts

- **CRD**: Extends Kubernetes API with custom resources
- **Group**: API group (e.g., stable.example.com)
- **Version**: API version (e.g., v1)
- **Scope**: Namespaced or Cluster-scoped
- **Schema**: Validation schema for custom resource
- **Names**: plural, singular, kind, shortNames

## CRD Components

- **metadata.name**: Must be `<plural>.<group>`
- **spec.group**: API group
- **spec.versions**: API versions
- **spec.scope**: Namespaced or Cluster
- **spec.names**: Resource naming

## Verification

```bash
# Check CRD exists
kubectl get crd operators.stable.example.com

# List custom resources
kubectl get operators

# Describe custom resource
kubectl describe operator operator-sample

# Get custom resource YAML
kubectl get operator operator-sample -o yaml
```

## Use Cases

- Custom application configurations
- Operators (Kubernetes operators)
- Domain-specific resources
- Extending Kubernetes functionality

## Cleanup

```bash
# Delete custom resource
kubectl delete operator operator-sample

# Delete CRD (will delete all custom resources)
kubectl delete crd operators.stable.example.com
```
