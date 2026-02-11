# Solution for Task 13: Add Init Container to Pod Spec

1. Create the directory and pod spec file:

```bash
# 1. Create directory
mkdir -p /opt/KUCC00108
```

2. Create the pod spec file at `/opt/KUCC00108/pod-spec-KUCC00108.yaml` with the following content:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: hungry-bear
spec:
  containers:
  - name: main
    image: busybox
    command: 
      - sh
      - -c
      - |
        if [ -f /workdir/calm.txt ]; then 
          echo "File exists. Pod will continue running."; 
          sleep 3600; 
        else 
          echo "Error: File /workdir/calm.txt is missing"; 
          exit 1; 
        fi
    volumeMounts:
    - name: workdir
      mountPath: /workdir
  initContainers:
  - name: init
    image: busybox
    command: 
      - sh
      - -c
      - |
        echo "Creating file /workdir/calm.txt";
        echo "This file was created by the init container" > /workdir/calm.txt;
        echo "File created successfully"
    volumeMounts:
    - name: workdir
      mountPath: /workdir
  volumes:
  - name: workdir
    emptyDir: {}
```

3. Apply the pod configuration:
```bash
kubectl apply -f /opt/KUCC00108/pod-spec-KUCC00108.yaml
```

4. Verify the pod status and logs:
```bash
# Check pod status
kubectl get pod hungry-bear

# Check main container logs
kubectl logs hungry-bear

# Check init container logs
kubectl logs hungry-bear -c init

# Verify the file was created
kubectl exec -it hungry-bear -- cat /workdir/calm.txt
```

This solution creates a pod with:
1. An init container that creates a file `/workdir/calm.txt`
2. A main container that verifies the file's existence
3. An `emptyDir` volume shared between both containers
4. Proper error handling if the file is missing
