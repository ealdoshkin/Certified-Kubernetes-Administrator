# Mock Exam 1 Solutions

---

## 1/12 (Weight: 8)

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mc-pod
spec:
  volumes:
    - name: shared-volume
      emptyDir: {}
  containers:
    - image: nginx:1-alpine
      name: mc-pod-1
      env:
        - name: NODE_NAME
          valueFrom:
            fieldRef:
              fieldPath: spec.nodeName
    - name: mc-pod-2
      image: busybox:1
      command:
        - "sh"
        - "-c"
        - "while true; do date >> /var/log/shared/date.log; sleep 1; done"
      volumeMounts:
        - name: shared-volume
          mountPath: /var/log/shared
    - name: mc-pod-3
      image: busybox:1
      command:
        - "sh"
        - "-c"
        - "tail -f /var/log/shared/date.log"
      volumeMounts:
        - name: shared-volume
          mountPath: /var/log/shared
  resources: {}
  dnsPolicy: ClusterFirst
  restartPolicy: Always
```

---

## 2/12 (Weight: 7)

```sh
dpkg -i /root/cri-docker_0.3.16.3-0.debian.deb
systemctl enable --now cri-docker
```

---

## 3/12 (Weight: 6)

```sh
kubectl get crd | grep -i verticalpodautoscaler > /root/vpa-crds.txt
```

Or:

```sh
kubectl get crd | grep -i vpa > /root/vpa-crds.txt
```

---

## 4/12 (Weight: 8)

```sh
kubectl expose pod messaging --port=6379 --name=messaging-service
```

---

## 5/12 (Weight: 10)

```sh
kubectl create deployment hr-web-app --image=kodekloud/webapp-color --replicas=2
```

Or using YAML:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hr-web-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: hr-web-app
  template:
    metadata:
      labels:
        app: hr-web-app
    spec:
      containers:
        - name: webapp-color
          image: kodekloud/webapp-color
```

---

## 6/12 (Weight: 12)

Identify and fix the issue with the `orange` application. Common issues to check:

```sh
# Check pod status and events
kubectl get pods
kubectl describe pod orange
kubectl logs orange

# Common fix - if init container has wrong command:
kubectl edit deployment orange
```

Typical fix: Correct the init container command or image pull policy issue.

---

## 7/12 (Weight: 8)

```sh
kubectl expose deployment hr-web-app --type=NodePort --port=8080 --name=hr-web-app-service --dry-run=client -o yaml > question7.yaml
```

Then edit `question7.yaml` to set `nodePort: 30082`:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: hr-web-app-service
spec:
  type: NodePort
  ports:
    - port: 8080
      targetPort: 8080
      nodePort: 30082
  selector:
    app: hr-web-app
```

Apply:

```sh
kubectl apply -f question7.yaml
```

---

## 8/12 (Weight: 8)

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-analytics
spec:
  capacity:
    storage: 100Mi
  volumeMode: Filesystem
  accessModes:
    - ReadWriteMany
  hostPath:
    path: /pv/data-analytics
```

---

## 9/12 (Weight: 10)

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: webapp-hpa
  namespace: default
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: kkapp-deploy
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 50
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
```

Save as `/root/webapp-hpa.yaml` and apply:

```sh
kubectl apply -f /root/webapp-hpa.yaml
```

---

## 10/12 (Weight: 9)

```yaml
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: analytics-vpa
  namespace: default
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: analytics-deployment
  updatePolicy:
    updateMode: "Auto"
```

---

## 11/12 (Weight: 6)

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: web-gateway
  namespace: nginx-gateway
spec:
  gatewayClassName: nginx
  listeners:
    - name: http
      protocol: HTTP
      port: 80
```

---

## 12/12 (Weight: 8)

```sh
# Update helm repository
helm repo update

# Upgrade the helm chart
helm upgrade kk-mock1 nginx/nginx -n kk-ns --version 18.1.15
```

Or if using local chart:

```sh
helm repo update
helm upgrade kk-mock1 . -n kk-ns --version 18.1.15
```

---
