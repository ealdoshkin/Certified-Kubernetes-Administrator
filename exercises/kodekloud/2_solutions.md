# Mock Exam 2 Solutions

## 1/11 - StorageClass

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: local-sc
  annotations:
    storageclass.kubernetes.io/is-default-class: "true"
provisioner: kubernetes.io/no-provisioner
allowVolumeExpansion: true
volumeBindingMode: WaitForFirstConsumer
```

---

## 2/11 - Deployment with Sidecar

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: logging-deployment
  namespace: logging-ns
spec:
  replicas: 1
  selector:
    matchLabels:
      app: logger
  template:
    metadata:
      labels:
        app: logger
    spec:
      volumes:
        - name: log-volume
          emptyDir: {}
      containers:
        - name: app-container
          image: busybox
          volumeMounts:
            - name: log-volume
              mountPath: /var/log/app
          command:
            - sh
            - -c
            - "while true; do echo 'Log entry' >> /var/log/app/app.log; sleep
5; done"
        - name: log-agent
          image: busybox
          volumeMounts:
            - name: log-volume
              mountPath: /var/log/app
          command:
            - tail
            - -f
            - /var/log/app/app.log
```

---

## 3/11 - Ingress

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: webapp-ingress
  namespace: ingress-ns
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  rules:
    - host: kodekloud-ingress.app
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: webapp-svc
                port:
                  number: 80
```

---

## 4/11 - Rolling Update

```bash
# Create deployment
kubectl create deployment nginx-deploy --image=nginx:1.16 --replicas=1

# Upgrade to 1.17
kubectl set image deployment/nginx-deploy nginx=nginx:1.17

# Verify rollout
kubectl rollout history deployment nginx-deploy
kubectl rollout history deployment nginx-deploy --revision=2
```

---

## 5/11 - RBAC and User

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: developer
  namespace: development
rules:
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["create", "list", "get", "update", "delete"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: john-developer-role-binding
  namespace: development
subjects:
  - kind: User
    name: john
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: developer
  apiGroup: rbac.authorization.k8s.io
```

```bash
# Create CSR
cat <<EOF | kubectl apply -f -
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: john-developer
spec:
  request: $(cat /root/CKA/john.csr | base64 | tr -d '\n')
  signerName: kubernetes.io/kube-apiserver-client
  expirationSeconds: 86400
  usages:
    - client auth
EOF

# Approve CSR
kubectl certificate approve john-developer

# Extract certificate
kubectl get csr john-developer -o jsonpath='{.status.certificate}' | base64
-d > john.crt

# Configure kubeconfig for john
kubectl config set-credentials john --client-certificate=john.crt
--client-key=/root/CKA/john.key
kubectl config set-context john-context --cluster=<cluster-name> --user=john
--namespace=development
```

---

## 6/11 - DNS Resolution

```bash
# Create pod
kubectl run nginx-resolver --image=nginx

# Expose service
kubectl expose pod nginx-resolver --name=nginx-resolver-service --port=80
--target-port=80 --type=ClusterIP

# Test service DNS
kubectl run test-nslookup --image=busybox:1.28 --rm -it --restart=Never --
nslookup nginx-resolver-service > /root/CKA/nginx.svc

# Test pod DNS (get pod IP first)
kubectl get pod nginx-resolver -o wide
kubectl run test-nslookup --image=busybox:1.28 --rm -it --restart=Never --
nslookup <pod-ip>.default.pod.cluster.local > /root/CKA/nginx.pod
```

---

## 7/11 - Static Pod

```bash
# Generate static pod manifest
kubectl run nginx-critical --image=nginx --dry-run=client -o yaml >
static.yaml

# Copy to node01 static pod path
scp static.yaml cluster1-node01:/etc/kubernetes/manifests/

# Or SSH to node and create directly
ssh cluster1-node01
cat <<EOF > /etc/kubernetes/manifests/nginx-critical.yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-critical
spec:
  containers:
    - name: nginx
      image: nginx
EOF
```

---

## 8/11 - Horizontal Pod Autoscaler

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: backend-hpa
  namespace: backend
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: backend-deployment
  minReplicas: 3
  maxReplicas: 15
  metrics:
    - type: Resource
      resource:
        name: memory
        target:
          type: Utilization
          averageUtilization: 65
```

```bash
kubectl apply -f webapp-hpa.yaml
```

---

## 9/11 - Gateway HTTPS

```yaml
apiVersion: gateway.networking.k8s.io/v1beta1
kind: Gateway
metadata:
  name: web-gateway
  namespace: cka5673
spec:
  gatewayClassName: kodekloud
  listeners:
    - allowedRoutes:
        namespaces:
          from: Same
      name: https
      port: 443
      protocol: HTTPS
      hostname: kodekloud.com
      tls:
        certificateRefs:
          - name: kodekloud-tls
```

---

## 10/11 - Helm Uninstall

```bash
# List all releases in all namespaces
helm list --all-namespaces

# Check manifests for vulnerable image
helm get manifest atlanta-page-apd -n atlanta-page-04 | grep -i
webapp-color:v1

# Uninstall the release
helm uninstall atlanta-page-apd -n atlanta-page-04
```

---

## 11/11 - NetworkPolicy

```bash
# Check available policies in /root
ls /root/*.yaml

# View each policy to find the most restrictive one
cat /root/policy1.yaml
cat /root/policy2.yaml
cat /root/policy3.yaml
```

Example most restrictive policy:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: backend-network-policy
  namespace: backend
spec:
  podSelector: {}
  policyTypes:
    - Ingress
  ingress:
    - from:
        - namespaceSelector:
            matchLabels:
              name: frontend
```
