# CKA Mock Exam 1 with Solutions

Inspired: CKA - G.R. Bayfield - 2024

### Question 1

**Task weight: 4% (not displayed in exam)**

**Use context:** k8sch1-H

**Task:**
Create a pod using image `nginx:alpine3.18-slim` in the namespace `busy`, configured with labels `exam=cka` and `question=1`. The pod and its container must be named `busy-time` and `busy-time-container`. This pod should only be permitted on the controlplane master node. Ensure that the pod is running.

**Solution:**

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

### Question 2

**Task weight: 3% (not displayed in exam)**

**Use context:** k8svl-L

**Task:**
Use the kubectl command to output a list of all node names and store in a file named `/opt/exam/101/node-names`. Store the details of nodes not using the taint `node-role.kubernetes.io/control-plane:NoSchedule` in individual json files in the same directory. Use the name of the node as the filename.

**Solution:**

```bash
kubectl config use-context k8svl-L
cd /opt/exam/101/
kubectl get nodes -o name > node-names
kubectl get no clusterq2-node1 -o json > clusterq2-node1.json
kubectl get no clusterq2-node2 -o json > clusterq2-node2.json
```

---

### Question 3

**Task weight: 6% (not displayed in exam)**

**Use context:** k8ssd

**Task:**
Create a persistent volume of type hostPath named `cka-pv-q3` with a storage capacity of 5Gi, ReadWriteOnce access mode, and file-path location `/mnt/app/data`. Define a storage class and name the storage class `cka-manual-mapping`. Create a new PersistentVolumeClaim named `cka-pvc-q3` in the default namespace. Ensure this PVC becomes bound to the persistent volume.

**Solution:**

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

### Question 4

**Task weight: 5% (not displayed in exam)**

**Use context:** k8scicd

**Task:**
A new service account `cicd-sa` in the existing `cicd` namespace will require create permission for deployments. Create a ClusterRole named `cicd-clusterrole` to provision this access and restrict its use to only this service account in the cicd namespace. Ensure that the new service account has the requested access permissions.

**Solution:**

```bash
kubectl config use-context k8scicd
kubectl create sa cicd-sa -n cicd
kubectl create clusterrole cicd-clusterrole --verb=create --resource=deployment
kubectl create rolebinding cicd-clusterrolebinding --clusterrole=cicd-clusterrole --serviceaccount=cicd:cicd-sa -n cicd
kubectl auth can-i create deploy --as=system:serviceaccount:cicd:cicd-sa -n cicd
```

---

### Question 5

**Task weight: 5% (not displayed in exam)**

**Use context:** k8sdld

**Task:**
Create a static pod named `cka-static-pod` on the control plane node using the image `httpd:2.4.58-alpine`. Ensure this new static pod achieves the running state in the default namespace.

**Solution:**

```bash
kubectl config use-context k8sdld
ssh clusterq5-controlplane
cd /etc/kubernetes/manifests
kubectl run cka-static-pod --image httpd:2.4.58-alpine --dry-run=client -o yaml > cka-static-pod.yaml
# Wait for kubelet to create the pod
kubectl get po -o wide
```

---

### Question 6

**Task weight: 5% (not displayed in exam)**

**Use context:** k8sws-s

**Task:**
Expose the existing application `web-server` as the `web-portal` service available on port 32001 on each node in the cluster. The web server application listens on port 8080. Ensure that the service has 3 endpoints defined.

**Solution:**

```bash
kubectl config use-context k8sws-s
kubectl expose deploy web-server -n app --name web-portal --type NodePort --port 8080
kubectl edit svc web-portal -n app  # Change nodePort to 32001
kubectl scale --current-replicas=2 --replicas=3 deployment/web-server -n app
kubectl get ep -n app
```

---

### Question 7

**Task weight: 6% (not displayed in exam)**

**Use context:** k8snsdy

**Task:**
Deploy a pod named `source-app` in the existing namespace `live` using the latest httpd image. Ensure that only pods in a new namespace named `customer` are able to access this pod only on port 80. Confirm that the required connectivity has been established using a pod named `test` running the alpine/curl image.

**Solution:**

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

### Question 8

**Task weight: 10% (not displayed in exam)**

**Use context:** k8s-tadL

**Task:**
Take a backup of the etcd cluster and store it on the control plane node in the directory `/opt/cka-etcd-backup.db`. Name the backup `cka-etcd-backup.db`. Once complete, create a pod named `bookworm` using the `nginx:bookworm` image in the default namespace. Finally, restore the etcd backup and confirm the bookworm pod is no longer present.

**Solution:**

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

### Question 9

**Task weight: 5% (not displayed in exam)**

**Use context:** k8s-sas-O

**Task:**
Examine your cluster and answer the following questions. Write each answer into a single file named `/opt/cka-Q9-answers` following the format as shown below:

1. What is the current version of Kustomize?
2. What is the Kubernetes service cluster IP range?
3. What is the container runtime name?
4. What address is the CoreDNS service running at?
5. What is the default directory location holding CNI plugin configuration file(s)?

**Solution:**

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

### Question 10

**Task weight: 4% (not displayed in exam)**

**Use context:** k8s-rH-csc

**Task:**
Use the kubeadm command to find the TLS certificate expiry dates for the running Kubernetes API server and the applicable certifying authority. Write these dates into the `/opt/cka-Q10-API-Cert-Expiry.txt` and `/opt/cka-Q10-API-CA-Expiry.txt` files respectively using the DD/MM/YYYY format. Then write a kubeadm command to renew the API server TLS certificate in the file `/opt/cka-Q10-API-Cert-Renew.txt`.

**Solution:**

```bash
kubectl config use-context k8s-rH-csc
ssh clusterq10-controlplane
kubeadm certs check-expiration

echo "20/11/2024" > /opt/cka-Q10-API-Cert-Expiry.txt
echo "11/11/2033" > /opt/cka-Q10-API-CA-Expiry.txt
echo "kubeadm certs renew apiserver" > /opt/cka-Q10-API-Cert-Renew.txt
```

---

### Question 11

**Task weight: 10% (not displayed in exam)**

**Use context:** k8s-jsnp-TH

**Task:**
Generate a list displaying each image name with the number of restarts for each running pod in the kube-system namespace. Order the list by the restarts count in descending order, and output into the `/opt/cka-Q11-image-restarts` file in the following repeating line format under the single line header as shown:

```
Image Name Restarts
```

**Solution:**

```bash
kubectl config use-context k8s-jsnp-TH
ssh clusterq11-controlplane

kubectl get po -n kube-system -o=jsonpath='{range .items[*]}{.spec.containers[*].image},{"\t"}{.status.containerStatuses[*].restartCount}{"\n"}{end}' \
  --sort-by=.status.containerStatuses[*].restartCount --no-headers | tac > /opt/cka-Q11-image-restarts

# Add header manually
# Image Name Restarts
```

---

### Question 12

**Task weight: 5% (not displayed in exam)**

**Use context:** k8s-ssT

**Task:**
Create a pod named `nginx` using the nginx image in the default namespace. Ensure all processes run as the user ID 34, with group ID 42. The container should sleep for 10 minutes and be explicitly configured to prevent any escalation of its privileges. Grant the network administration privilege.

**Solution:**

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

### Question 13

**Task weight: 8% (not displayed in exam)**

**Use context:** k8skcq-ns

**Task:**
A replacement kubeconfig file named `trial-kube-config` is located in the `/opt` directory. However the test team's attempted use of its single context fails. Investigate and fix this issue.

**Solution:**

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

### Question 14

**Task weight: 10% (not displayed in exam)**

**Use context:** k8s-recop

**Task:**
An update of the image associated with an existing deployment named `cka-q14-deploy` has not provisioned the expected functional improvements in the `web-service` namespace. Revert the deployment to the previous version and add the labels `action=recovered` and `program=cka` to both the deployment and running pods. Deploy a service with the same name and namespace based only on these two new tags exposing port 80.

**Solution:**

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

### Question 15

**Task weight: 8% (not displayed in exam)**

**Use context:** k8s-ssh

**Task:**
Create a new user named `khippy`, based on the private key and user certificate signing request provisioned in the `/opt/cka-Q15/` directory. Grant this new user permission to create, get, list, and watch pods in any namespace.

**Solution:**

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

### Question 16

**Task weight: 6% (not displayed in exam)**

**Use context:** k8s-e8p

**Task:**
Create a deployment named `cka-q16-deploy` using the latest httpd image with 3 replicas. Instruct an init container using the busybox image to sleep for 10 seconds. Configure a readiness probe to call the base path `/` on the default http port, with an initial delay and period, both set to 3 seconds. Also, implement a liveness probe, which can just return true.

**Solution:**

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

---

## Chapter 9: CKA Mock Exam 2 with Solutions

### Question 1

**Task weight: 2% (not displayed in exam)**

**Use context:** k8sch1-H

**Task:**
Access the logs for the pod associated with the deployment named `cka-q1-deploy` running in the `cka-exam` namespace. Output the log for the init container to `/opt/cka-Q2/init`. Output the log for the main container to `/opt/cka-Q2/main`. Write a kubectl command to follow all pod logging to `/opt/cka-Q2/all`.

**Solution:**

```bash
kubectl config use-context k8sch1-H
mkdir /opt/cka-Q2/

kubectl logs -n cka-exam <pod-name> -c init-cka-q1-httpd > /opt/cka-Q2/init
kubectl logs -n cka-exam <pod-name> > /opt/cka-Q2/main
echo "kubectl logs -n cka-exam <pod-name> --all-containers -f" > /opt/cka-Q2/all
```

---

### Question 2

**Task weight: 6% (not displayed in exam)**

**Use context:** k8s-kskd

**Task:**
Create a storage class named `cka-q2-sc` with the `kubernetes.io/aws-ebs` provisioner setting the type parameter to `gp3`. Ensure the volume binding mode is set to `WaitForFirstConsumer`. Next, list all the available storage classes sorted by age with the newest first, writing this output to `/opt/cka-Q2/k8s-kskd`.

**Solution:**

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

### Question 3

**Task weight: 5% (not displayed in exam)**

**Use context:** k8s

**Task:**
Create a new service account named `cka-sa` in the default namespace and provide permissions to get and list pods only in its own namespace.

**Solution:**

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

### Question 4

**Task weight: 12% (not displayed in exam)**

**Use context:** k8s-dnsl

**Task:**
Create a deployment named `cka-q4-deploy` in the existing `cka-exam` namespace using the `httpd:alpine` image with 1 replica and use the label `app=cka`. Once running, scale the deployment to 2 replicas using kubectl. Next, expose `cka-q4-deploy` as an internal service named `cka-q4-service` on port 80. Finally, perform a DNS lookup from within the cluster of both the service and a pod, writing output to new `service-dns-lookup` and `pod-dns-lookup` files on the `/opt/cka-Q4` directory.

**Solution:**

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

### Question 5

**Task weight: 4% (not displayed in exam)**

**Use context:** k8s-RS

**Task:**
Create a pod named `multi-app` in a new `test` namespace that runs a busybox image to write the current date to a persistent volume of type `emptyDir` on path `/app/data`. Ensure that the primary container with image `nginx:alpine` outputs this date to the pod log.

**Solution:**

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

### Question 6

**Task weight: 5% (not displayed in exam)**

**Use context:** k8s-cswp

**Task:**
Create two pods using the httpd image named `control-plane-pod` and `data-plane-pod`. Ensure the first pod runs on the master node in the cluster and the second on the single worker node. Resource limits should be applied to the worker node pod in the form of 150 millicore CPU, 250-mebibyte memory, and 1-gigabyte ephemeral storage.

**Solution:**

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

### Question 7

**Task weight: 6% (not displayed in exam)**

**Use context:** k8s-tr-K

**Task:**
To prepare for scheduled maintenance, configure the `clusterq7-node1` to ensure no new pods can be scheduled to run on it. Next, gracefully reschedule all non-daemonset pods running on this node. When this process has successfully completed write the status of the node as described in the node event logging to `/opt/cka-Q7/node-status`. Finally return to the node to its original operational status.

**Solution:**

```bash
kubectl config use-context k8s-tr-K

kubectl cordon clusterq7-node1
kubectl drain --ignore-daemonsets clusterq7-node1

mkdir /opt/cka-Q7
echo "NodeNotSchedulable" > /opt/cka-Q7/node-status

kubectl uncordon clusterq7-node1
```

---

### Question 8

**Task weight: 6% (not displayed in exam)**

**Use context:** k8s-secSS

**Task:**
Create a ConfigMap named `cm-7` containing entries `app=cka-7` and `exam=cka` in the existing namespace `space`. Create a pod named `voyager` using image `httpd:alpine3.18` in the same namespace and reference the config map data as environment variables, converting each key name into uppercase to derive the corresponding environment variable name. Create a second ConfigMap named `cm-8` with entries `tier1=0-5`, `tier2=6-8`, and `tier3=9-10`. Mount this second config map as volume data, with each separate individual file having the name of a specific key and holding the corresponding value. Access the pod and output all environment variables to `/opt/cka-Q8/env-vars` on the same node. Also, list the file contents of the mounted directory to `/opt/cka-Q8/volume-files`.

**Solution:**

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

### Question 9

**Task weight: 12% (not displayed in exam)**

**Use context:** k8s-po-NE

**Task:**
The Kubernetes server environment has one node that is at an earlier release of Kubernetes and is not part of the cluster. Upgrade this node `clusterq9-node2` to the same version of Kubernetes as the rest of the cluster. Finally, add this node to the existing cluster. Kubeadm is already installed as per the required version.

**Solution:**

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

### Question 10

**Task weight: 8% (not displayed in exam)**

**Use context:** k8s-K

**Task:**
A running application has been redeployed but the update is reported to have failed. Investigate the `app` namespace and restore the deployment to a running state.

**Solution:**

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

### Question 11

**Task weight: 6% (not displayed in exam)**

**Use context:** k8s-po-SW

**Task:**
Generate a list of events from all namespaces containing the word error in any case, in a reverse chronological order. Write this output to `/opt/cka-Q11/error-events`.

**Solution:**

```bash
kubectl config use-context k8s-po-SW

mkdir /opt/cka-Q11/
kubectl get events -A --sort-by='.lastTimestamp' | grep -i error | tac > /opt/cka-Q11/error-events
```

---

### Question 12

**Task weight: 6% (not displayed in exam)**

**Use context:** k8s-gfp2

**Task:**
A pod named `web` and labeled `type=web` is running using the `httpd:alpine3.19` image. A second pod named `api` uses the `tomcat:latest` image and is labeled `type=api`. Deploy network policies to ensure that the web node is only accessible on port 80. The api pod should only accept inbound traffic from the web pod on port 8080 based on the use of labels. Show that the pod network is secured using another test pod in the same namespace.

**Solution:**

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

### Question 13

**Task weight: 10% (not displayed in exam)**

**Use context:** k8s-upd-CP

**Task:**
Upgrade the current single master node from v1.27.8 to v1.28.2. Ensure the master node is drained first, then update the core cluster components. Keep in mind to not upgrade the etcd, the container runtime, CNI plugin, DNS, or any other plugin. Do not upgrade the worker node.

**Solution:**

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

### Question 14

**Task weight: 3% (not displayed in exam)**

**Use context:** None (no context change required)

**Task:**
Create a pod named `junction` using the latest `nginx:alpine` image in a new namespace named `section`. Label the pod with `env=prod` and `dept=field-services`. Use only the `env=prod` label to expose the pod as an internal Kubernetes service named `section-junction` available on port 12345 using container port 80.

**Solution:**

```bash
kubectl create ns section
kubectl run junction --image nginx:alpine -l env=prod,dept=field-services --port 80 -n section
kubectl expose pod junction -n section --name=section-junction --selector='env=prod' --port 12345 --target-port 80
```

---

### Question 15

**Task weight: 5% (not displayed in exam)**

**Use context:** k8s-ns-rl

**Task:**
A requirement has come to you to restrict resource allocation on a new namespace to be called `limits`. The entire namespace should support no more than 12 pods, and have a maximum memory allocation of 2GB. In addition, no single container should be allocated more than 300m of CPU. Attempt to create a pod using the httpd image provisioned with a resource request for 200m CPU and 3GB memory in this limits namespace. Write any resultant error to the `/opt/cka-Q15/limits-error` file.

**Solution:**

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

### Question 16

**Task weight: 4% (not displayed in exam)**

**Use context:** k8s-ns-LKS

**Task:**
Create a new deployment named `cka-deploy` using the image `nginx:alpine` with replicas 1 and map storage to the existing persistent volume claim `cka-pvc`. Expose this deployment as an internal Kubernetes service named `cka-service` on port 8080 and container port 80. Demonstrate that the service is working.

**Solution:**

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
