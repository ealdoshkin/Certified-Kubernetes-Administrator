# Helm

```sh
source <(helm completion bash)
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm search repo prometheus

helm lint ./chart - проверить линтером целостность

helm pull prometheus-community/kube-prometheus-stack --untar -d .
helm show values prometheus-community/kube-prometheus-stack > values.yaml

helm install --generate-name ./chart
helm install prom prometheus-community/kube-prometheus-stack -f values.yaml -n monitoring --create-namespace --set imageTag=tdd
helm upgrade prom prometheus-community/kube-prometheus-stack -f values.yaml -n monitoring
helm uninstall -n monitoring prom

helm template prometheus-community/kube-prometheus-stack -f values.yaml > check.yml # From repo
helm get manifest -n argocd argo > check2.yml #All Manifests from cluster
helm get value -n argocd argo

helm ls -A
helm history -n argocd argo
helm rollback
```


## ApiVersion
- v1 (Helm2)
- v2 (Helm3)
