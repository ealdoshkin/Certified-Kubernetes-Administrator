# Snip

Run pod command:
```yaml
  containers:
  - name: busybox
    image: radial/busyboxplus:curl
    command: ['sh', '-c', 'while true; do sleep 3600; done']
```
```yaml
  containers:
  - name: busybox
    image: radial/busyboxplus:curl
    command:
    - sh
    - c
    - while true; do echo hello; sleep 2; done
```

Nginx with custom port and welcome:
```yaml
    image: nginx
    command: ["/bin/sh"]
    args: ["-c", "echo 'worked' > /usr/share/nginx/html/index.html && echo 'server { listen 8080; root /usr/share/nginx/html; }' > /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'"]
    ports:
    - containerPort: 8080
```


Images:
```yaml
  containers:
  - name: webapp-green
    image: kodekloud/webapp-color
    args: ["--color","green"]
```


Deployment rollout stragetegy:

```yaml
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
```

Parallelistm in job:
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  creationTimestamp: null
  labels:
    run: busybox
  name: busybox
spec:
  parallelism: 5 # add this line
```

Autoterminate Job:

```yaml
```bash
apiVersion: batch/v1
kind: Job
metadata:
  creationTimestamp: null
  labels:
    run: busybox
  name: busybox
spec:
  activeDeadlineSeconds: 30 # add this line
```
