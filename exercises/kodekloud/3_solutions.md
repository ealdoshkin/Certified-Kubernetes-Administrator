# Moc Exam 3 Solutions

### 1 (Weight: 6) - Network Parameters

```bash
# Create sysctl configuration file
cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.ipv4.ip_forward = 1
net.bridge.bridge-nf-call-iptables = 1
EOF

# Apply sysctl params without reboot
sudo sysctl --system
```

---

### 2 (Weight: 8) - RBAC and Service Account

```bash
# Create service account
kubectl create serviceaccount pvviewer

# Create cluster role
kubectl create clusterrole pvviewer-role \
  --resource=persistentvolumes \
  --verb=list

# Create cluster role binding
kubectl create clusterrolebinding pvviewer-role-binding \
  --clusterrole=pvviewer-role \
  --serviceaccount=default:pvviewer

# Create pod
kubectl run pvviewer \
  --image=redis \
  --serviceaccount=pvviewer
```

---

### 3 (Weight: 6) - StorageClass

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: rancher-sc
provisioner: rancher.io/local-path
allowVolumeExpansion: true
volumeBindingMode: WaitForFirstConsumer
```

Apply with: `kubectl apply -f rancher-sc.yaml`

---

### 4 (Weight: 8) - ConfigMap and Deployment

```bash
# Create ConfigMap
kubectl create configmap app-config \
  --namespace=cm-namespace \
  --from-literal=ENV=production \
  --from-literal=LOG_LEVEL=info
```

Edit the Deployment `cm-webapp` to add:

```yaml
spec:
  template:
    spec:
      containers:
        - name: nginx
          envFrom:
            - configMapRef:
                name: app-config
```

---

### 5 (Weight: 8) - PriorityClass

```bash
# Create PriorityClass
kubectl create priorityclass low-priority \
  --value=500000 \
  --description="Low priority class"

# Delete and recreate the pod with priority class
kubectl delete pod lp-pod -n low-priority

# Create new pod with priority class
kubectl run lp-pod \
  --image=redis \
  --namespace=low-priority \
  --overrides='{"spec":{"priorityClassName":"low-priority"}}'
```

Or use YAML:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: lp-pod
  namespace: low-priority
spec:
  priorityClassName: low-priority
  containers:
    - name: lp-pod
      image: redis
```

---

### 6 (Weight: 8) - NetworkPolicy

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: ingress-to-nptest
spec:
  podSelector:
    matchLabels:
      app: np-test-1
  policyTypes:
    - Ingress
  ingress:
    - ports:
        - protocol: TCP
          port: 80
```

Apply with: `kubectl apply -f networkpolicy.yaml`

---

### 7 (Weight: 12) - Taints and Tolerations

```bash
# Taint the node
kubectl taint node node01 env_type=production:NoSchedule

# Create dev-redis pod (will NOT schedule on node01)
kubectl run dev-redis --image=redis:alpine

# Create prod-redis pod with toleration
```

`prod-redis.yaml`:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: prod-redis
spec:
  tolerations:
    - effect: NoSchedule
      key: env_type
      operator: Equal
      value: production
  containers:
    - name: prod-redis
      image: redis:alpine
```

Apply with: `kubectl apply -f prod-redis.yaml`

---

### 8 (Weight: 6) - PVC/PV Binding Issue

Check the PVC and PV access modes. If PV has `ReadWriteOnce` but PVC has
`ReadWriteMany`, edit the PVC:

```bash
kubectl get pv app-pv -o yaml | grep accessModes
kubectl get pvc app-pvc -n storage-ns -o yaml | grep accessModes
```

Edit PVC to match PV's access mode:

```bash
kubectl edit pvc app-pvc -n storage-ns
```

Change to:

```yaml
accessModes:
  - ReadWriteOnce
```

---

### 9 (Weight: 8) - Kubeconfig Fix

Check and fix the server port in `/root/CKA/super.kubeconfig`:

```bash
# View current config
cat /root/CKA/super.kubeconfig
```

Change from:

```yaml
server: https://controlplane:9999
```

To:

```yaml
server: https://controlplane:6443
```

Edit with: `vim /root/CKA/super.kubeconfig`

---

### 10 (Weight: 10) - Deployment Scaling Issue

```bash
# Scale deployment
kubectl scale deploy nginx-deploy --replicas=3

# Check deployment status
kubectl get deployment nginx-deploy

# Check pods
kubectl get pods

# Check controller manager (issue: ImagePullBackOff)
kubectl get pods -n kube-system

# Fix kube-controller-manager
kubectl describe pod -n kube-system kube-controller-manager-controlplane

# Check manifest file
cat /etc/kubernetes/manifests/kube-controller-manager.yaml
```

Fix image issue in the static pod manifest, then wait for pod to restart.

---

### 11 (Weight: 6) - HPA

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: api-hpa
  namespace: api
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: api-deployment
  minReplicas: 1
  maxReplicas: 20
  metrics:
    - type: Pods
      pods:
        metric:
          name: requests_per_second
        target:
          type: AverageValue
          averageValue: "1000"
```

Apply with: `kubectl apply -f hpa.yaml`

---

### 12 (Weight: 6) - HTTPRoute Traffic Split

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: web-route
  namespace: default
spec:
  parentRefs:
    - name: web-gateway
      namespace: default
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /
      backendRefs:
        - name: web-service
          port: 80
          weight: 80
        - name: web-service-v2
          port: 80
          weight: 20
```

Apply with: `kubectl apply -f web-route.yaml`

---

### 13 (Weight: 4) - Helm Upgrade

```bash
# Validate the new chart
helm lint /root/new-version

# Install new version
helm upgrade --install webpage-server-01 /root/new-version

# Or if different release name needed:
helm install webpage-server-02 /root/new-version

# Verify new version is running
helm list
kubectl get pods

# Uninstall old version
helm uninstall webpage-server-01
```

---

### 14 (Weight: 4) - Pod CIDR

```bash
# Get pod CIDR from cluster
kubectl cluster-info dump | grep -m 1 cluster-cidr

# Or from kube-controller-manager
kubectl get nodes -o jsonpath='{.items[*].spec.podCIDR}'

# Or check kube-proxy config
kubectl get configmap kube-proxy -n kube-system -o yaml | grep clusterCIDR

# Output to file
kubectl cluster-info dump | grep -m 1 cluster-cidr | \
  awk -F'"' '{print $4}' > /root/pod-cidr.txt

# Alternative: Get from node spec
kubectl get node controlplane -o jsonpath='{.spec.podCIDR}' > /root/pod-cidr.txt
```

---
