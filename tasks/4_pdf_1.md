# CKA Practice Tasks Simulator

Based on the exam questions document, here are simulated tasks for CKA practice:

## Task Set 1: Pod Creation & Environment Variables

### Task 1: Create Pod with Environment Variables
**Objective:** Create a pod named `nginx` with environment variable `var1=value1` and verify the variable exists in the pod.

**Requirements:**
- Use image: `nginx`
- Pod name: `nginx`
- Environment variable: `var1=value1`
- Restart policy: `Never`
- Verify using three different methods

**Commands to execute:**
```bash
# 1. Create the pod
kubectl run nginx --image=nginx --restart=Never --env=var1=value1

# 2. Verify method 1: Check all environment variables
kubectl exec -it nginx -- env | grep var1

# 3. Verify method 2: Echo the variable
kubectl exec -it nginx -- sh -c 'echo $var1'

# 4. Verify method 3: Describe pod and grep
kubectl describe po nginx | grep value1
```

### Task 2: List Pods with Custom Columns
**Objective:** List the nginx pod with custom columns showing POD_NAME and POD_STATUS.

**Requirements:**
- Use custom columns format
- Column headers: POD_NAME and POD_STATUS

**Commands to execute:**
```bash
# List pod with custom columns
kubectl get po nginx -o=custom-columns="POD_NAME:.metadata.name,POD_STATUS:.status.phase"
```

## Task Set 2: Namespace & Pod Management

### Task 3: Create Pod in New Namespace
**Objective:** Create a pod named `mongo` using image `mongo` in a new namespace called `my-website`.

**Requirements:**
- Create namespace `my-website`
- Create pod `mongo` in that namespace
- Use image: `mongo`

**Commands to execute:**
```bash
# 1. Create namespace
kubectl create namespace my-website

# 2. Create pod in the namespace
kubectl run mongo --image=mongo --restart=Never -n my-website

# 3. Verify
kubectl get pods -n my-website
```

## Task Set 3: Deployment Management

### Task 4: Deployment Rolling Update & Rollback
**Objective:** Create a deployment with 3 replicas, perform rolling update, then rollback.

**Requirements:**
- Deployment name: `nginx-app`
- Initial image: `nginx:1.11.10-alpine`
- Replicas: 3
- Update to: `nginx:1.11.13-alpine`
- Rollback to original version

**Commands to execute:**
```bash
# 1. Create deployment
kubectl create deployment nginx-app --image=nginx:1.11.10-alpine --replicas=3

# 2. Verify deployment
kubectl get deployments
kubectl get pods -l app=nginx-app

# 3. Perform rolling update
kubectl set image deployment/nginx-app nginx=nginx:1.11.13-alpine

# 4. Check rollout status
kubectl rollout status deployment/nginx-app

# 5. Check history
kubectl rollout history deployment/nginx-app

# 6. Rollback to previous version
kubectl rollout undo deployment/nginx-app

# 7. Verify rollback
kubectl describe deployment nginx-app | grep Image
```

## Task Set 4: Node Management

### Task 5: Drain Node
**Objective:** Set node `ek8s-node-1` as unavailable and reschedule all pods running on it.

**Requirements:**
- Cordon the node (mark as unschedulable)
- Drain the node (evict all pods)

**Commands to execute:**
```bash
# 1. Mark node as unschedulable
kubectl cordon ek8s-node-1

# 2. Drain the node (evict pods)
kubectl drain ek8s-node-1 --ignore-daemonsets --delete-emptydir-data

# 3. Verify node status
kubectl get nodes

# 4. To make node schedulable again (optional)
kubectl uncordon ek8s-node-1
```

## Task Set 5: Storage Management

### Task 6: Create Persistent Volume
**Objective:** Create a persistent volume with specific parameters.

**Requirements:**
- PV name: `app-data`
- Capacity: 2Gi
- Access mode: ReadWriteMany
- Type: hostPath
- Path: `/srv/app-data`
- Storage class: `shared`

**YAML file to create:**
```yaml
# app-data-pv.yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: app-data
spec:
  capacity:
    storage: 2Gi
  accessModes:
    - ReadWriteMany
  storageClassName: shared
  hostPath:
    path: /srv/app-data
```

**Commands to execute:**
```bash
# 1. Create the PV
kubectl apply -f app-data-pv.yaml

# 2. Verify
kubectl get pv app-data
```

### Task 7: Create PersistentVolumeClaim
**Objective:** Create a PVC that requests the PV created in Task 6.

**YAML file to create:**
```yaml
# app-data-pvc.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: app-data
spec:
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 2Gi
  storageClassName: shared
```

**Commands to execute:**
```bash
# 1. Create PVC
kubectl apply -f app-data-pvc.yaml

# 2. Check PVC status
kubectl get pvc app-data

# 3. Check PV status (should be Bound)
kubectl get pv app-data
```

### Task 8: List PVs Sorted by Capacity
**Objective:** List all persistent volumes sorted by capacity and save output to file.

**Requirements:**
- Sort by capacity using kubectl's sorting functionality
- Save full output to `/opt/KUCC00102/volume_list`
- Don't manipulate output further

**Commands to execute:**
```bash
# 1. Create directory if it doesn't exist
mkdir -p /opt/KUCC00102

# 2. List PVs sorted by capacity and save to file
kubectl get pv --sort-by='.spec.capacity.storage' > /opt/KUCC00102/volume_list

# 3. Verify file content
cat /opt/KUCC00102/volume_list
```

## Task Set 6: Logging & Monitoring

### Task 9: Extract and Filter Logs
**Objective:** Extract logs from pod `frontend`, filter for "started", and save to file.

**Requirements:**
- Pod name: `frontend`
- Search pattern: "started" (case-insensitive)
- Output file: `/opt/error-logs`

**Commands to execute:**
```bash
# 1. First, create a test frontend pod if it doesn't exist
kubectl run frontend --image=nginx --restart=Never -- sh -c 'echo "Application started successfully"; nginx -g "daemon off;"'

# 2. Wait for pod to be ready
kubectl wait --for=condition=Ready pod/frontend --timeout=30s

# 3. Extract logs, filter, and save to file
kubectl logs frontend | grep -i "started" > /opt/error-logs

# 4. Verify
cat /opt/error-logs
```

## Task Set 7: JSONPath & Output Formatting

### Task 10: List Pods with JSONPath
**Objective:** Get list of all pods showing name and namespace using JSONPath.

**Requirements:**
- Output format: One pod per line with name and namespace
- Use JSONPath expression

**Commands to execute:**
```bash
# Method 1: Using JSONPath template
kubectl get pods -o=jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.metadata.namespace}{"\n"}{end}'

# Method 2: Alternative JSONPath
kubectl get pods -o=jsonpath='{"NAME\tNAMESPACE\n"}{range .items[*]}{.metadata.name}{"\t"}{.metadata.namespace}{"\n"}{end}'
```

### Task 11: Check Image Version without Describe
**Objective:** Check the image version in a pod without using `describe` command.

**Requirements:**
- Pod name: `nginx`
- Don't use `kubectl describe`

**Commands to execute:**
```bash
# 1. Create test pod if needed
kubectl run nginx --image=nginx:1.14.2 --restart=Never

# 2. Check image version using JSONPath
kubectl get pod nginx -o jsonpath='{.spec.containers[0].image}'

# 3. Alternative using yq
kubectl get pod nginx -o yaml | yq '.spec.containers[0].image'
```

### Task 12: List Pods for Specific Service
**Objective:** Create a file listing all pods that implement service `baz` in namespace `development`.

**Requirements:**
- Namespace: `development`
- Service: `baz`
- Output file: `/opt/KUCC00302/kucc00302.txt`
- Format: One pod name per line

**Commands to execute:**
```bash
# 1. Create directory
mkdir -p /opt/KUCC00302

# 2. First, set up test environment (if not exists)
kubectl create namespace development
kubectl create deployment baz-deploy --image=nginx --replicas=2 -n development
kubectl expose deployment baz-deploy --name=baz --port=80 -n development

# 3. Get pods for service baz
kubectl get pods -n development -l app=baz-deploy -o jsonpath='{range .items[*]}{.metadata.name}{"\n"}{end}' > /opt/KUCC00302/kucc00302.txt

# 4. Verify
cat /opt/KUCC00302/kucc00302.txt
```

## Task Set 8: Init Containers

### Task 13: Add Init Container to Existing Pod Spec
**Objective:** Add an init container to a pod spec that creates a file and validates it.

**Requirements:**
- Pod spec file: `/opt/KUCC00108/pod-spec-KUCC00108.yaml`
- Init container should create: `/workdir/calm.txt`
- Main container should check for file existence
- If file doesn't exist, pod should exit

**Sample pod spec to create:**
```yaml
# /opt/KUCC00108/pod-spec-KUCC00108.yaml
apiVersion: v1
kind: Pod
metadata:
  name: hungry-bear
spec:
  containers:
  - name: main
    image: busybox
    command: ['sh', '-c', 'if [ -f /workdir/calm.txt ]; then echo "File exists"; sleep 3600; else echo "File missing"; exit 1; fi']
    volumeMounts:
    - name: workdir
      mountPath: /workdir
  initContainers:
  - name: init
    image: busybox
    command: ['sh', '-c', 'touch /workdir/calm.txt']
    volumeMounts:
    - name: workdir
      mountPath: /workdir
  volumes:
  - name: workdir
    emptyDir: {}
```

**Commands to execute:**
```bash
# 1. Create directory
mkdir -p /opt/KUCC00108

# 2. Create the pod spec file
cat > /opt/KUCC00108/pod-spec-KUCC00108.yaml << 'EOF'
apiVersion: v1
kind: Pod
metadata:
  name: hungry-bear
spec:
  containers:
  - name: main
    image: busybox
    command: ['sh', '-c', 'if [ -f /workdir/calm.txt ]; then echo "File exists"; sleep 3600; else echo "File missing"; exit 1; fi']
    volumeMounts:
    - name: workdir
      mountPath: /workdir
  initContainers:
  - name: init
    image: busybox
    command: ['sh', '-c', 'touch /workdir/calm.txt']
    volumeMounts:
    - name: workdir
      mountPath: /workdir
  volumes:
  - name: workdir
    emptyDir: {}
EOF

# 3. Create the pod
kubectl apply -f /opt/KUCC00108/pod-spec-KUCC00108.yaml

# 4. Check pod status
kubectl get pod hungry-bear
kubectl logs hungry-bear
```

## Task Set 9: Scheduling

### Task 14: Schedule Pod with Node Selector
**Objective:** Schedule a pod with node selector constraint.

**Requirements:**
- Pod name: `nginx-kusc00101`
- Image: `nginx`
- Node selector: `disk=ssd`

**Commands to execute:**
```bash
# Method 1: Imperative command
kubectl run nginx-kusc00101 --image=nginx --restart=Never --overrides='{"spec": {"nodeSelector": {"disk": "ssd"}}}'

# Method 2: Create YAML file
cat > nginx-pod.yaml << EOF
apiVersion: v1
kind: Pod
metadata:
  name: nginx-kusc00101
spec:
  containers:
  - name: nginx
    image: nginx
  nodeSelector:
    disk: ssd
EOF

kubectl apply -f nginx-pod.yaml

# Check pod scheduling (may be pending if no node has disk=ssd label)
kubectl get pod nginx-kusc00101 -o wide
kubectl describe pod nginx-kusc00101
```

## Setup Script for Practice Environment

```bash
#!/bin/bash
# setup-practice.sh
echo "Setting up CKA practice environment..."

# Create necessary directories
mkdir -p /opt/KUCC00102
mkdir -p /opt/KUCC00302
mkdir -p /opt/KUCC00108

# Create test pods and deployments
kubectl create namespace development 2>/dev/null || true
kubectl create namespace my-website 2>/dev/null || true

# Label a node for node selector task (using first worker node)
NODE_NAME=$(kubectl get nodes | grep -v master | head -1 | awk '{print $1}')
kubectl label node $NODE_NAME disk=ssd --overwrite

echo "Practice environment setup complete!"
echo "Run the tasks in order from Task 1 to Task 14."
```

## Verification Checklist

After completing each task, verify:

1. **Task 1**: `kubectl exec nginx -- env | grep var1` returns `var1=value1`
2. **Task 2**: Custom columns show correct pod name and status
3. **Task 3**: `kubectl get pods -n my-website` shows mongo pod
4. **Task 4**: Deployment has 3 replicas and correct image version
5. **Task 5**: Node `ek8s-node-1` shows `SchedulingDisabled`
6. **Task 6**: PV `app-data` exists with 2Gi capacity
7. **Task 7**: PVC `app-data` is Bound to PV
8. **Task 8**: File `/opt/KUCC00102/volume_list` exists and shows sorted PVs
9. **Task 9**: File `/opt/error-logs` contains "started"
10. **Task 10**: JSONPath output shows all pods with names and namespaces
11. **Task 11**: Command returns image version without using describe
12. **Task 12**: File `/opt/KUCC00302/kucc00302.txt` has pod names
13. **Task 13**: Pod `hungry-bear` runs successfully (file check passes)
14. **Task 14**: Pod `nginx-kusc00101` has nodeSelector set

These tasks cover key CKA exam objectives including pod creation, deployments, scheduling, storage, troubleshooting, and logging.
