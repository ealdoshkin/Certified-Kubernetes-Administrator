# Reconfigure Kubernetes Service CIDR and DNS

## **Question:**

How do I change the Service CIDR to `100.96.0.0/16`, update the DNS Service IP, and ensure new Pods use the new DNS configuration?

---

## **Solution Steps:**

| Step   | Action                                  | Command/File                                                                                                 |
| ------ | --------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **1**  | Edit API server config                  | `vim /etc/kubernetes/manifests/kube-apiserver.yaml`                                                          |
|        | Change `--service-cluster-ip-range`     | to `100.96.0.0/16`                                                                                           |
| **2**  | Delete existing services                | `kubectl -n kube-system delete svc kube-dns` <br> `kubectl delete svc kubernetes`                            |
| **3**  | Delete old ServiceCIDR                  | `kubectl delete servicecidr kubernetes`                                                                      |
| **4**  | Verify new CIDR                         | `kubectl get servicecidr`                                                                                    |
| **5**  | Recreate `kubernetes` Service           | `kubectl create -f kubernetes-service.yaml`                                                                  |
| **6**  | Recreate `kube-dns` Service with new IP | to `100.96.0.10` > `kubectl create -f coredns-service.yaml`                                                  |
| **7**  | Update kubelet config file              | `vim /var/lib/kubelet/config.yaml` → set `clusterDNS: [100.96.0.10]`                                         |
| **8**  | Edit kubelet ConfigMap                  | `kubectl -n kube-system edit cm kubelet-config`                                                              |
| **9**  | Upgrade node kubelet config             | `kubeadm upgrade node phase kubelet-config`                                                                  |
| **10** | Restart kubelet                         | `systemctl daemon-reload && systemctl restart kubelet`                                                       |
| **11** | Test with new Pod                       | `kubectl run netshoot --image=nicolaka/netshoot -- sleep 3600`                                               |
| **12** | Verify DNS                              | `kubectl exec -it netshoot -- cat /etc/resolv.conf` <br> `kubectl exec -it netshoot -- nslookup example.com` |

---

## **Key Files to Modify:**

- `/etc/kubernetes/manifests/kube-apiserver.yaml` — API server static pod manifest
- `/var/lib/kubelet/config.yaml` — Kubelet local configuration
- `kubelet-config` ConfigMap in `kube-system` namespace — Kubelet dynamic configuration

## **Verification Commands:**

```bash
kubectl get svc -A                    # Check Service IPs in new range
kubectl get po netshoot -o wide       # Verify pod running
kubectl exec -it netshoot -- bash     # Enter test container
cat /etc/resolv.conf                  # Confirm nameserver 100.96.0.10
nslookup example.com                  # Test DNS resolution
```
