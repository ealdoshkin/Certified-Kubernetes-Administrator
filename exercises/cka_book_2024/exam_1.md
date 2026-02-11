## CKA Mock Exam 1

### Question 1

**Task weight:** 4%

**Use context:** k8sch1-H

**Task:**
Create a pod using image `nginx:alpine3.18-slim` in the namespace `busy`, configured with labels `exam=cka` and `question=1`. The pod and its container must be named `busy-time` and `busy-time-container`. This pod should only be permitted on the controlplane master node. Ensure that the pod is running.

---

### Question 2

**Task weight:** 3%

**Use context:** k8svl-L

**Task:**
Use the kubectl command to output a list of all node names and store in a file named `/opt/exam/101/node-names`. Store the details of nodes not using the taint `node-role.kubernetes.io/control-plane:NoSchedule` in individual json files in the same directory. Use the name of the node as the filename.

---

### Question 3

**Task weight:** 6%

**Use context:** k8ssd

**Task:**
Create a persistent volume of type hostPath named `cka-pv-q3` with a storage capacity of 5Gi, ReadWriteOnce access mode, and file-path location `/mnt/app/data`. Define a storage class and name the storage class `cka-manual-mapping`. Create a new PersistentVolumeClaim named `cka-pvc-q3` in the default namespace. Ensure this PVC becomes bound to the persistent volume.

---

### Question 4

**Task weight:** 5%

**Use context:** k8scicd

**Task:**
A new service account `cicd-sa` in the existing `cicd` namespace will require create permission for deployments. Create a ClusterRole named `cicd-clusterrole` to provision this access and restrict its use to only this service account in the cicd namespace. Ensure that the new service account has the requested access permissions.

---

### Question 5

**Task weight:** 5%

**Use context:** k8sdld

**Task:**
Create a static pod named `cka-static-pod` on the control plane node using the image `httpd:2.4.58-alpine`. Ensure this new static pod achieves the running state in the default namespace.

---

### Question 6

**Task weight:** 5%

**Use context:** k8sws-s

**Task:**
Expose the existing application `web-server` as the `web-portal` service available on port 32001 on each node in the cluster. The web server application listens on port 8080. Ensure that the service has 3 endpoints defined.

---

### Question 7

**Task weight:** 6%

**Use context:** k8snsdy

**Task:**
Deploy a pod named `source-app` in the existing namespace `live` using the latest httpd image. Ensure that only pods in a new namespace named `customer` are able to access this pod only on port 80. Confirm that the required connectivity has been established using a pod named `test` running the alpine/curl image.

---

### Question 8

**Task weight:** 10%

**Use context:** k8s-tadL

**Task:**
Take a backup of the etcd cluster and store it on the control plane node in the directory `/opt/cka-etcd-backup.db`. Name the backup `cka-etcd-backup.db`. Once complete, create a pod named `bookworm` using the `nginx:bookworm` image in the default namespace. Finally, restore the etcd backup and confirm the bookworm pod is no longer present.

---

### Question 9

**Task weight:** 5%

**Use context:** k8s-sas-O

**Task:**
Examine your cluster and answer the following questions. Write each answer into a single file named `/opt/cka-Q9-answers` following the format as shown below:

1. What is the current version of Kustomize?
2. What is the Kubernetes service cluster IP range?
3. What is the container runtime name?
4. What address is the CoreDNS service running at?
5. What is the default directory location holding CNI plugin configuration file(s)?

---

### Question 10

**Task weight:** 4%

**Use context:** k8s-rH-csc

**Task:**
Use the kubeadm command to find the TLS certificate expiry dates for the running Kubernetes API server and the applicable certifying authority. Write these dates into the `/opt/cka-Q10-API-Cert-Expiry.txt` and `/opt/cka-Q10-API-CA-Expiry.txt` files respectively using the DD/MM/YYYY format. Then write a kubeadm command to renew the API server TLS certificate in the file `/opt/cka-Q10-API-Cert-Renew.txt`.

---

### Question 11

**Task weight:** 10%

**Use context:** k8s-jsnp-TH

**Task:**
Generate a list displaying each image name with the number of restarts for each running pod in the kube-system namespace. Order the list by the restarts count in descending order, and output into the `/opt/cka-Q11-image-restarts` file in the following repeating line format under the single line header as shown:

```
Image Name Restarts
```

---

### Question 12

**Task weight:** 5%

**Use context:** k8s-ssT

**Task:**
Create a pod named `nginx` using the nginx image in the default namespace. Ensure all processes run as the user ID 34, with group ID 42. The container should sleep for 10 minutes and be explicitly configured to prevent any escalation of its privileges. Grant the network administration privilege.

---

### Question 13

**Task weight:** 8%

**Use context:** k8skcq-ns

**Task:**
A replacement kubeconfig file named `trial-kube-config` is located in the `/opt` directory. However the test team's attempted use of its single context fails. Investigate and fix this issue.

---

### Question 14

**Task weight:** 10%

**Use context:** k8s-recop

**Task:**
An update of the image associated with an existing deployment named `cka-q14-deploy` has not provisioned the expected functional improvements in the `web-service` namespace. Revert the deployment to the previous version and add the labels `action=recovered` and `program=cka` to both the deployment and running pods. Deploy a service with the same name and namespace based only on these two new tags exposing port 80.

---

### Question 15

**Task weight:** 8%

**Use context:** k8s-ssh

**Task:**
Create a new user named `khippy`, based on the private key and user certificate signing request provisioned in the `/opt/cka-Q15/` directory. Grant this new user permission to create, get, list, and watch pods in any namespace.

---

### Question 16

**Task weight:** 6%

**Use context:** k8s-e8p

**Task:**
Create a deployment named `cka-q16-deploy` using the latest httpd image with 3 replicas. Instruct an init container using the busybox image to sleep for 10 seconds. Configure a readiness probe to call the base path `/` on the default http port, with an initial delay and period, both set to 3 seconds. Also, implement a liveness probe, which can just return true.

---
