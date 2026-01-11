# CKA 0

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

List the nginx pod with custom columns POD_NAME and POD_STATUS
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

```bash
kubectl get po -o=custom-columns="POD_NAME:.metadata.name, POD_STATUS:.status.container Statuses[].state"
```

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

---

## Question 5

Set the node named ek 8s-node-1 as unavailable and reschedule all the pods running on it.
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

---

## Question 6

Create a persistent volume with nameapp-data, of capacity 2 Giandaccess mode Read Write Many. Thetype of volume ishost Pathand itslocation is /srv/app-data.
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

Persistent Volume
A persistent volume is a piece of storage in a Kubernetes cluster. Persistent Volumes are a cluster-level resource like nodes, which don??t belong to any
namespace. It is provisioned by the administrator and has a particular file size. This way, a developer deploying their app on Kubernetes need not knowthe
underlying infrastructure. When the developer needs a certain amount of persistent storage for their application, the system administrator configures the cluster so
that they consume the Persistent Volume provisioned in an easy way.
Creating Persistent Volume
kind: Persistent Volumeapi Version: v 1metadata: name: app-dataspec: capacity: # defines the capacity of P V we are creatingstorage:2 Gi#the amount of storage we
are tying to claimaccess Modes: # defines the rights of the volumewe are creating-Read Write Manyhost Path: path: "/srv/app-data" # path to which we are creating
the volume
Challenge
Create a Persistent Volume namedapp-data, with access mode Read Write Many, storage classname
shared,2 Giof storage capacity and the host path/srv/app-data.
* 2. Save the file and create the persistent volume. Image for post
* 3. View the persistent volume.
Our persistent volume status is available meaning it is available and it has not been mounted yet. This status willchange when we mount the persistent Volume to
a persistent Volume Claim.
Persistent Volume Claim
In a real ecosystem, a system admin will create the Persistent Volume then a developer will create a Persistent Volume Claim which will be referenced in a pod. A
Persistent Volume Claim is created by specifying the minimum size and the access mode they require from the persistent Volume.
Challenge
Create a Persistent Volume Claim that requests the Persistent Volume we had created above. The claim should request 2 Gi. Ensurethat the Persistent Volume
Claim has the same storage Class Name as the persistent Volume you had previously created.
kind: Persistent Volumeapi Version: v 1metadata: name: app-data spec:
access Modes:-Read Write Manyresources:
requests: storage:2 Gi storage Class Name: shared
* 2. Save and create the pvc
njerry 191@cloudshell:~(extreme-clone-2654111)$ kubect 1 create -f app-data.yaml persistentvolumeclaim/app-data created
* 3. View the pvc Image for post
* 4. Let??s see what has changed in the pv we had initially created.
Image for post
Our status has now changed fromavailabletobound.
* 5. Create a new pod named myapp with image nginx that will be used to Mount the Persistent Volume Claim with the path /var/app/config.
Mounting a Claim
api Version: v 1kind: Podmetadata: creation Timestamp: nullname: app-dataspec: volumes:- name: congigpvcpersisten Volume Claim: claim Name: app-datacontainers:-
image: nginxname: appvolume Mounts:- mount Path: "/srv/app-data"name: configpvc

---

## Question 7

List pod logs named ??frontend?? and search for the pattern ??started?? and write it to a file ??/opt/error-logs??
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

```bash
Kubectl logs frontend | grep -i ??started?? > /opt/error-logs
```

---

## Question 8

List all persistent volumes sorted bycapacity, saving the fullkubectloutput to
/opt/K UC C00102/volume_list. Usekubectl 's own functionality forsorting the output, and do not manipulate it any further.

- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

---

## Question 9

Get list of all the pods showing name and namespace with a jsonpath expression.
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

```bash
kubectl get pods -o=jsonpath="{.items[*]['metadata.name'

, 'metadata.namespace']}"
```

---

## Question 10

Create a file:
/opt/K UC C00302/kucc 00302.txtthatlists all pods that implement servicebazin namespacedevelopment.
The format of the file should be onepod name per line.
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

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

## Question 13

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

---

## Question 16

List all the pods showing name and namespace with a json path expression
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

```bash
kubectl get pods -o=jsonpath="{.items[*]['metadata.name', 'metadata.namespace']}"
```

---

## Question 17

Schedule a pod as follows:
Name: nginx-kusc 00101
Image: nginx
Node selector: disk=ssd
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

---

## Question 22

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