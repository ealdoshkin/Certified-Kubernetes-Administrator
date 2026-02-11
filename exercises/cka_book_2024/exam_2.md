## CKA Mock Exam 2

### Question 1

**Task weight:** 2%

**Use context:** k8sch1-H

**Task:**
Access the logs for the pod associated with the deployment named `cka-q1-deploy` running in the `cka-exam` namespace. Output the log for the init container to `/opt/cka-Q2/init`. Output the log for the main container to `/opt/cka-Q2/main`. Write a kubectl command to follow all pod logging to `/opt/cka-Q2/all`.

---

### Question 2

**Task weight:** 6%

**Use context:** k8s-kskd

**Task:**
Create a storage class named `cka-q2-sc` with the `kubernetes.io/aws-ebs` provisioner setting the type parameter to `gp3`. Ensure the volume binding mode is set to `WaitForFirstConsumer`. Next, list all the available storage classes sorted by age with the newest first, writing this output to `/opt/cka-Q2/k8s-kskd`.

---

### Question 3

**Task weight:** 5%

**Use context:** k8s

**Task:**
Create a new service account named `cka-sa` in the default namespace and provide permissions to get and list pods only in its own namespace.

---

### Question 4

**Task weight:** 12%

**Use context:** k8s-dnsl

**Task:**
Create a deployment named `cka-q4-deploy` in the existing `cka-exam` namespace using the `httpd:alpine` image with 1 replica and use the label `app=cka`. Once running, scale the deployment to 2 replicas using kubectl. Next, expose `cka-q4-deploy` as an internal service named `cka-q4-service` on port 80. Finally, perform a DNS lookup from within the cluster of both the service and a pod, writing output to new `service-dns-lookup` and `pod-dns-lookup` files on the `/opt/cka-Q4` directory.

---

### Question 5

**Task weight:** 4%

**Use context:** k8s-RS

**Task:**
Create a pod named `multi-app` in a new `test` namespace that runs a busybox image to write the current date to a persistent volume of type `emptyDir` on path `/app/data`. Ensure that the primary container with image `nginx:alpine` outputs this date to the pod log.

---

### Question 6

**Task weight:** 5%

**Use context:** k8s-cswp

**Task:**
Create two pods using the httpd image named `control-plane-pod` and `data-plane-pod`. Ensure the first pod runs on the master node in the cluster and the second on the single worker node. Resource limits should be applied to the worker node pod in the form of 150 millicore CPU, 250-mebibyte memory, and 1-gigabyte ephemeral storage.

---

### Question 7

**Task weight:** 6%

**Use context:** k8s-tr-K

**Task:**
To prepare for scheduled maintenance, configure the `clusterq7-node1` to ensure no new pods can be scheduled to run on it. Next, gracefully reschedule all non-daemonset pods running on this node. When this process has successfully completed write the status of the node as described in the node event logging to `/opt/cka-Q7/node-status`. Finally return to the node to its original operational status.

---

### Question 8

**Task weight:** 6%

**Use context:** k8s-secSS

**Task:**
Create a ConfigMap named `cm-7` containing entries `app=cka-7` and `exam=cka` in the existing namespace `space`. Create a pod named `voyager` using image `httpd:alpine3.18` in the same namespace and reference the config map data as environment variables, converting each key name into uppercase to derive the corresponding environment variable name. Create a second ConfigMap named `cm-8` with entries `tier1=0-5`, `tier2=6-8`, and `tier3=9-10`. Mount this second config map as volume data, with each separate individual file having the name of a specific key and holding the corresponding value. Access the pod and output all environment variables to `/opt/cka-Q8/env-vars` on the same node. Also, list the file contents of the mounted directory to `/opt/cka-Q8/volume-files`.

---

### Question 9

**Task weight:** 12%

**Use context:** k8s-po-NE

**Task:**
The Kubernetes server environment has one node that is at an earlier release of Kubernetes and is not part of the cluster. Upgrade this node `clusterq9-node2` to the same version of Kubernetes as the rest of the cluster. Finally, add this node to the existing cluster. Kubeadm is already installed as per the required version.

---

### Question 10

**Task weight:** 8%

**Use context:** k8s-K

**Task:**
A running application has been redeployed but the update is reported to have failed. Investigate the `app` namespace and restore the deployment to a running state.

---

### Question 11

**Task weight:** 6%

**Use context:** k8s-po-SW

**Task:**
Generate a list of events from all namespaces containing the word error in any case, in a reverse chronological order. Write this output to `/opt/cka-Q11/error-events`.

---

### Question 12

**Task weight:** 6%

**Use context:** k8s-gfp2

**Task:**
A pod named `web` and labeled `type=web` is running using the `httpd:alpine3.19` image. A second pod named `api` uses the `tomcat:latest` image and is labeled `type=api`. Deploy network policies to ensure that the web node is only accessible on port 80. The api pod should only accept inbound traffic from the web pod on port 8080 based on the use of labels. Show that the pod network is secured using another test pod in the same namespace.

---

### Question 13

**Task weight:** 10%

**Use context:** k8s-upd-CP

**Task:**
Upgrade the current single master node from v1.27.8 to v1.28.2. Ensure the master node is drained first, then update the core cluster components. Keep in mind to not upgrade the etcd, the container runtime, CNI plugin, DNS, or any other plugin. Do not upgrade the worker node.

---

### Question 14

**Task weight:** 3%

**Use context:** None (no context change required)

**Task:**
Create a pod named `junction` using the latest `nginx:alpine` image in a new namespace named `section`. Label the pod with `env=prod` and `dept=field-services`. Use only the `env=prod` label to expose the pod as an internal Kubernetes service named `section-junction` available on port 12345 using container port 80.

---

### Question 15

**Task weight:** 5%

**Use context:** k8s-ns-rl

**Task:**
A requirement has come to you to restrict resource allocation on a new namespace to be called `limits`. The entire namespace should support no more than 12 pods, and have a maximum memory allocation of 2GB. In addition, no single container should be allocated more than 300m of CPU. Attempt to create a pod using the httpd image provisioned with a resource request for 200m CPU and 3GB memory in this limits namespace. Write any resultant error to the `/opt/cka-Q15/limits-error` file.

---

### Question 16

**Task weight:** 4%

**Use context:** k8s-ns-LKS

**Task:**
Create a new deployment named `cka-deploy` using the image `nginx:alpine` with replicas 1 and map storage to the existing persistent volume claim `cka-pvc`. Expose this deployment as an internal Kubernetes service named `cka-service` on port 8080 and container port 80. Demonstrate that the service is working.

---
