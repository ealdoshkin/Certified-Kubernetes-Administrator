# Debug

Ephemeral Debug Containers:

```bash
# For troubleshooting without modifying pod spec
kubectl debug <pod-name> -it --image=busybox --target=<container-name>
```


```sh
k top nodes, pods
```

Pods error:
CrashLoopBackOffThe pod is trying to start, crashing, and then restarting in a loop.
Kubernetes will wait for an increasing back-off time between
restarts to give you a chance to fix the error.
ImagePullBackOffA pod cannot start up because it can’t find the specified image
locally or in the remote container registry. It will continue to try
with an increasing back-off delay.
ErrImagePullA pod fails to start up because the image cannot be found or
pulled due to authorization.
CreateContainerConfig-ErrorA container within the pod will not start due to missing compo-
nents that are required to run.
RunContainerErrorRunning the container within a pod fails due to problems with
the container runtime or entry point of the container.
FailedSchedulingA pod is unable to be scheduled to a node because nodes are
marked as unschedulable, a taint is applied, or the node can’t
satisfy the requirements.
NonZeroExitCodeThe container within a pod exits unexpectedly due to an applica-
tion error or missing file or directory.
OOMKilledA pod was scheduled, but the memory limit assigned to it has
been exceeded.



Type troubleshooting:

Pods (object) - log, error
Services
Network (Network policy)
Node - kubelet
Control-plane
Certificate
Resources


## Pod
•Always start with kubectl get pods.
•Use kubectl describe for detailed information.
•Check logs with kubectl logs.
•Review events with kubectl get events.

Pod state:

Pending: The pod is accepted by the cluster but is
waiting for scheduling and not yet running.
Running: The pod is assigned to a node, and at least
one container is running or starting.
Succeeded: All containers have completed
successfully.
Failed: One or more containers have failed, and the
pod will not restart.
Unknown: The pod state cannot be determined due
to a node communication failure.


Container States in a Pod
Inside a pod, each container has its own lifecycle, categorized into
three states:
Waiting: The container is preparing to start, pulling
images, or processing secrets.
Running: The container is actively executing
without errors.
Terminated: The container has either successfully
exited or failed, with logs indicating the reason.


k get svc
kubectl get endpoints myservice


## Сluster

Step to checking:

crictl log
systemctl status kubelet

kubectl context

kubectl cluster-info
kubectl cluster-info dump | grep error
k get cs



API > Kubelet > API_CONFIG > ETCD > CRICTL logs
Kubeconfig > IP:PORT > Cert > Kubelet


kubectl logs kube-apiserver-minikube



HTTP > Service > Endpoint > MathLabel > Pod > Log > Other container | Svc
