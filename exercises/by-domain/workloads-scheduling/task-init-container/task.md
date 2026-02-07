# Task: Init Containers

## Objective
Add an init container to a pod that performs setup tasks before the main container starts.

## Requirements
- Add an init container to existing pod spec
- Init container should create an empty file named `/workdir/calm.txt`
- If `/workdir/calm.txt` is not detected, the pod should exit
- Update the pod spec file and create the pod

## Solution

### Step 1: Read Existing Pod Spec
```bash
cat /opt/KUCC00108/pod-spec-KUCC00108.yaml
```

### Step 2: Edit Pod Spec to Add Init Container
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: hungry-bear
spec:
  initContainers:
  - name: init-workdir
    image: busybox
    command: ['sh', '-c', 'touch /workdir/calm.txt']
    volumeMounts:
    - name: workdir
      mountPath: /workdir
  containers:
  - name: main-container
    image: nginx
    command: ['sh', '-c', 'if [ ! -f /workdir/calm.txt ]; then exit 1; fi; sleep 3600']
    volumeMounts:
    - name: workdir
      mountPath: /workdir
  volumes:
  - name: workdir
    emptyDir: {}
```

### Step 3: Create Pod
```bash
kubectl create -f /opt/KUCC00108/pod-spec-KUCC00108.yaml
```

## Key Concepts
- **Init Containers**: Run before main containers start
- **Sequential Execution**: Init containers run in order
- **Shared Volumes**: Init containers can share volumes with main containers
- **Pod Startup**: Pod doesn't start until all init containers succeed

## Init Container Use Cases
- Database migrations
- File downloads
- Configuration setup
- Dependency checks
- Data initialization

## Verification
```bash
# Check pod status
kubectl get pod hungry-bear

# Check init container logs
kubectl logs hungry-bear -c init-workdir

# Verify file was created
kubectl exec hungry-bear -- ls -la /workdir/calm.txt
```

## Important Notes
- Init containers run sequentially (one after another)
- All init containers must succeed for pod to start
- If init container fails, pod status shows Init:Error
- Init containers can access same volumes as main containers
