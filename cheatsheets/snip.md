# Snip

Run pod command:
```yam
  containers:
  - name: busybox
    image: radial/busyboxplus:curl
    command: ['sh', '-c', 'while true; do sleep 3600; done']
```
```yam
  containers:
  - name: busybox
    image: radial/busyboxplus:curl
    command:
    - sh
    - c
    - while true; do echo hello; sleep 2; done
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
