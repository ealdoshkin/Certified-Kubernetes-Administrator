# CRD

Узнать имя ресурса в crd:
```sh
kubectl api-resources

# Or

plural:
shortNames:
singular:
```

Fast create cr:
```sh
k create ns test --oyaml --dry-run=client > cr.yml
kubectl explain websites.example.com.spec >> cr.yml
```

Удалить CRD:
```
k delete websites.example.com cr-name my-blog test
k delete customresourcedefinitions.apiextensions.k8s.io websites.example.com
```
