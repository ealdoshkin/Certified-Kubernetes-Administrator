## Solutions (Mock Exam 1)

### Question 1 Solution

```bash
kubectl config use-context k8sch1-H
kubectl create ns busy
kubectl run busy-time -n busy --image nginx:alpine3.18-slim --labels="exam=cka,question=1" --dry-run=client -o yaml > q1.yaml
# Edit q1.yaml to add:
# - container name: busy-time-container
# - nodeSelector: node-role.kubernetes.io/control-plane: ""
# - tolerations for control-plane taint
kubectl apply -f q1.yaml
kubectl get po -n busy
```

---

### Question 2 Solution

```bash
kubectl config use-context k8svl-L
cd /opt/exam/101/
kubectl get nodes -o name > node-names
kubectl get no clusterq2-node1 -o json > clusterq2-node1.json
kubectl get no clusterq2-node2 -o json > clusterq2-node2.json
```

---

### Question 3 Solution

```bash
kubectl config use-context k8ssd

# Create PV
cat > pv.yaml <<EOF
apiVersion: v1
kind: PersistentVolume
metadata:
  name: cka-pv-q3
spec:
  storageClassName: cka-manual-mapping
  capacity:
    storage: 5Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: /mnt/app/data
EOF
kubectl apply -f pv.yaml

# Create PVC
cat > pvc.yaml <<EOF
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: cka-pvc-q3
spec:
  accessModes:
    - ReadWriteOnce
  volumeMode: Filesystem
  resources:
    requests:
      storage: 5Gi
  storageClassName: cka-manual-mapping
EOF
kubectl apply -f pvc.yaml
```

---

### Question 4 Solution

```bash
kubectl config use-context k8scicd
kubectl create sa cicd-sa -n cicd
kubectl create clusterrole cicd-clusterrole --verb=create --resource=deployment
kubectl create rolebinding cicd-clusterrolebinding --clusterrole=cicd-clusterrole --serviceaccount=cicd:cicd-sa -n cicd
kubectl auth can-i create deploy --as=system:serviceaccount:cicd:cicd-sa -n cicd
```

---

### Question 5 Solution

```bash
kubectl config use-context k8sdld
ssh clusterq5-controlplane
cd /etc/kubernetes/manifests
kubectl run cka-static-pod --image httpd:2.4.58-alpine --dry-run=client -o yaml > cka-static-pod.yaml
# Wait for kubelet to create the pod
kubectl get po -o wide
```

---

### Question 6 Solution

```bash
kubectl config use-context k8sws-s
kubectl expose deploy web-server -n app --name web-portal --type NodePort --port 8080
kubectl edit svc web-portal -n app  # Change nodePort to 32001
kubectl scale --current-replicas=2 --replicas=3 deployment/web-server -n app
kubectl get ep -n app
```

---

### Question 7 Solution

```bash
kubectl config use-context k8snsdy
kubectl create ns customer
kubectl run source-app -n live --image httpd

cat > netpol.yaml <<EOF
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: cka-q7-netpol
  namespace: live
spec:
  podSelector:
    matchLabels:
      run: source-app
  policyTypes:
  - Ingress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: customer
    ports:
    - protocol: TCP
      port: 80
EOF
kubectl apply -f netpol.yaml

# Test from customer namespace
kubectl run test --image alpine/curl -n customer -- curl <source-app-ip>
```

---

### Question 8 Solution

```bash
kubectl config use-context k8s-tadL
ssh clusterq8-controlplane

# Backup etcd
ETCDCTL_API=3 etcdctl snapshot save --cert=/etc/kubernetes/pki/etcd/server.crt \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt --key=/etc/kubernetes/pki/etcd/server.key \
  --endpoints=https://127.0.0.1:2379 /opt/cka-etcd-backup.db

# Create test pod
kubectl run bookworm --image nginx:bookworm

# Restore etcd
ETCDCTL_API=3 etcdctl snapshot restore --data-dir=/var/lib/etcd-backup \
  --cert=/etc/kubernetes/pki/etcd/server.crt --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --key=/etc/kubernetes/pki/etcd/server.key --endpoints=https://127.0.0.1:2379 \
  /opt/cka-etcd-backup.db

# Update etcd.yaml to use /var/lib/etcd-backup
vi /etc/kubernetes/manifests/etcd.yaml
# Change data-dir and volume mounts to /var/lib/etcd-backup

# Verify bookworm pod is gone
kubectl get po
```

---

### Question 9 Solution

```bash
kubectl config use-context k8s-sas-O
ssh clusterq9-controlplane

# Answers:
# 1. kubectl version | grep Kustomize
# 2. cat /etc/kubernetes/manifests/kube-apiserver.yaml | grep service-cluster-ip-range
# 3. kubectl get no -o wide | grep CONTAINER-RUNTIME
# 4. kubectl cluster-info | grep CoreDNS
# 5. ls -l /etc/cni/net.d

cat > /opt/cka-Q9-answers <<EOF
1) v5.0.4-0.20230601165947-6ce0bf390ce3
2) 10.96.0.0/12
3) containerd
4) https://172.30.1.2:6443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
5) /etc/cni/net.d
EOF
```

---

### Question 10 Solution

```bash
kubectl config use-context k8s-rH-csc
ssh clusterq10-controlplane
kubeadm certs check-expiration

echo "20/11/2024" > /opt/cka-Q10-API-Cert-Expiry.txt
echo "11/11/2033" > /opt/cka-Q10-API-CA-Expiry.txt
echo "kubeadm certs renew apiserver" > /opt/cka-Q10-API-Cert-Renew.txt
```

---

### Question 11 Solution

```bash
kubectl config use-context k8s-jsnp-TH
ssh clusterq11-controlplane

kubectl get po -n kube-system -o=jsonpath='{range .items[*]}{.spec.containers[*].image},{"\t"}{.status.containerStatuses[*].restartCount}{"\n"}{end}' \
  --sort-by=.status.containerStatuses[*].restartCount --no-headers | tac > /opt/cka-Q11-image-restarts

# Add header manually
# Image Name Restarts
```

---

### Question 12 Solution

```bash
kubectl config use-context k8s-ssT

cat > cka-Q12-pod.yaml <<EOF
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  securityContext:
    runAsUser: 34
    runAsGroup: 42
  containers:
  - name: nginx
    image: nginx
    args: ["sleep", "10m"]
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        add: ["NET_ADMIN"]
EOF
kubectl apply -f cka-Q12-pod.yaml
```

---

### Question 13 Solution

```bash
kubectl config use-context k8skcq-ns

# Check the difference between working and broken config
kubectl cluster-info  # Shows port 6443

# Fix the server port in trial-kube-config
vi /opt/trial-kube-config
# Change: server: https://172.30.1.2
# To: server: https://172.30.1.2:6443

kubectl get svc --kubeconfig=/opt/trial-kube-config
```

---

### Question 14 Solution

```bash
kubectl config use-context k8s-recop

# Rollback deployment
kubectl rollout undo deploy cka-q14-deploy -n web-service

# Export, delete, and recreate with new labels
kubectl get deploy -n web-service cka-q14-deploy -o yaml > cka-q14-deploy.yaml
kubectl delete deploy -n web-service cka-q14-deploy --force --grace-period 0

# Edit cka-q14-deploy.yaml to add labels: action=recovered, program=cka
# to metadata.labels, spec.selector.matchLabels, and spec.template.metadata.labels
kubectl apply -f cka-q14-deploy.yaml

# Expose service with only the two new labels
kubectl expose deploy cka-q14-deploy --name=cka-q14-deploy -n web-service --port=80 --target-port=80
kubectl edit svc cka-q14-deploy -n web-service  # Remove app label, keep only action=recovered and program=cka
```

---

### Question 15 Solution

```bash
kubectl config use-context k8s-ssh
cd /opt/cka-Q15/

# Create CSR
cat > csr.yaml <<EOF
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: khippy
spec:
  request: $(cat khippy.csr | base64 | tr -d "\n")
  signerName: kubernetes.io/kube-apiserver-client
  expirationSeconds: 86400
  usages:
  - client auth
EOF
kubectl apply -f csr.yaml
kubectl certificate approve khippy

# Create permissions
kubectl create clusterrole cka-cr-pods --verb=create,get,list,watch --resource=pods
kubectl create clusterrolebinding cka-crb-pods --clusterrole=cka-cr-pods --user=khippy

# Verify
kubectl auth can-i get pods --as khippy
kubectl auth can-i create pods --as khippy -n kube-system
```

---

### Question 16 Solution

```bash
kubectl config use-context k8s-e8p

cat > cka-q16-httpd.yaml <<EOF
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cka-q16-httpd
spec:
  replicas: 3
  selector:
    matchLabels:
      app: cka-q16-httpd
  template:
    metadata:
      labels:
        app: cka-q16-httpd
    spec:
      initContainers:
      - name: init-cka-q16-httpd
        image: busybox
        command: ['sh', '-c', 'sleep 10']
      containers:
      - name: httpd
        image: httpd
        ports:
        - containerPort: 80
        readinessProbe:
          httpGet:
            path: /
            port: 80
          initialDelaySeconds: 3
          periodSeconds: 3
        livenessProbe:
          exec:
            command:
            - 'true'
EOF
kubectl apply -f cka-q16-httpd.yaml
```
