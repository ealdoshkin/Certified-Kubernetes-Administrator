# Task: Troubleshoot Kubelet Failure

## Objective
Troubleshoot and fix kubelet service issues.

## Scenario: Kubelet Service Failure

```bash
# Simulate kubelet issue
curl https://raw.githubusercontent.com/chadmcrowell/acing-the-cka-exam/main/ch_08/10-kubeadm.conf \
  --silent --output /etc/systemd/system/kubelet.service.d/10-kubeadm.conf

# Reload systemd and restart kubelet
systemctl daemon-reload
systemctl restart kubelet
```

## Troubleshooting Steps

### 1. Check Kubelet Status
```bash
# Check kubelet service status
systemctl status kubelet

# Check if kubelet is running
ps aux | grep kubelet
```

### 2. Check Kubelet Logs
```bash
# View kubelet logs
journalctl -u kubelet -n 50

# Follow kubelet logs
journalctl -u kubelet -f
```

### 3. Check Kubelet Configuration
```bash
# Check kubelet config file
cat /etc/systemd/system/kubelet.service.d/10-kubeadm.conf

# Check kubelet config
cat /var/lib/kubelet/config.yaml
```

### 4. Check Node Status
```bash
# Check if node is ready
kubectl get nodes

# Describe node
kubectl describe node <node-name>
```

## Fix: Restore Kubelet

### Option 1: Restore Configuration
```bash
# Backup current config
cp /etc/systemd/system/kubelet.service.d/10-kubeadm.conf /tmp/

# Restore from backup or recreate
cat <<EOF | sudo tee /etc/systemd/system/kubelet.service.d/10-kubeadm.conf
[Service]
Environment="KUBELET_KUBECONFIG_ARGS=--bootstrap-kubeconfig=/etc/kubernetes/bootstrap-kubelet.conf --kubeconfig=/etc/kubernetes/kubelet.conf"
Environment="KUBELET_CONFIG_ARGS=--config=/var/lib/kubelet/config.yaml"
EnvironmentFile=-/var/lib/kubelet/kubeadm-flags.env
ExecStart=
ExecStart=/usr/bin/kubelet \$KUBELET_KUBECONFIG_ARGS \$KUBELET_CONFIG_ARGS \$KUBELET_KUBEADM_ARGS \$KUBELET_EXTRA_ARGS
EOF

# Reload and restart
systemctl daemon-reload
systemctl restart kubelet
```

### Option 2: Reinstall Kubelet
```bash
# Reinstall kubelet
sudo apt-get install --reinstall kubelet

# Restart service
systemctl restart kubelet
systemctl enable kubelet
```

## Verification
```bash
# Check kubelet status
systemctl status kubelet

# Check node is ready
kubectl get nodes

# Test pod creation
kubectl run test-pod --image nginx
kubectl get pod test-pod
```

## Key Concepts
- **Kubelet**: Node agent that runs pods
- **Systemd Service**: Kubelet runs as systemd service
- **Configuration**: `/etc/systemd/system/kubelet.service.d/10-kubeadm.conf`
- **Logs**: Journalctl for systemd service logs

## Common Issues
- Configuration file errors
- Certificate issues
- Network connectivity
- Resource constraints
- CRI (Container Runtime) issues
