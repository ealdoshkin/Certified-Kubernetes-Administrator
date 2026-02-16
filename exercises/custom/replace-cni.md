# Switch flannel to calico

- drain nodes
- delete flannel ns
- clean /etc/cni/net.d + /var/lib/cni on all nodes
- ip link delete cni0, flannel
- restart kubelet
- install calico
- uncordon nodes
