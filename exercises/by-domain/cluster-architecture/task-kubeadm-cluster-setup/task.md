# Task: kubeadm Cluster Setup

## Objective
Set up a Kubernetes cluster using kubeadm with master and worker nodes.

## Requirements
- Master node: `ik8s-master-0`
- Worker node: `ik8s-node-0`
- Use kubeadm configuration file: `/etc/kubeadm.conf`
- Use `--ignore-preflight-errors=all` flag
- Install CNI plugin (Calico recommended)

## Solution

### Step 1: Configure Master Node
```bash
# SSH to master node
ssh ik8s-master-0

# Assume elevated privileges
sudo -i

# Initialize cluster with kubeadm config
kubeadm init --config=/etc/kubeadm.conf --ignore-preflight-errors=all

# Set up kubeconfig
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

### Step 2: Install CNI Plugin
```bash
# Install Calico CNI
kubectl apply -f https://docs.projectcalico.org/v3.14/manifests/calico.yaml

# Or use other CNI plugins
# kubectl apply -f <cni-manifest-url>
```

### Step 3: Get Join Command
```bash
# Get join command from master
kubeadm token create --print-join-command
```

### Step 4: Join Worker Node
```bash
# SSH to worker node
ssh ik8s-node-0

# Assume elevated privileges
sudo -i

# Join cluster using command from master
kubeadm join <master-ip>:<port> --token <token> --discovery-token-ca-cert-hash sha256:<hash> --ignore-preflight-errors=all
```

## Key Concepts
- **kubeadm**: Tool for bootstrapping Kubernetes clusters
- **Master Node**: Control plane node
- **Worker Node**: Worker node that joins cluster
- **CNI Plugin**: Container Network Interface plugin
- **Preflight Checks**: Validation before cluster setup

## Verification
```bash
# Check nodes
kubectl get nodes

# Check cluster status
kubectl cluster-info

# Check pods in kube-system
kubectl get pods -n kube-system
```

## Important Notes
- Use --ignore-preflight-errors=all for lab environments
- CNI plugin required for pod networking
- Master node must be initialized first
- Worker nodes join using token from master

## Common CNI Plugins
- Calico
- Flannel
- Weave Net
- Cilium
