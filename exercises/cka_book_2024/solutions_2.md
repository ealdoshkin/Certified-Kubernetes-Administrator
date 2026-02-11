## Solutions (Mock Exam 2)

### Question 1 Solution

```bash
kubectl config use-context k8sch1-H
mkdir /opt/cka-Q2/

kubectl logs -n cka-exam <pod-name> -c init-cka-q1-httpd > /opt/cka-Q2/init
kubectl logs -n cka-exam <pod-name> > /opt/cka-Q2/main
echo "kubectl logs -n cka-exam <pod-name> --all-containers -f" > /opt/cka-Q2/all
```

---

### Question 2 Solution

```bash
kubectl config use-context k8s-kskd

cat > sc.yaml <<EOF
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: cka-q2-sc
provisioner: kubernetes.io/aws-ebs
parameters:
  type: gp3
volumeBindingMode: WaitForFirstConsumer
EOF
kubectl apply -f sc.yaml

mkdir /opt/cka-Q2/
kubectl get sc --sort-by='.metadata.creationTimestamp' --no-headers | tac > /opt/cka-Q2/k8s-kskd
```

---

### Question 3 Solution

```bash
kubectl config use-context k8s

kubectl create sa cka-sa
kubectl create role cka-pod-role --verb=get --verb=list --resource=pods -n default
kubectl create rolebinding cka-pod-rolebinding --role=cka-pod-role --serviceaccount=default:cka-sa -n default

# Verify
kubectl auth can-i get po --as=system:serviceaccount:default:cka-sa -n default
kubectl auth can-i list po --as=system:serviceaccount:default:cka-sa -n default
```

---

### Question 4 Solution

```bash
kubectl config use-context k8s-dnsl

cat > cka-q4-deploy.yaml <<EOF
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cka-q4-deploy
  namespace: cka-exam
spec:
  replicas: 1
  selector:
    matchLabels:
      app: cka
  template:
    metadata:
      labels:
        app: cka
    spec:
      containers:
      - name: httpd
        image: httpd:alpine
        ports:
        - containerPort: 80
EOF
kubectl apply -f cka-q4-deploy.yaml

kubectl scale deployment cka-q4-deploy --replicas 2 --current-replicas 1 -n cka-exam
kubectl expose deploy -n cka-exam cka-q4-deploy --name cka-q4-service --port=80

mkdir /opt/cka-Q4
kubectl run busybox --image busybox -n cka-exam -- sleep 6000

# DNS lookups
kubectl exec busybox -n cka-exam -- nslookup cka-q4-service > /opt/cka-Q4/service-dns-lookup
kubectl exec busybox -n cka-exam -- nslookup <pod-ip-with-dashes>.cka-exam.pod.cluster.local > /opt/cka-Q4/pod-dns-lookup
```

---

### Question 5 Solution

```bash
kubectl config use-context k8s-RS

kubectl create ns test

cat > cka-q5-pod.yaml <<EOF
apiVersion: v1
kind: Pod
metadata:
  name: multi-app
  namespace: test
spec:
  initContainers:
  - name: init-busybox
    image: busybox
    args: ["sh","-c","date > /app/data/date"]
    volumeMounts:
    - name: cka-volume
      mountPath: /app/data
  containers:
  - name: nginx
    image: nginx:alpine
    args: ["sh","-c","cat /app/data/date && sleep 6000"]
    volumeMounts:
    - name: cka-volume
      mountPath: /app/data
  volumes:
  - name: cka-volume
    emptyDir: {}
EOF
kubectl apply -f cka-q5-pod.yaml
kubectl logs -n test multi-app --all-containers
```

---

### Question 6 Solution

```bash
kubectl config use-context k8s-cswp

# Control plane pod with toleration and nodeName
cat > cka-q6-control-pod.yaml <<EOF
apiVersion: v1
kind: Pod
metadata:
  name: control-plane-pod
spec:
  nodeName: clusterq6-controlplane
  tolerations:
  - effect: NoSchedule
    key: node-role.kubernetes.io/control-plane
  containers:
  - image: httpd
    name: control-plane-pod
EOF
kubectl apply -f cka-q6-control-pod.yaml

# Data plane pod with resource limits
cat > cka-q6-data-pod.yaml <<EOF
apiVersion: v1
kind: Pod
metadata:
  name: data-plane-pod
spec:
  containers:
  - image: httpd
    name: data-plane-pod
    resources:
      limits:
        cpu: 150m
        memory: 250Mi
        ephemeral-storage: 1G
EOF
kubectl apply -f cka-q6-data-pod.yaml
```

---

### Question 7 Solution

```bash
kubectl config use-context k8s-tr-K

kubectl cordon clusterq7-node1
kubectl drain --ignore-daemonsets clusterq7-node1

mkdir /opt/cka-Q7
echo "NodeNotSchedulable" > /opt/cka-Q7/node-status

kubectl uncordon clusterq7-node1
```

---

### Question 8 Solution

```bash
kubectl config use-context k8s-secSS

kubectl create configmap cm-7 --from-literal=app=cka-7 --from-literal=exam=cka -n space
kubectl create configmap cm-8 --from-literal=tier1=0-5 --from-literal=tier2=6-8 --from-literal=tier3=9-10 -n space

cat > cka-q8-pod.yaml <<EOF
apiVersion: v1
kind: Pod
metadata:
  name: voyager
  namespace: space
spec:
  containers:
  - image: httpd
    name: voyager
    env:
    - name: APP
      valueFrom:
        configMapKeyRef:
          name: cm-7
          key: app
    - name: EXAM
      valueFrom:
        configMapKeyRef:
          name: cm-7
          key: exam
    volumeMounts:
    - name: cka-q8
      mountPath: "/cka-Q8/data"
  volumes:
  - name: cka-q8
    configMap:
      name: cm-8
      items:
      - key: tier1
        path: tier1
      - key: tier2
        path: tier2
      - key: tier3
        path: tier3
EOF
kubectl apply -f cka-q8-pod.yaml

mkdir /opt/cka-Q8/
kubectl exec -n space voyager -it -- env > /opt/cka-Q8/env-vars
kubectl exec -n space voyager -it -- ls -l /cka-Q8/data > /opt/cka-Q8/volume-files
```

---

### Question 9 Solution

```bash
kubectl config use-context k8s-po-NE

ssh clusterq9-node2
apt update
apt install kubelet=1.28.2-1.1 kubectl=1.28.2-1.1
service kubelet restart

# On control plane
ssh clusterq9-controlplane
kubeadm token create --print-join-command

# Back on node2
kubeadm join 172.30.1.2:6443 --token <token> --discovery-token-ca-cert-hash sha256:<hash>
```

---

### Question 10 Solution

```bash
kubectl config use-context k8s-K

kubectl get deploy -n app
kubectl get events -n app
kubectl get cm -n app

# Found issue: ConfigMap key is 'regions' not 'region'
kubectl edit deploy app-deployment -n app
# Change: key: region  →  key: regions

kubectl get deploy -n app
```

---

### Question 11 Solution

```bash
kubectl config use-context k8s-po-SW

mkdir /opt/cka-Q11/
kubectl get events -A --sort-by='.lastTimestamp' | grep -i error | tac > /opt/cka-Q11/error-events
```

---

### Question 12 Solution

```bash
kubectl config use-context k8s-gfp2

cat > cka-q12-netpol.yaml <<EOF
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: web-q12-netpol
  namespace: default
spec:
  podSelector:
    matchLabels:
      app: cka-q12
      type: web
  policyTypes:
  - Ingress
  ingress:
  - ports:
    - protocol: TCP
      port: 80
---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: api-q12-netpol
  namespace: default
spec:
  podSelector:
    matchLabels:
      app: cka-q12
      type: api
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: cka-q12
          type: web
    ports:
    - protocol: TCP
      port: 8080
EOF
kubectl apply -f cka-q12-netpol.yaml

# Test with busybox pod
kubectl run test --image busybox -- "sh" "-c" "sleep 3600"
kubectl exec test -it -- sh
# wget -O- 192.168.1.3  # Should work (web:80)
# wget -O- 192.168.1.4:8080  # Should fail from test pod
```

---

### Question 13 Solution

```bash
kubectl config use-context k8s-upd-CP

kubectl drain clusterq13-controlplane --ignore-daemonsets

ssh clusterq13-controlplane
apt update
apt install kubeadm=1.28.2-1.1 kubelet=1.28.2-1.1 kubectl=1.28.2-1.1

kubeadm upgrade plan
kubeadm upgrade apply v1.28.2

systemctl restart kubelet
exit

kubectl uncordon clusterq13-controlplane
```

---

### Question 14 Solution

```bash
kubectl create ns section
kubectl run junction --image nginx:alpine -l env=prod,dept=field-services --port 80 -n section
kubectl expose pod junction -n section --name=section-junction --selector='env=prod' --port 12345 --target-port 80
```

---

### Question 15 Solution

```bash
kubectl config use-context k8s-ns-rl

kubectl create ns limits

cat > cka-q15-quota.yaml <<EOF
apiVersion: v1
kind: ResourceQuota
metadata:
  name: cka-quota
  namespace: limits
spec:
  hard:
    memory: 2G
    pods: "12"
EOF
kubectl apply -f cka-q15-quota.yaml

cat > cka-q15-limits.yaml <<EOF
apiVersion: v1
kind: LimitRange
metadata:
  name: cka-limits
  namespace: limits
spec:
  limits:
  - max:
      cpu: 300m
    type: Container
EOF
kubectl apply -f cka-q15-limits.yaml

# Attempt to create violating pod
cat > cka-q15-pod.yaml <<EOF
apiVersion: v1
kind: Pod
metadata:
  name: cka-q15-pod
  namespace: limits
spec:
  containers:
  - name: cka-q15-pod
    image: httpd
    resources:
      requests:
        memory: 3G
        cpu: 200m
EOF

mkdir /opt/cka-Q15
kubectl apply -f cka-q15-pod.yaml 2>&1 | tee /opt/cka-Q15/limits-error
```

---

### Question 16 Solution

```bash
kubectl config use-context k8s-ns-LKS

cat > cka-q16-deploy.yaml <<EOF
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cka-deploy
spec:
  replicas: 1
  selector:
    matchLabels:
      app: cka-deploy
  template:
    metadata:
      labels:
        app: cka-deploy
    spec:
      containers:
      - image: nginx:alpine
        name: nginx
        volumeMounts:
        - name: cka-q16-vol
          mountPath: /cka/data
      volumes:
      - name: cka-q16-vol
        persistentVolumeClaim:
          claimName: cka-pvc
EOF
kubectl apply -f cka-q16-deploy.yaml

kubectl expose deploy cka-deploy --name cka-service --port 8080 --target-port 80

# Test service
kubectl run test --image busybox -- "sh" "-c" "sleep 3600"
kubectl exec test -it -- sh
# wget -O- cka-service:8080
```
