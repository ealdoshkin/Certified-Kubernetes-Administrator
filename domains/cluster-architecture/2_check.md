# K8s health check

```sh
k cluster-info
k get cs
k get nodes -A -owide
```


## Check kubeconfig

```sh
kubectl --kubeconfig controller-manager.conf auth whoami
kubectl --kubeconfig controller-manager.conf get ns
kubectl auth can-i --list --kubeconfig=admin.conf

```

Check certificate validity:
```sh
kubectl --kubeconfig kubelet.conf config view --raw \
  -o jsonpath='{.users[0].user.client-certificate-data}' \
  | base64 -d | openssl x509 -noout -subject (-enddate)
```
