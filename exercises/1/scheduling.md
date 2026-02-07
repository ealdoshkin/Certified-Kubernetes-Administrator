### Create a configmap named `my-configmap` with two values, one single line and one multi-line

<details><summary>show</summary>
<p>

```bash
# create a configmap with a siingle line and a multi-line
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-configmap
data:
  single: "This is a single line value"
  multi: |
    This is a multi-line value.
    It spans multiple lines.
    You can include as many lines as needed.
EOF

# view the configmap data in the cluster
kubectl describe cm my-configmap

```

### Use the configMap `my-configmap` in a deployment named `my-nginx-deployment` that uses the image `nginx:latest` mounting the configMap as a volume

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-nginx-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        volumeMounts:
        - name: config-volume
          mountPath: /etc/config
          readOnly: true
      volumes:
      - name: config-volume
        configMap:
          name: my-configmap
```

</p>
</details>

### Use the configMap `my-configmap` as an environment variable in a deployment named `mynginx-deploy` that uses the image `nginx-latest`, passing in the single line value as an environment variable named `SINGLE_VALUE` and the multi-line value as `MULTI_VALUE`

<details><summary>show</summary>
<p>

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mynginx-deploy
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        env:
        - name: SINGLE_VALUE
          valueFrom:
            configMapKeyRef:
              name: my-configmap
              key: single
        - name: MULTI_VALUE
          valueFrom:
            configMapKeyRef:
              name: my-configmap
              key: multi

```

### Create a secret via yaml that contains two base64 encoded values


```bash
# create two base64 encoded strings
echo -n 'secret' | base64

echo -n 'anothersecret' | base64

# create a file named secret.yml
apiVersion: v1
kind: Secret
metadata:
  name: my-secret
type: Opaque
data:
  secretkey1: <base64 String 1>
  secretkey2: <base64 String 2>

# create a secret
kubectl create -f secretl.yml
```

</p>
</details>



### Create a new pod named “ssd-pod” using the nginx image. Use node affinity to select nodes based on a weight of 1 to nodes labeled “disk=ssd”. If the selection criteria don’t match, it can also choose nodes that have the label “kubernetes.io/os=linux”

<details><summary>show command</summary>
<p>

```bash
# create the YAML for a pod named 'ssd-pod'
kubectl run ssd-pod --image nginx --dry-run=client -o yaml > pod.yaml
```

```yaml
# pod.yaml file
apiVersion: v1
kind: Pod
metadata:
  creationTimestamp: null
  labels:
    run: ssd-pod
  name: ssd-pod
spec:
############## START HERE ############################
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: kubernetes.io/os
            operator: In
            values:
            - linux
      preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 1
        preference:
          matchExpressions:
          - key: disk
            operator: In
            values:
            - ssd
############## END HERE ############################
  containers:
  - image: nginx
    name: ssd-pod
```
