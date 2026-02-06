# Gateway API

Следующее поколение ingress

- Имеет возможность обрабатывать L4
- Универсальные анотации
- Blue-green deploy
- Обработка HTTP header
- Взаимодействие между namespace

**Gateway API Controller** - компонент настраивающий маршруты

## Nginx Gateway Fabric

- Control Plane Controller - смотрит CRD
- Date plane - настраивает трафик

Установка:

CRD:

```sh
# Maybe conflict with Controller version
kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.4.0/standard-install.yaml

```

NGF:

```sh
helm show values oci://ghcr.io/nginx/charts/nginx-gateway-fabric > ngf.yaml
helm install ngf oci://ghcr.io/nginx/charts/nginx-gateway-fabric -f ngf.yaml --create-namespace -n nginx-gateway
```

Смотрим ресурсы:

```sh
kubectl api-resources --api-group=gateway.networking.k8s.io
```

## Gateway Resources

- GatewayClass - выбрать нужный контроллер
- Gateway - как трафик заходит в кластер
- HTTPRoute - заводим HTTP трафик на сервис
- gRPCRoute - gRPC на сервис
- ReferenceGrants - настройка трафика на разные namespaces

Проверяем ресурсы после создания:

```sh
k -n webserver get gateway  # Attached Routes: 1
k -n webserver describe httproute # Backend service | Message
k -n webserver exec -it <CONTROLLER POD NAME> -- nginx -T # Pod IPs
```

Migration from Ingress → Gateway + HttpRoute, etc.
