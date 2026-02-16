**Worker Node – Change CRI (with kubeadm rejoin)**

1. `kubectl drain <node> --ignore-daemonsets`
2. Stop kubelet
3. `kubeadm reset`
4. Remove old CRI + CNI configs (`/etc/cni/net.d/*`)
5. Install new CRI
6. Configure CRI socket for kubelet
7. **Reboot (recommended if many old CNI processes)**
8. Start container runtime + kubelet
9. `kubeadm join ...`
10. `kubectl uncordon <node>`


**Control Plane Node – Change CRI (with kubeadm)**

1. `kubectl drain <master-node> --ignore-daemonsets --delete-emptydir-data`
2. Stop kubelet & container runtime
3. Remove old CRI + CNI configs (`/etc/cni/net.d/*`)
4. Install new CRI
5. Configure CRI socket for kubelet
6. **Reboot (recommended for clean state)**
7. Start container runtime + kubelet
8. If needed, `kubeadm init phase kubelet-start` or restart control plane components
9. `kubectl uncordon <master-node>`

**Note:** Backup etcd before making changes.
