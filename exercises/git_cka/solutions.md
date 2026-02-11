## Solutions (Answers)

### Solution 1: Schedule Pod on Master Node

**Inspect taints/labels:**

```bash
kubectl get nodes
kubectl describe node cluster1-master1 | grep -i taint
kubectl get node cluster1-master1 --show-labels
```

**Create YAML:**

```bash
kubectl run pod1 --image=httpd:2.4.41-alpine -o yaml --dry-run=client > pod1.yaml
```

**Edit and apply:**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod1
spec:
  containers:
    - name: pod1-container
      image: httpd:2.4.41-alpine
  tolerations:
    - key: node-role.kubernetes.io/master
      effect: NoSchedule
  nodeSelector:
    node-role.kubernetes.io/master: ""
```

```bash
kubectl apply -f pod1.yaml
kubectl get pod pod1 -o wide
echo "Master nodes are tainted to avoid scheduling regular workloads" > /opt/course/2/master_schedule_reason
```

---

### Solution 2: Storage with PV, PVC, Deployment

**PV:**

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: safari-pv
spec:
  capacity:
    storage: 2Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: "/Volumes/Data"
```

**PVC:**

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: safari-pvc
  namespace: project-tiger
spec:
  accessModes: ["ReadWriteOnce"]
  resources:
    requests:
      storage: 2Gi
```

**Deployment:**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: safari
  namespace: project-tiger
spec:
  replicas: 1
  selector:
    matchLabels:
      app: safari
  template:
    metadata:
      labels:
        app: safari
    spec:
      volumes:
        - name: data
          persistentVolumeClaim:
            claimName: safari-pvc
      containers:
        - name: container
          image: httpd:2.4.41-alpine
          volumeMounts:
            - name: data
              mountPath: /tmp/safari-data
```

**Apply & verify:**

```bash
kubectl apply -f pv.yaml
kubectl apply -f pvc.yaml
kubectl apply -f deploy.yaml
kubectl -n project-tiger get pv,pvc,deploy,pods -o wide
```

---

### Solution 3: RBAC with ServiceAccount, Role, RoleBinding

```bash
kubectl -n project-hamster create sa processor
kubectl -n project-hamster create role processor --verb=create --resource=secrets --resource=configmaps
kubectl -n project-hamster create rolebinding processor --role=processor --serviceaccount=project-hamster:processor
```

**Verify:**

```bash
kubectl -n project-hamster auth can-i create secret --as system:serviceaccount:project-hamster:processor
kubectl -n project-hamster auth can-i create configmap --as system:serviceaccount:project-hamster:processor
kubectl -n project-hamster auth can-i delete secret --as system:serviceaccount:project-hamster:processor
```

---

### Solution 4: DaemonSet on All Nodes

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: ds-important
  namespace: project-tiger
  labels:
    id: ds-important
    uuid: 18426a0b-5f59-4e10-923f-c0e078e82462
spec:
  selector:
    matchLabels:
      id: ds-important
  template:
    metadata:
      labels:
        id: ds-important
    spec:
      tolerations:
        - key: node-role.kubernetes.io/master
          effect: NoSchedule
      containers:
        - name: ds-important
          image: httpd:2.4-alpine
          resources:
            requests:
              cpu: 10m
              memory: 10Mi
```

**Verify:**

```bash
kubectl -n project-tiger get ds
kubectl -n project-tiger get pods -o wide -l id=ds-important
```

---

### Solution 5: Deployment with Anti-Affinity or Spread Constraints

**Solution A — podAntiAffinity:**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deploy-important
  namespace: project-tiger
  labels:
    id: very-important
spec:
  replicas: 3
  selector:
    matchLabels:
      id: very-important
  template:
    metadata:
      labels:
        id: very-important
    spec:
      affinity:
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            - labelSelector:
                matchExpressions:
                  - key: id
                    operator: In
                    values: ["very-important"]
              topologyKey: kubernetes.io/hostname
      containers:
        - name: container1
          image: nginx:1.17.6-alpine
        - name: container2
          image: kubernetes/pause
```

**Solution B — topologySpreadConstraints:**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deploy-important
  namespace: project-tiger
  labels:
    id: very-important
spec:
  replicas: 3
  selector:
    matchLabels:
      id: very-important
  template:
    metadata:
      labels:
        id: very-important
    spec:
      topologySpreadConstraints:
        - maxSkew: 1
          topologyKey: kubernetes.io/hostname
          whenUnsatisfiable: DoNotSchedule
          labelSelector:
            matchLabels:
              id: very-important
      containers:
        - name: container1
          image: nginx:1.17.6-alpine
        - name: container2
          image: kubernetes/pause
```

**Verify behavior:**

```bash
kubectl -n project-tiger get deploy,pods -o wide -l id=very-important
```

---

### Solution 6: Multi-Container Pod with Shared Volume

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: multi-container-playground
spec:
  volumes:
    - name: vol
      emptyDir: {}
  containers:
    - name: c1
      image: nginx:1.17.6-alpine
      env:
        - name: MY_NODE_NAME
          valueFrom:
            fieldRef:
              fieldPath: spec.nodeName
      volumeMounts:
        - name: vol
          mountPath: /vol
    - name: c2
      image: busybox:1.31.1
      command:
        ["sh", "-c", "while true; do date >> /vol/date.log; sleep 1; done"]
      volumeMounts:
        - name: vol
          mountPath: /vol
    - name: c3
      image: busybox:1.31.1
      command: ["sh", "-c", "tail -f /vol/date.log"]
      volumeMounts:
        - name: vol
          mountPath: /vol
```

**Apply & verify:**

```bash
kubectl apply -f pod.yaml
kubectl get pod multi-container-playground
kubectl exec multi-container-playground -c c1 -- env | grep MY_NODE_NAME
kubectl logs multi-container-playground -c c3 | head
```

---

### Solution 7: Secrets: Mount + Env Vars

**Create namespace & Secret #1:**

```bash
kubectl create ns secret
sed -e 's/namespace: .*/namespace: secret/' /opt/course/19/secret1.yaml > /tmp/secret1.yaml
kubectl apply -f /tmp/secret1.yaml
```

**Create Secret #2:**

```bash
kubectl -n secret create secret generic secret2 --from-literal=user=user1 --from-literal=pass=1234
```

**Pod:**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secret-pod
  namespace: secret
spec:
  tolerations:
    - key: node-role.kubernetes.io/master
      effect: NoSchedule
  containers:
    - name: secret-pod
      image: busybox:1.31.1
      command: ["sh", "-c", "sleep 1d"]
      env:
        - name: APP_USER
          valueFrom:
            secretKeyRef:
              name: secret2
              key: user
        - name: APP_PASS
          valueFrom:
            secretKeyRef:
              name: secret2
              key: pass
      volumeMounts:
        - name: secret1
          mountPath: /tmp/secret1
          readOnly: true
  volumes:
    - name: secret1
      secret:
        secretName: secret1
```

**Verify:**

```bash
kubectl -n secret apply -f pod.yaml
kubectl -n secret exec secret-pod -- env | grep APP_
kubectl -n secret exec secret-pod -- ls -l /tmp/secret1
```

---

### Solution 8: Upgrade Node and Join Cluster

**On control plane, find version & get join command:**

```bash
kubectl get nodes -o wide
sudo kubeadm token create --print-join-command
```

**On the target worker (`cluster3-worker2`):**

```bash
sudo apt-get update
sudo apt-get install -y kubelet=1.33.0-00 kubeadm=1.33.0-00 kubectl=1.33.0-00
sudo systemctl enable --now kubelet
```

**If the node was previously initialized, reset first:**

```bash
sudo kubeadm reset -f
sudo rm -rf ~/.kube
```

**Join:**

```bash
sudo kubeadm join <CP_IP>:6443 --token <TOKEN> --discovery-token-ca-cert-hash sha256:<HASH>
```

**Back on control plane:**

```bash
kubectl get nodes
```

---

### Solution 9: NetworkPolicy with Egress Control

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: np-backend
  namespace: project-snake
spec:
  podSelector:
    matchLabels:
      app: backend
  policyTypes:
    - Egress
  egress:
    - to:
        - podSelector:
            matchLabels:
              app: db1
      ports:
        - protocol: TCP
          port: 1111
    - to:
        - podSelector:
            matchLabels:
              app: db2
      ports:
        - protocol: TCP
          port: 2222
```

**Test:**

```bash
kubectl -n project-snake exec backend-0 -- curl -s <db1-ip>:1111
kubectl -n project-snake exec backend-0 -- curl -s <db2-ip>:2222
kubectl -n project-snake exec backend-0 -- curl -s <vault-ip>:3333
```

---

### Solution 10: Etcd Backup and Restore

**On control plane, save snapshot:**

```bash
export ETCDCTL_API=3
etcdctl --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  snapshot save /tmp/etcd-backup.db
```

**Create a test Pod:**

```bash
kubectl run test --image=nginx
kubectl get pods -l run=test -w
```

**Stop control plane:**

```bash
sudo mkdir -p /root/manifests-bak
sudo mv /etc/kubernetes/manifests/* /root/manifests-bak/
```

**Restore snapshot to a fresh data dir:**

```bash
etcdctl snapshot restore /tmp/etcd-backup.db --data-dir /var/lib/etcd-backup
```

**Point etcd manifest to the new data dir (`/etc/kubernetes/manifests/etcd.yaml`):**

```yaml
hostPath:
  path: /var/lib/etcd-backup
  type: DirectoryOrCreate
```

**Start control plane again:**

```bash
sudo mv /root/manifests-bak/* /etc/kubernetes/manifests/
kubectl get pods -A
kubectl get pods -l run=test
```
