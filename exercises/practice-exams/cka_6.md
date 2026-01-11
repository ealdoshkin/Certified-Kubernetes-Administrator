# CKA 6

---

## Question 1

Create a pod that echo ??hello world?? and then exists. Have the pod deleted automatically when it??s completed
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

```bash
kubectl run busybox --image=busybox -it --rm --restart=Never -

/bin/sh -c 'echo hello world'
```bash
kubectl get po # You shouldn't see pod with the name "busybox"
```

---

## Question 2

Monitor the logs of pod foo and:
Extract log lines correspondingto error unable-to-access-website
Write them to/opt/K UL M00201/foo
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

We recommend you to try the P RE MI UM C KA Dumps From Exambible
https://www.exambible.com/C KA-exam/ (60 Q&As)

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
We recommend you to try the P RE MI UM C KA Dumps From Exambible
https://www.exambible.com/C KA-exam/ (60 Q&As)
The deployment should contain 3 replicas
Next, deploy the application with new version 1.11.13-alpine, by performing a rolling update.
Finally, rollback that update to the previous version 1.11.10-alpine.
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

We recommend you to try the P RE MI UM C KA Dumps From Exambible
https://www.exambible.com/C KA-exam/ (60 Q&As)

---

## Question 5

List ??nginx-dev?? and ??nginx-prod?? pod and delete those pods
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

kubect 1 get pods -o wide
```bash
kubectl delete po ??nginx-dev??kubectl delete po ??nginx-prod??
```

---

## Question 6

Set the node named ek 8s-node-1 as unavailable and reschedule all the pods running on it.
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

We recommend you to try the P RE MI UM C KA Dumps From Exambible
https://www.exambible.com/C KA-exam/ (60 Q&As)

---

## Question 7

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
We recommend you to try the P RE MI UM C KA Dumps From Exambible
https://www.exambible.com/C KA-exam/ (60 Q&As)
* 2. Save the file and create the persistent volume. Image for post
* 3. View the persistent volume.
Our persistent volume status is available meaning it is available and it has not been mounted yet. This status willchange when we mount the persistent Volume
to a persistent Volume Claim.
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

## Question 8

```bash
List all persistent volumes sorted bycapacity, saving the fullkubectloutput to
/opt/K UC C00102/volume_list. Usekubectl 's own functionality forsorting the output, and do not manipulate it any further.

- A. Mastered
- B. Not Mastered
We recommend you to try the P RE MI UM C KA Dumps From Exambible
https://www.exambible.com/C KA-exam/ (60 Q&As)
**Answer:** A
```

**Explanation:**
```

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

We recommend you to try the P RE MI UM C KA Dumps From Exambible
https://www.exambible.com/C KA-exam/ (60 Q&As)
We recommend you to try the P RE MI UM C KA Dumps From Exambible
https://www.exambible.com/C KA-exam/ (60 Q&As)

---

## Question 10

Create a Kubernetes secret asfollows:
Name: super-secret
password: bob
Create a pod namedpod-secrets-via-file, using theredis Image, which mounts a secret namedsuper-secretat
/secrets.
Create a second pod namedpod-secrets-via-env, using theredis Image, which exportspasswordas
C ON FI DE NT IA L
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

We recommend you to try the P RE MI UM C KA Dumps From Exambible
https://www.exambible.com/C KA-exam/ (60 Q&As)

---

## Question 10

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
We recommend you to try the P RE MI UM C KA Dumps From Exambible
https://www.exambible.com/C KA-exam/ (60 Q&As)
name: nginx-dev
spec: containers:
- image: nginx name: nginx-dev
restart Policy: Always
```bash
# kubectl create -f nginx-prod-dev.yaml Verify :
kubectl get po --show-labels kubectl get po -l env=prod kubectl get po -l env=dev
```

---

## Question 11

Configure the kubelet systemd-managed service, on the nodelabelled withname=wk 8s-node-1, tolaunch a pod containing a singlecontainer of
Imagehttpdnamedwebtoolautomatically. Any spec filesrequired should be placed in the/etc/kubernetes/manifestsdirectoryon the node.
You canssh to theappropriate node using:
[student@node-1] $ sshwk 8s-node-1
You can assume elevatedprivileges on the node with thefollowing command:
[student@wk 8s-node-1] $ |sudo ?Ci
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

We recommend you to try the P RE MI UM C KA Dumps From Exambible
https://www.exambible.com/C KA-exam/ (60 Q&As)
We recommend you to try the P RE MI UM C KA Dumps From Exambible
https://www.exambible.com/C KA-exam/ (60 Q&As)

---

## Question 13

From the pod labelname=cpu-utilizer, find podsrunning high C PU workloads and
write the name of the pod consumingmost C PU to thefile/opt/K UT R00102/K UT R00102.txt(which already exists).
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

We recommend you to try the P RE MI UM C KA Dumps From Exambible
https://www.exambible.com/C KA-exam/ (60 Q&As)

---

## Question 15

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

We recommend you to try the P RE MI UM C KA Dumps From Exambible
https://www.exambible.com/C KA-exam/ (60 Q&As)
We recommend you to try the P RE MI UM C KA Dumps From Exambible
https://www.exambible.com/C KA-exam/ (60 Q&As)

---

## Question 19

Check the Image version of nginx-dev pod using jsonpath
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

kubect 1 get po nginx-dev -o jsonpath='{.spec.containers[].image}{"\n"}'

---

## Question 22

Create a busybox pod and add ??sleep 3600?? command
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

```bash
kubectl run busybox --image=busybox --restart=Never -- /bin/sh -c "sleep 3600"
```

---

## Question 26

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

## Question 34

Create a snapshot of theetcdinstance running athttps://127.0.0.1:2379, saving thesnapshot to the file path /srv/data/etcd-snapshot.db.
We recommend you to try the P RE MI UM C KA Dumps From Exambible
https://www.exambible.com/C KA-exam/ (60 Q&As)
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
```

---

## Question 37

Schedule a pod as follows:
Name: nginx-kusc 00101
Image: nginx
Node selector: disk=ssd
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

We recommend you to try the P RE MI UM C KA Dumps From Exambible
https://www.exambible.com/C KA-exam/ (60 Q&As)
We recommend you to try the P RE MI UM C KA Dumps From Exambible
https://www.exambible.com/C KA-exam/ (60 Q&As)

---

## Question 40

Check to see how many worker nodes are ready (not including nodes tainted No Schedule) and write the number to/opt/K UC C00104/kucc 00104.txt.
- A. Mastered
- B. Not Mastered
**Answer:** A

**Explanation:**

We recommend you to try the P RE MI UM C KA Dumps From Exambible
https://www.exambible.com/C KA-exam/ (60 Q&As)

---

## Question 45

......
We recommend you to try the P RE MI UM C KA Dumps From Exambible
https://www.exambible.com/C KA-exam/ (60 Q&As)
Relate Links
100% Pass Your C KA Exam with Exambible Prep Materials
https://www.exambible.com/C KA-exam/
Contact us
We are proud of our high-quality customer service, which serves you around the clock 24/7.
Viste - https://www.exambible.com/
Powered by T CP DF (www.tcpdf.org)