# Task: Upgrade Control Plane Components with kubeadm

## Objective
Upgrade the control plane components using kubeadm to version 1.31.6, including kubelet and kubectl.

## Steps

### 1. Check Current Version and Plan Upgrade
```bash
# List control plane components and their versions
kubeadm upgrade plan
```

### 2. Upgrade Control Plane Components
```bash
# Apply the upgrade to 1.31.6
kubeadm upgrade apply v1.31.6
```

### 3. Upgrade kubeadm (if needed)
If you get a message that kubeadm needs to be upgraded first:

```bash
# Download the public signing key
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.31/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg

# Add Kubernetes apt repository
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.31/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list

# Update kubeadm to version 1.31.6-1.1
sudo apt install -y kubeadm=1.31.6-1.1

# Try upgrade again
kubeadm upgrade apply v1.31.6 -y
```

### 4. Verify Upgrade
```bash
# Check upgrade plan again to verify everything is at 1.31.6
kubeadm upgrade plan

# Verify kubelet version
kubelet --version

# Verify kubectl version
kubectl version --client
```

## Key Concepts
- **kubeadm upgrade**: Tool for upgrading Kubernetes clusters
- **Control Plane Components**: API server, etcd, scheduler, controller manager
- **Version Compatibility**: Ensure kubeadm version supports target Kubernetes version

## Notes
- Always backup etcd before upgrading
- Drain nodes before upgrading worker nodes
- Upgrade control plane first, then worker nodes
