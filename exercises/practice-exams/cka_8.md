# CKA 8

---

## Question 1

Create a pod with environment variables as var1=value1.Check the environment variable in pod
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

```bash
kubectl run nginx --image=nginx --restart=Never --env=var1=value1
# then
kubectl exec -it nginx -- env
# or
kubectl exec -it nginx -- sh -c 'echo $var1'
# or
kubectl describe po nginx | grep value1
```

---

## Question 2

Create a deployment as follows:
Name: nginx-random
Exposed via a servicenginx-random
Ensure that the service & podare accessible via theirrespective D NS records
The container(s) within anypod(s) running as a part of thisdeployment should use thenginx Image
Next, use the utilitynslookupto lookup the D NS records of the service &pod and write the output to
/opt/K UN W00601/service.dnsand/opt/K UN W00601/pod.dnsrespectively.
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

Certshared now are offering 100% pass ensure C KA dumps!
https://www.certshared.com/exam/C KA/ (65 Q&As)

---

## Question 3

Create a pod as follows:
Name: mongo
Using Image: mongo
In a new Kubernetes namespace named: my-website
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

Certshared now are offering 100% pass ensure C KA dumps!
https://www.certshared.com/exam/C KA/ (65 Q&As)

---

## Question 4

Create a deployment as follows:
Name: nginx-app
Using container nginx with version 1.11.10-alpine
The deployment should contain 3 replicas
Next, deploy the application with new version 1.11.13-alpine, by performing a rolling update.
Finally, rollback that update to the previous version 1.11.10-alpine.
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

Certshared now are offering 100% pass ensure C KA dumps!
https://www.certshared.com/exam/C KA/ (65 Q&As)

---

## Question 5

Create a pod namedkucc 8with asingle app container for each of the
following images running inside(there may be between 1 and 4images specified): nginx + redis + memcached.
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

Certshared now are offering 100% pass ensure C KA dumps!
https://www.certshared.com/exam/C KA/ (65 Q&As)
Certshared now are offering 100% pass ensure C KA dumps!
https://www.certshared.com/exam/C KA/ (65 Q&As)

---

## Question 6

Create a pod with image nginx called nginx and allow traffic on port 80
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

```bash
kubectlrun nginx --image=nginx --restart=Never --port=80

```

---

## Question 7

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

## Question 8

List all persistent volumes sorted bycapacity, saving the fullkubectloutput to
/opt/K UC C00102/volume_list. Usekubectl 's own functionality forsorting the output, and do not manipulate it any further.

- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

Certshared now are offering 100% pass ensure C KA dumps!
https://www.certshared.com/exam/C KA/ (65 Q&As)

---

## Question 9

Create a pod as follows:
Name: non-persistent-redis
container Image: redis
Volume with name: cache-control
Mount path:/data/redis
The pod should launch in thestagingnamespace and the volumemust notbe persistent.
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

Certshared now are offering 100% pass ensure C KA dumps!
https://www.certshared.com/exam/C KA/ (65 Q&As)
Certshared now are offering 100% pass ensure C KA dumps!
https://www.certshared.com/exam/C KA/ (65 Q&As)

---

## Question 10

Ensure a single instance of podnginxis running on each node of the Kubernetes cluster wherenginxalso represents the Image name whichhas to be used. Do not
override anytaints currently in place.
Use Daemon Setto complete thistask and useds-kusc 00201as Daemon Set name.
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

Certshared now are offering 100% pass ensure C KA dumps!
https://www.certshared.com/exam/C KA/ (65 Q&As)
Certshared now are offering 100% pass ensure C KA dumps!
https://www.certshared.com/exam/C KA/ (65 Q&As)

---

## Question 10

Check the image version in pod without the describe command
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

```bash
kubectl get po nginx -o jsonpath='{.spec.containers[].image}{"\n"}'

```

---

## Question 14

Create 2 nginx image pods in which one of them is labelled with env=prod and another one labelled with
env=dev and verify the same.
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

```bash
kubectl run --generator=run-pod/v 1 --image=nginx -- labels=env=prod nginx-prod --dry-run -o yaml > nginx-prodpod.yaml Now, edit nginx-prod-pod.yaml file and

remove entries like ??creation Timestamp: null?? ??dns Policy: Cluster First??
vim nginx-prod-pod.yaml api Version: v 1
kind: Pod metadata: labels: env: prod
name: nginx-prod spec:
containers:
- image: nginx name: nginx-prod
restart Policy: Always
```bash
# kubectl create -f nginx-prod-pod.yaml
kubectl run --generator=run-pod/v 1 --image=nginx -- labels=env=dev nginx-dev --dry-run -o yaml > nginx-dev-pod.yaml api Version: v 1

kind: Pod metadata: labels: env: dev
name: nginx-dev
spec: containers:
- image: nginx name: nginx-dev
restart Policy: Always
```bash
# kubectl create -f nginx-prod-dev.yaml Verify :
kubectl get po --show-labels kubectl get po -l env=prod kubectl get po -l env=dev
```

---

## Question 16

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

Certshared now are offering 100% pass ensure C KA dumps!
https://www.certshared.com/exam/C KA/ (65 Q&As)
Certshared now are offering 100% pass ensure C KA dumps!
https://www.certshared.com/exam/C KA/ (65 Q&As)

---

## Question 18

Check the Image version of nginx-dev pod using jsonpath
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

kubect 1 get po nginx-dev -o jsonpath='{.spec.containers[].image}{"\n"}'

---

## Question 23

Create a busybox pod and add ??sleep 3600?? command
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

```bash
kubectl run busybox --image=busybox --restart=Never -- /bin/sh -c "sleep 3600"
```

---

## Question 24

Create and configure the servicefront-end-serviceso it's accessiblethrough Node Portand routes to theexisting pod namedfront-end.
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

Certshared now are offering 100% pass ensure C KA dumps!
https://www.certshared.com/exam/C KA/ (65 Q&As)

---

## Question 25

Get I P address of the pod ?C ??nginx-dev??
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

Kubect 1 get po -o wide Using Json Path
kubect 1 get pods -o=jsonpath='{range items[*]}{.metadata.name}{"\t"}{.status.pod IP}{"\n"}{end}'

---

## Question 29

List all the pods showing name and namespace with a json path expression
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

```bash
kubectl get pods -o=jsonpath="{.items[*]['metadata.name', 'metadata.namespace']}"

```

---

## Question 33

Create a snapshot of theetcdinstance running athttps://127.0.0.1:2379, saving thesnapshot to the file path /srv/data/etcd-snapshot.db.
```bash
The following T LScertificates/key are suppliedfor connecting to the server withetcdctl:

C A certificate:/opt/K UC M00302/ca.crt
Client certificate:/opt/K UC M00302/etcd-client.crt
Client key: Topt/K UC M00302/etcd-client.key
- A. Mastered
- B. Not Mastered
**Answer:** A
```

**Explanation:**

Certshared now are offering 100% pass ensure C KA dumps!
https://www.certshared.com/exam/C KA/ (65 Q&As)
```

---

## Question 35

Schedule a pod as follows:
Name: nginx-kusc 00101
Image: nginx
Node selector: disk=ssd
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

Certshared now are offering 100% pass ensure C KA dumps!
https://www.certshared.com/exam/C KA/ (65 Q&As)

---

## Question 39

Check to see how many worker nodes are ready (not including nodes tainted No Schedule) and write the number to/opt/K UC C00104/kucc 00104.txt.
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

Certshared now are offering 100% pass ensure C KA dumps!
https://www.certshared.com/exam/C KA/ (65 Q&As)

---

## Question 44

......
Certshared now are offering 100% pass ensure C KA dumps!
https://www.certshared.com/exam/C KA/ (65 Q&As)
Thank You for Trying Our Product
We offer two products:
1st - We have Practice Tests Software with Actual Exam Questions
2nd - Questons and Answers in P DF Format
C KA Practice Exam Features:
* C KA Questions and Answers Updated Frequently
* C KA Practice Questions Verified by Expert Senior Certified Staff
* C KA Most Realistic Questions that Guarantee you a Pass on Your First Try
* C KA Practice Test Questions in Multiple Choice Formats and Updatesfor 1 Year
100% Actual & Verified — Instant Download, Please Click
Order The C KA Practice Test Here
Powered by T CP DF (www.tcpdf.org)