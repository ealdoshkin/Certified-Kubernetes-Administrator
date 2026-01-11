# CKA 1

---

## Question 1

A Kubernetes worker node, named wk 8s-node-0 is in state Not Ready. Investigate why this is the case, and perform any appropriate steps to bring the node to a
Ready state, ensuring that any changes are made permanent.
You can ssh to the failed node using:
[student@node-1] $ | ssh Wk 8s-node-0
You can assume elevated privileges on the node with the following command:
[student@w 8ks-node-0] $ | sudo –i
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

---

## Question 2

List all the pods showing name and namespace with a json path expression
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

```bash
kubectl get pods -o=jsonpath="{.items[*]['metadata.name', 'metadata.namespace']}"

```

---

## Question 3

Create a pod that having 3 containers in it? (Multi-Container)
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

image=nginx, image=redis, image=consul Name nginx container as “nginx-container” Name redis container as “redis-container” Name consul container as
“consul-container”
Create a pod manifest file for a container and append container section for rest of the images
```bash
kubectl run multi-container --generator=run-pod/v 1 --image=nginx -- dry-run -o yaml > multi-container.yaml
# then

vim multi-container.yaml api Version: v 1
kind: Pod metadata: labels:
run: multi-container name: multi-container spec:
containers:
- image: nginx
name: nginx-container
- image: redis
name: redis-container
- image: consul
name: consul-container restart Policy: Always

```

---

## Question 4

List all the pods sorted by name
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

```bash
kubectl get pods --sort-by=.metadata.name
```

---

## Question 5

Create a deployment spec file that will:
Launch 7 replicas of the nginx Image with the labelapp_runtime_stage=dev
deployment name: kual 00201
Save a copy of this spec file to /opt/K UA L00201/spec_deployment.yaml
(or /opt/K UA L00201/spec_deployment.json).
When you are done, clean up (delete) any new Kubernetes A PI object that you produced during this task.
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

---

## Question 6

Get I P address of the pod – “nginx-dev”
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

Kubect 1 get po -o wide Using Json Path
kubect 1 get pods -o=jsonpath='{range items[*]}{.metadata.name}{"\t"}{.status.pod IP}{"\n"}{end}'

---

## Question 7

Create a file:
/opt/K UC C00302/kucc 00302.txt that lists all pods that implement service baz in namespace development.
The format of the file should be one pod name per line.
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

---

## Question 8

Check the image version in pod without the describe command
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

```bash
kubectl get po nginx -o jsonpath='{.spec.containers[].image}{"\n"}'
```

---

## Question 9

Create a pod as follows:
Name: non-persistent-redis
container Image: redis
Volume with name: cache-control
Mount path: /data/redis
The pod should launch in the staging namespace and the volume must not be persistent.
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

---

## Question 10

Score: 13%
Task
A Kubernetes worker node, named wk 8s-node-0 is in state Not Ready. Investigate why this is the case, and perform any appropriate steps to bring the node to a
Ready state, ensuring that any changes are made permanent.
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

sudo -i
systemctl status kubelet systemctl start kubelet systemctl enable kubelet

---

## Question 10

For this item, you will have to ssh to the nodes ik 8s-master-0 and ik 8s-node-0 and complete all tasks on these nodes. Ensure that you return to the base node
(hostname: node-1) when you have completed this item.
Context
As an administrator of a small development team, you have been asked to set up a Kubernetes cluster to test the viability of a new application.
Task
```bash
You must use kubeadm to perform this task. Any kubeadm invocations will require the use of the

--ignore-preflight-errors=all option.
Configure the node ik 8s-master-O as a master node. .
Join the node ik 8s-node-o to the cluster.
- A. Mastered
- B. Not Mastered
**Answer:** A
```

**Explanation:**

```bash
You must use the kubeadm configuration file located at /etc/kubeadm.conf when initializingyour cluster.

You may use any C NI plugin to complete this task, but if you don't have your favourite C NI plugin's manifest U RL at hand, Calico is one popular option:
https://docs.projectcalico.org/v 3.14/manifests/calico.yaml
Docker is already installed on both nodes and apt has been configured so that you can install the required tools.
```

---

## Question 13

List all the pods sorted by name
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

kubect 1 get pods --sort-by=.metadata.name

---

## Question 15

Check the Image version of nginx-dev pod using jsonpath
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

kubect 1 get po nginx-dev -o jsonpath='{.spec.containers[].image}{"\n"}'

---

## Question 19

Create a deployment as follows:
Name: nginx-random
Exposed via a service nginx-random
Ensure that the service & pod are accessible via their respective D NS records
The container(s) within any pod(s) running as a part of this deployment should use the nginx Image
Next, use the utility nslookup to look up the D NS records of the service & pod and write the output to
/opt/K UN W00601/service.dns and /opt/K UN W00601/pod.dns respectively.
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

---

## Question 23

Create a busybox pod and add “sleep 3600” command
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

```bash
kubectl run busybox --image=busybox --restart=Never -- /bin/sh -c "sleep 3600"
```

---

## Question 27

Create a Kubernetes secret as follows:
Name: super-secret
password: bob
Create a pod named pod-secrets-via-file, using the redis Image, which mounts a secret named super-secret at /secrets.
Create a second pod named pod-secrets-via-env, using the redis Image, which exports password as
C ON FI DE NT IA L
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

---

## Question 30

Create a pod with image nginx called nginx and allow traffic on port 80
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

```bash
kubectl run nginx --image=nginx --restart=Never --port=80

```

---

## Question 35

Score:7%
Task
Create a new Persistent Volume Claim
• Name: pv-volume
• Class: csi-hostpath-sc
• Capacity: 10 Mi
Create a new Pod which mounts the Persistent Volume Claim as a volume:
• Name: web-server
• Image: nginx
• Mount path: /usr/share/nginx/html
Configure the new Pod to have Read Write Once access on the volume.
```bash
Finally, using kubectl edit or kubectl patch expand the Persistent Volume Claim to a capacity of 70 Mi and record that change.

- A. Mastered
- B. Not Mastered
**Answer:** A
```

**Explanation:**

vi pvc.yaml storageclass pvc api Version: v 1
kind: Persistent Volume Claim metadata:
name: pv-volume spec: access Modes:
- Read Write Once volume Mode: Filesystem resources:
requests: storage: 10 Mi
storage Class Name: csi-hostpath-sc
```bash
# vi pod-pvc.yaml api Version: v 1 kind: Pod metadata:

name: web-server spec:
containers:
- name: web-server image: nginx volume Mounts:
- mount Path: "/usr/share/nginx/html"
name: my-volume volumes:
- name: my-volume persistent Volume Claim: claim Name: pv-volume
```bash
# craete
kubectl create -f pod-pvc.yaml
#edit
kubectl edit pvc pv-volume --record

```

---

## Question 40

Score: 4%
Context
You have been asked to create a new Cluster Role for a deployment pipeline and bind it to a specific Service Account scoped to a specific namespace.
Task
Create a new Cluster Role named deployment-clusterrole, which only allows to create the following resource types:
• Deployment
• Stateful Set
• Daemon Set
Create a new Service Account named cicd-token in the existing namespace app-team 1.
Bind the new Cluster Role deployment-clusterrole lo the new Service Account cicd-token , limited to the namespace app-team 1.
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

Task should be complete on node k 8s -1 master, 2 worker for this connect use command
[student@node-1] > ssh k 8s
```bash
kubectl create clusterrole deployment-clusterrole --verb=create

--resource=deployments,statefulsets,daemonsets
```bash
kubectl create serviceaccount cicd-token --namespace=app-team 1
kubectl create rolebinding deployment-clusterrole --clusterrole=deployment-clusterrole

--serviceaccount=default: cicd-token --namespace=app-team 1

```

---

## Question 43

......
T HA NK S F OR T RY IN G T HE D EM O O F O UR P RO DU CT
Visit Our Site to Purchase the Full Set of Actual C KA Exam Questions With Answers.
We Also Provide Practice Exam Software That Simulates Real Exam Environment And Has Many Self-Assessment Features. Order the C KA
Product From:
Money Back Guarantee
C KA Practice Exam Features:
* C KA Questions and Answers Updated Frequently
* C KA Practice Questions Verified by Expert Senior Certified Staff
* C KA Most Realistic Questions that Guarantee you a Pass on Your First Try
* C KA Practice Test Questions in Multiple Choice Formats and Updatesfor 1 Year
Powered by T CP DF (www.tcpdf.org)