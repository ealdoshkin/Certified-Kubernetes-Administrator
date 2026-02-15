# Short command

Fast run:
`k run alpine --image=alpine -n namespace-netpol -- sleep 1d`

Fast expose with custom name:
`k expose deployment cka-deploy --selector='env=prod' --name=cka-service --port=8080 --target-port=80`


Use this:
`kubectl taint --help`


### Pod

```bash
kubectl run example-pod \
  --image=nginx \
  --restart=Never \
  --dry-run=client -o yaml
```

### Deployment

```bash
kubectl create deployment example-deployment \
  --image=nginx \
  --dry-run=client -o yaml
```

### DaemonSet

```bash
kubectl create daemonset example-daemonset \
  --image=nginx \
  --dry-run=client -o yaml
```

### Job

```bash
kubectl create job example-job \
  --image=busybox \
  --dry-run=client -o yaml -- \
  echo "Hello Kubernetes"
```

### CronJob

```bash
kubectl create cronjob example-cronjob \
  --image=busybox \
  --schedule="*/5 * * * *" \
  --dry-run=client -o yaml -- date
```

### Service (ClusterIP)

```bash
kubectl expose deployment example-deployment \
  --port=80 \
  --target-port=80 \
  --type=ClusterIP \
  --dry-run=client -o yaml
```

---

## 2. Create immediately (no YAML)

### Pod

```bash
kubectl run example-pod --image=nginx --restart=Never
```

### Deployment

```bash
kubectl create deployment example-deployment --image=nginx
```

### DaemonSet

```bash
kubectl create daemonset example-daemonset --image=nginx
```

---

## 3. Objects kubectl **cannot** generate directly

These must be written or modified manually:

- StatefulSet
- ConfigMap (complex)
- Secret (complex)
- HPA
- NetworkPolicy
- Ingress (basic support depends on version)

Quick examples:

### ConfigMap

```bash
kubectl create configmap example-config \
  --from-literal=APP_ENV=prod \
  --dry-run=client -o yaml
```

### Secret

```bash
kubectl create secret generic example-secret \
  --from-literal=username=admin \
  --from-literal=password=secret \
  --dry-run=client -o yaml
```

### Other

```
k delete all --all -n default
k logs -n default --selector app=myapp --prefix
k run -ti alpine --image=alpine --restart=Never -rm -- /bin/sh
-owide
--show-labels
k debug pod/busybox -it --copy-to=debug --share-processes --image=nicolaka/netshoot
k drain minikube-m02 --ignore-daemonsets --delete-emptydir-data
kubectl label nodes <your-node-name> disktype=ssd

nodeName: staging-node1 - назначить на ноду
kubectl get pods --sort-by=.metadata.name
kubectl get componentstatuses
kubectl replace -f question6.yaml --force # заменить и перезапустить под
```

### Doc

- Command argument



kubectl set image deployment/nginx-deployment nginx=nginx:1.21.1
kubectl scale deployments/<deployment-name>  --replicas=4
kubectl label pods redis-pod tier=database
kubectl label pods redis-pod tier-

 kubectl port-forward svc/nginx-demo 8000:80
kubectl create svc clusterip redis --tcp=8080:9090 --dry-run=client -o yaml > service.yaml
kubectl get pods -l environment=production,tier=frontend
kubectl top pods --sort-by=cpu

kubectl create quota myrq --hard=cpu=1,memory=1G,pods=2 --dry-run=client -o yaml
kubectl annotate po nginx1 nginx2 nginx3 description='my description'
kubectl explain po.spec

kubectl run busybox --image=busybox --restart=Never -o yaml --dry-run=client -- /bin/sh -c 'sleep 3600' > pod.yaml


kubectl create cronjob time-limited-job --image=busybox --restart=Never --dry-run=client --schedule="* * * * *" -o yaml -- /bin/sh -c 'date; echo Hello from the Kubernetes cluster' > time-limited-job.yaml
kk


helm list --pending -A



Extract last deploy state:
kubectl get deployment my-app -o jsonpath='{.metadata.annotations.kubectl\.kubernetes\.io/last-applied-configuration}' | jq


## Add private registry

This command is used to create a Kubernetes secret of type `docker-registry`. This secret allows Kubernetes to authenticate with a private Docker registry when pulling images for your pods. Here’s a breakdown of the process and how to use it:

---

### **What the Command Does**
```bash
kubectl create secret docker-registry regcred \
  --docker-server=<your-registry-server> \
  --docker-username=<your-username> \
  --docker-password=<your-password> \
  --docker-email=<your-email>
```

- **`regcred`**: The name of the secret you are creating.
- **`--docker-server`**: The address of your private Docker registry (e.g., `docker.io`, `ghcr.io`, or a custom registry like `myregistry.example.com`).
- **`--docker-username`**: Your username for the Docker registry.
- **`--docker-password`**: Your password or access token for the Docker registry.
- **`--docker-email`**: Your email associated with the Docker registry account.

---

### Use private registry

```bash
kubectl create secret docker-registry regcred \
  --docker-server=myregistry.example.com \
  --docker-username=myusername \
  --docker-password=mypassword \
  --docker-email=myemail@example.com
```

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
  - name: mycontainer
    image: myregistry.example.com/myimage:latest
  imagePullSecrets:
  - name: regcred
```
