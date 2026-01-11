# CKA 4

---

## Question 1

Monitor the logs of pod foo and:
Extract log lines correspondingto error unable-to-access-website
Write them to/opt/K UL M00201/foo
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

100% Valid and Newest Version C KA Questions & Answers shared by Certleader
https://www.certleader.com/C KA-dumps.html (67 Q&As)

---

## Question 2

Create a pod with image nginx called nginx and allow traffic on port 80
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

```bash
kubectlrun nginx --image=nginx --restart=Never --port=80

```

---

## Question 3

Create a nginx pod with label env=test in engineering namespace
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

```bash
kubectl run nginx --image=nginx --restart=Never --labels=env=test --namespace=engineering --dry-run -o yaml > nginx-pod.yaml
kubectl run nginx --image=nginx --restart=Never --labels=env=test --namespace=engineering --dry-run -o yaml | kubectl create -nengineering-f ?C

Y AM L File: api Version: v 1 kind: Pod metadata: name: nginx
namespace: engineering labels:
env: test spec: containers:
- name: nginx image: nginx
image Pull Policy: If Not Present restart Policy: Never
```bash
kubectl create -f nginx-pod.yaml

```

---

## Question 4

Create a namespace called 'development' and a pod with image nginx called nginx on this namespace.
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

```bash
kubectl create namespace development
kubectl run nginx --image=nginx --restart=Never -n development
```

---

## Question 5

A Kubernetes worker node, namedwk 8s-node-0 is in state Not Ready.Investigate why this is the case, andperform any appropriate steps tobring the node to
a Readystate,ensuring that any changes are madepermanent.
You cansshto the failednode using:
[student@node-1] $ | ssh Wk 8s-node-0
You can assume elevatedprivileges on the node with thefollowing command:
[student@w 8ks-node-0] $ |sudo ?Ci
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

100% Valid and Newest Version C KA Questions & Answers shared by Certleader
https://www.certleader.com/C KA-dumps.html (67 Q&As)

---

## Question 6

Get list of all pods in all namespaces and write it to file ??/opt/pods-list.yaml??
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

```bash
kubectl get po ?Call-namespaces > /opt/pods-list.yaml

```

---

## Question 7

Check the image version in pod without the describe command
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

```bash
kubectl get po nginx -o jsonpath='{.spec.containers[].image}{"\n"}'
```

---

## Question 8

Perform the following tasks:
Add an init container tohungry-bear(which has beendefined in spec file
/opt/K UC C00108/pod-spec-K UC C00108.yaml)
The init container should createan empty file named/workdir/calm.txt
If/workdir/calm.txtis notdetected, the pod should exit
Once the spec file has beenupdatedwith the init containerdefinition, the pod should becreated
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

100% Valid and Newest Version C KA Questions & Answers shared by Certleader
https://www.certleader.com/C KA-dumps.html (67 Q&As)

---

## Question 9

Create a busybox pod and add ??sleep 3600?? command
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

```bash
kubectl run busybox --image=busybox --restart=Never -- /bin/sh -c "sleep 3600"
```

---

## Question 10

Create and configure the servicefront-end-serviceso it's accessiblethrough Node Portand routes to theexisting pod namedfront-end.
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

---

## Question 10

Get I P address of the pod ?C ??nginx-dev??
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

Kubect 1 get po -o wide Using Json Path
kubect 1 get pods -o=jsonpath='{range items[*]}{.metadata.name}{"\t"}{.status.pod IP}{"\n"}{end}'

---

## Question 15

List all the pods showing name and namespace with a json path expression
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

```bash
kubectl get pods -o=jsonpath="{.items[*]['metadata.name', 'metadata.namespace']}"
```

---

## Question 16

Scale the deploymentwebserverto 6pods.
- A. Mastered
- B. Not Mastered
100% Valid and Newest Version C KA Questions & Answers shared by Certleader
https://www.certleader.com/C KA-dumps.html (67 Q&As)
**Answer:** A

**Explanation:**

---

## Question 20

Create a pod that having 3 containers in it? (Multi-Container)
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

image=nginx, image=redis, image=consul Name nginx container as ??nginx-container?? Name redis container as ??redis-container?? Name consul container as
??consul-container??
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
name: consul-container
restart Policy: Always

```

---

## Question 24

......
100% Valid and Newest Version C KA Questions & Answers shared by Certleader
https://www.certleader.com/C KA-dumps.html (67 Q&As)
Thank You for Trying Our Product
* 100% Pass or Money Back
All our products come with a 90-day Money Back Guarantee.
* One year free update
You can enjoy free update one year. 24x 7 online support.
* Trusted by Millions
We currently serve more than 30,000,000 customers.
* Shop Securely
All transactions are protected by Veri Sign!
100% Pass Your C KA Exam with Our Prep Materials Via below:
https://www.certleader.com/C KA-dumps.html
Powered by T CP DF (www.tcpdf.org)