# CKAD

---

## Question 1

Exhibit:
Given a container that writes a log file in format A and a container that converts log files from format
A to format B, create a deployment that runs both containers such that the log files from the first
container are converted by the second container, emitting logs in format B.
Task:
* Create a deployment named deployment-xyz in the default namespace, that:
* Includes a primary
lfccncf/busybox:1 container, named logger-dev
* includes a sidecar Ifccncf/fluentd: v 0.12 container, named adapter-zen
* Mounts a shared volume /tmp/log on both containers, which does not persist when the pod is
deleted
* Instructs the logger-dev
container to run the command
which should output logs to /tmp/log/input.log in plain text format, with example values:
* The adapter-zen sidecar container should read /tmp/log/input.log and output the data to
/tmp/log/output.* in Fluentd J SO N format. Note that no knowledge of Fluentd is required to complete
this task: all you will need to achieve this is to create the Config Map from the spec file provided at
/opt/K DM C00102/fluentd-configma p.yaml , and mount that Config Map to /fluentd/etc in the adapter-
zen sidecar container
A.
B.
Correct Answer: A

---

## Question 2

Exhibit:
Context
You are tasked to create a Config Map and consume the Config Map in a pod using a volume mount.
Task
Please complete the following:
* Create a Config Map named another-config containing the key/value pair: key 4/value3
* start a pod named nginx-configmap containing a single container using the
nginx image, and mount the key you just created into the pod under directory /also/a/path
A.
B.
Correct Answer: A

---

## Question 3

Exhibit:
Context
A user has reported an aopticauon is unteachable due to a failing liveness Probe .
Task
Perform the following tasks:
* Find the broken pod and store its name and namespace to /opt/K DO B00401/broken.txt in the
format:
The output file has already been created
* Store the associated error events to a file /opt/K DO B00401/error.txt, The output file has already
been created. You will need to use the -o wide output specifier with your command
* Fix the issue.
```bash
A. Solution: Create the Pod: kubectl create -f

http://k 8s.io/docs/tasks/configure-pod-container/exec-liveness.yaml Within 30 seconds, view the
```bash
Pod events: kubectl describe pod liveness-exec The output indicates that no liveness probes have

failed yet: First Seen Last Seen Count From Subobject Path Type Reason Message--------- -------- ----- --
-- ------------- -------- ------ -------24s 24s 1 {default-scheduler } Normal Scheduled Successfully
assigned liveness-exec to worker 023s 23s 1 {kubelet worker 0} spec.containers{liveness} Normal
Pulling pulling image 'gcr.io/google_containers/busybox'23s 23s 1 {kubelet worker 0}
spec.containers{liveness} Normal Pulled Successfully pulled image
'gcr.io/google_containers/busybox'23s 23s 1 {kubelet worker 0} spec.containers{liveness} Normal
Created Created container with docker id 86849c 15382e; Security:[seccomp=unconfined]23s 23s
1 {kubelet worker 0} spec.containers{liveness} Normal Started Started container with docker id
```bash
86849c 15382e After 35 seconds, view the Pod events again: kubectl describe pod liveness-exec At

the bottom of the output, there are messages indicating that the liveness probes have failed, and
the containers have been killed and recreated.First Seen Last Seen Count From Subobject Path Type
Reason Message ----------------------------------------------------------37s 37s 1 {default-scheduler }
Normal Scheduled Successfully assigned liveness-exec to worker 036s 36s 1 {kubelet worker 0}
spec.containers{liveness} Normal Pulling pulling image 'gcr.io/google_containers/busybox'36s 36s
1 {kubelet worker 0} spec.containers{liveness} Normal Pulled Successfully pulled image
'gcr.io/google_containers/busybox'36s 36s 1 {kubelet worker 0} spec.containers{liveness} Normal
Created Created container with docker id 86849c 15382e; Security:[seccomp=unconfined]36s 36s
1 {kubelet worker 0} spec.containers{liveness} Normal Started Started container with docker id
86849c 15382e 2s 2s 1 {kubelet worker 0} spec.containers{liveness} Warning Unhealthy Liveness
probe failed: cat: can't open '/tmp/healthy': No such file or directory Wait another 30 seconds, and
```bash
verify that the Container has been restarted: kubectl get pod liveness-exec The output shows

that RE ST AR TShas been incremented: N AM E R EA DY S TA TU S R ES TA RT S A GEliveness-exec 1/1
Running 1 m
```bash
B. Solution: Create the Pod: kubectl create -f

http://k 8s.io/docs/tasks/configure-pod-container/exec-liveness.yaml Within 30 seconds, view the
```bash
Pod events: kubectl describe pod liveness-exec The output indicates that no liveness probes have

failed yet: First Seen Last Seen Count From Subobject Path Type Reason Message--------- -------- ----- --
-- ------------- -------- ------ -------24s 24s 1 {default-scheduler } Normal Scheduled Successfully
assigned liveness-exec to worker 023s 23s 1 {kubelet worker 0} spec.containers{liveness} Normal
```bash
Pulling pulling image 'gcr.io/google_containers/busybox'kubectl describe pod liveness-exec At the

bottom of the output, there are messages indicating that the liveness probes have failed, and the
containers have been killed and recreated.First Seen Last Seen Count From Subobject Path Type
Reason Message ----------------------------------------------------------37s 37s 1 {default-scheduler }
Normal Scheduled Successfully assigned liveness-exec to worker 036s 36s 1 {kubelet worker 0}
spec.containers{liveness} Normal Pulling pulling image 'gcr.io/google_containers/busybox'36s 36s
1 {kubelet worker 0} spec.containers{liveness} Normal Pulled Successfully pulled image
'gcr.io/google_containers/busybox'36s 36s 1 {kubelet worker 0} spec.containers{liveness} Normal
Created Created container with docker id 86849c 15382e; Security:[seccomp=unconfined]36s 36s
1 {kubelet worker 0} spec.containers{liveness} Normal Started Started container with docker id
86849c 15382e 2s 2s 1 {kubelet worker 0} spec.containers{liveness} Warning Unhealthy Liveness
probe failed: cat: can't open '/tmp/healthy': No such file or directory Wait another 30 seconds, and
```bash
verify that the Container has been restarted: kubectl get pod liveness-exec The output shows

that RE ST AR TShas been incremented: N AM E R EA DY S TA TU S R ES TA RT S A GEliveness-exec 1/1
Running 1 m
Correct Answer: A