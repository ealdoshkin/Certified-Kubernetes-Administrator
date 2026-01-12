#!/bin/bash
echo "=== Restoring normal system time ==="
echo

# 1. Stop kubelet and services again
echo "[1/6] Stopping Kubernetes services..."
sudo systemctl stop kubelet docker containerd
echo "Services stopped."

# 2. Enable and force time synchronization
echo "[2/6] Enabling time synchronization..."
sudo systemctl enable systemd-timesyncd
sudo systemctl start systemd-timesyncd
sudo timedatectl set-ntp true
echo "Time sync enabled."

# 3. Force immediate sync with NTP servers
echo "[3/6] Forcing immediate time sync..."
sudo systemctl restart systemd-timesyncd
sleep 2
sudo timedatectl set-ntp false
sudo timedatectl set-ntp true
echo "Time sync triggered."

# 4. Verify synchronization
echo "[4/6] Verifying time sync status..."
timedatectl status
echo "Waiting for sync to complete..."
sleep 5

# 5. Show before/after time
echo "[5/6] Time adjustment complete:"
echo "Current system time: $(date)"
echo "Real-world time should now be correct."

# 6. Restart services
echo "[6/6] Restarting Kubernetes services..."
sudo systemctl start docker containerd kubelet
echo "Services restarted."
echo
echo "=== IMPORTANT NEXT STEPS ==="
echo "1. Check if control plane is healthy: sudo kubectl get pods -n kube-system"
echo "2. Renew certificates if needed: sudo kubeadm certs renew all"
echo "3. Restart static pods: sudo systemctl restart kubelet"
echo "4. Full system reboot is recommended to clear any time-related issues."