# Kubeadm tasks

---

## 1. Cluster Initialization (MOST COMMON)

### 1.1 Initialize a Control Plane with kubeadm

Typical wording:

> “Initialize a Kubernetes cluster using kubeadm”

You may be required to:

- Run `kubeadm init`
- Specify:

  - Pod CIDR (for CNI)
  - CRI socket (if containerd)
  - Advertise address

- Configure kubectl for the admin user

Skills tested:

```bash
kubeadm init --pod-network-cidr=10.244.0.0/16
mkdir -p $HOME/.kube
cp /etc/kubernetes/admin.conf $HOME/.kube/config
chown $(id -u):$(id -g) $HOME/.kube/config
```

---

## 2. Node Joining (VERY COMMON)

### 2.1 Join Worker Node to Cluster

Typical wording:

> “Add this node to the existing cluster”

You must:

- Generate join command on control plane
- Execute it on worker node

Skills tested:

```bash
kubeadm token create --print-join-command
kubeadm join ...
```

Variants:

- Join using a specific token
- Join after token expired (regenerate token)

---

## 3. kubeadm Reset & Re-initialization

### 3.1 Reset a Node

Typical wording:

> “Reset the node so it can rejoin the cluster”

Skills tested:

```bash
kubeadm reset -f
rm -rf ~/.kube
```

Sometimes combined with:

- Re-joining the node
- Fixing a broken cluster

---

## 4. CNI Installation After kubeadm Init

### 4.1 Install a Pod Network Add-on

Typical wording:

> “Install a network plugin so pods can communicate”

Usually:

- Flannel
- Calico

Skills tested:

```bash
kubectl apply -f flannel.yaml
```

Important:

- You must match `--pod-network-cidr` with CNI
- Pods remain `NotReady` until CNI installed

---

## 5. kubeadm Configuration Files (LESS COMMON)

### 5.1 Initialize Using a kubeadm Config File

Typical wording:

> “Initialize the cluster using the provided kubeadm configuration file”

Skills tested:

```bash
kubeadm init --config kubeadm-config.yaml
```

May include:

- API server extra args
- Networking section
- CRI socket config

---

## 6. Certificates & kubeadm (RARE BUT POSSIBLE)

### 6.1 Check Certificate Expiration

Typical wording:

> “Check the expiration of Kubernetes certificates”

Skills tested:

```bash
kubeadm certs check-expiration
```

---

### 6.2 Renew Certificates

Typical wording:

> “Renew all expired certificates”

Skills tested:

```bash
kubeadm certs renew all
systemctl restart kubelet
```

---

## 7. Control Plane Troubleshooting with kubeadm

### 7.1 Control Plane Not Starting

Typical wording:

> “The control plane is not functioning. Investigate and fix.”

You may need to:

- Inspect static pods:

```bash
ls /etc/kubernetes/manifests
```

- Check kubelet logs
- Re-run:

```bash
kubeadm init phase control-plane all
```

---

## 8. kubeadm Phases (ADVANCED / RARE)

### 8.1 Run Specific kubeadm Phases

Typical wording:

> “Run only the required kubeadm phase to fix the issue”

Skills tested:

```bash
kubeadm init phase kubeconfig admin
kubeadm init phase control-plane apiserver
```

---

## 9. kubeadm Upgrade Tasks (VERY IMPORTANT)

### 9.1 Upgrade Control Plane Version

Typical wording:

> “Upgrade the Kubernetes control plane to version X”

Skills tested:

```bash
apt update
apt install kubeadm=1.28.x-00
kubeadm upgrade plan
kubeadm upgrade apply v1.28.x
```

---

### 9.2 Upgrade Worker Nodes

Typical wording:

> “Upgrade the worker node components”

Skills tested:

```bash
kubectl drain node1 --ignore-daemonsets
apt install kubeadm kubelet kubectl
kubeadm upgrade node
systemctl restart kubelet
kubectl uncordon node1
```

---

## 10. kubeadm Token Management

### 10.1 Create / List Tokens

Typical wording:

> “Create a new join token”

Skills tested:

```bash
kubeadm token list
kubeadm token create
```

---

## 11. kubeadm + CRI Configuration

### 11.1 Specify CRI Socket

Typical wording:

> “Initialize cluster using containerd”

Skills tested:

```bash
kubeadm init --cri-socket=unix:///run/containerd/containerd.sock
```

---

## 12. kubeadm Cleanup / Recovery

### 12.1 Recover from Failed Init

Typical wording:

> “kubeadm init failed. Fix and retry.”

Skills tested:

```bash
kubeadm reset -f
kubeadm init ...
```

---

## What Will NOT Appear ❌

These are **not** tested in CKA:

- kubeadm HA multi-control-plane setup
- etcd manual cluster creation
- kubeadm alpha commands
- Custom CA creation
- External etcd with kubeadm

---

## Exam Frequency Summary

| Topic           | Likelihood |
| --------------- | ---------- |
| kubeadm init    | ⭐⭐⭐⭐⭐ |
| kubeadm join    | ⭐⭐⭐⭐⭐ |
| CNI install     | ⭐⭐⭐⭐⭐ |
| Upgrade cluster | ⭐⭐⭐⭐   |
| Reset node      | ⭐⭐⭐     |
| Certificates    | ⭐⭐       |
| Phases          | ⭐         |

---
