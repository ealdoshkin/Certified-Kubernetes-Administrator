# Short command

## 1. Generate YAML (without creating) — preferred for templates

Use `--dry-run=client -o yaml`.

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
