# Solution for Task 12: List Pods for Specific Service

```bash
# 1. Create directory if it doesn't exist
mkdir -p /opt/KUCC00302

# 2. Get the selector from the service
SELECTOR=$(kubectl get svc baz -n development -o jsonpath='{.spec.selector}' | jq -r 'to_entries|map("\(.key)=\(.value|tostring)")|.[]' | paste -sd ',' -)

# 3. Get pods matching the service selector and save to file
kubectl get pods -n development -l "$SELECTOR" -o jsonpath='{range .items[*]}{.metadata.name}{'\n'}{end}' > /opt/KUCC00302/kucc00302.txt

# 4. If the file is empty (no pods found), ensure it exists with empty content
touch /opt/KUCC00302/kucc00302.txt

# 5. Verify the file content
cat /opt/KUCC00302/kucc00302.txt
```

Alternative approach if you know the label selector in advance (e.g., `app=baz-deploy`):

```bash
# 1. Create directory if it doesn't exist
mkdir -p /opt/KUCC00302

# 2. Get pods using known label selector
kubectl get pods -n development -l app=baz-deploy -o jsonpath='{range .items[*]}{.metadata.name}{'\n'}{end}' > /opt/KUCC00302/kucc00302.txt

# 3. Ensure file exists even if no pods are found
touch /opt/KUCC00302/kucc00302.txt
```

Note: The solution first tries to get the selector from the service dynamically. If you know the exact label selector in advance, you can use the alternative approach which is more straightforward.
