# Solution for Task 9: Extract and Filter Logs

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

This will:
1. Create a test nginx pod with a startup message
2. Wait for the pod to be ready
3. Extract logs, filter for lines containing "started" (case-insensitive), and save to /opt/error-logs
4. Display the contents of the output file for verification
