# Kubeadm

## Setup cluster

Init single Control-Plane:

```sh
kubeadm init --apiserver-advertise-address=192.168.56.11 --pod-network-cidr=10.244.0.0/16
```

Init HA cluster:

```sh
kubeadm init --apiserver-advertise-address=192.168.56.21 --control-plane-endpoint=192.168.56.10 --pod-network-cidr=10.
244.0.0/16 --upload-certs
```

Install Flannel:

```sh
wget https://github.com/flannel-io/flannel/releases/latest/download/kube-flannel.yml # Change CIDR
```

Join Control-Plane:

```sh
kubeadm init phase upload-certs --upload-certs

kubeadm token create --print-join-command

kubeadm join 192.168.56.10:6443 --token m5t146.2n3x7216onk2ch71 \
--discovery-token-ca-cert-hash sha256:3323c5688df4221bc2fe39d4b166d10fe7e954ddd9e7a176810a1c312bc429a9 \
--apiserver-advertise-address=192.168.56.22 \
--certificate-key=5e004720ad46cbbcc40b512f62f78decc7df5e7267eb0ce9638cded6dbb72111 --control-plane
```

Join node:

```sh
kubeadm token create --print-join-command
kubeadm join 192.168.56.11:6443 --token u6u99i.gbe1ao4glkq4spik \
--discovery-token-ca-cert-hash sha256:132add43ecb1197b53a5eba78e55b41bbe8dcabad876b7078c1efc13e7725499
```

Reset node:

```sh
kubeadm reset -f
kubectl delete node master-1 --force --grace-period=0
rm -rf /var/lib/etcd
```

## Update cluster

Update cluster:
```sh
# Step-by-step 1.33 > 1.34 #
kubeadm upgrade plan
kubeadm upgrade apply v1.19.0
```

Update Control-Plane:

```sh
kubeadm upgrade node
systemctl restart kubelet
```

Update worker:

```sh
kubectl drain worker-1 --ignore-daemonsets --delete-emptydir-data
kubeadm upgrade node
systemctl restart kubelet
```

## Renew certificate

```sh
# Check expiry
kubeadm certs check-expiration

# Renew all certs
kubeadm certs renew all

systemctl restart kubelet
```



## Etcd


Create backup:
```sh
ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379
--cacert=/etc/kubernetes/pki/etcd/ca.crt
--cert=/etc/kubernetes/pki/etcd/server.crt
--key=/etc/kubernetes/pki/etcd/server.key
snapshot save /tmp/etcd_backup.db
```


## Configuration

```sh
kubectl cluster-info # See HA status
kubectl get cm kubeadm-config -n kube-system -o yaml
```
