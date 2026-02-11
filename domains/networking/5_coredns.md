# CoreDNS (CKA)

[Custom DNS](https://kubernetes.io/docs/tasks/administer-cluster/dns-custom-nameservers/)

**Порты:** 53/UDP, 53/TCP (DNS), 9153/TCP (Prometheus)

**Что востановить dns имя**
cat /etc/resolv.con | grep cluster.local

**Обращаемся к service в пределах namespace**
`ping api`

**Обращаемся к service в другом namespace**
`ping api.namespace`

**Проверка службы:**
kubectl -n kube-system get svc kube-dns
# ClusterIP обычно 10.96.0.10

**Установка инструментов для теста:**
apk add bind-tools  # alpine

**Перезапуск CoreDNS:**
kubectl -n kube-system rollout restart deployment coredns

## Основные секции Corefile

- `kubernetes {}` – плагин для разрешения имён сервисов и pod’ов в cluster.local
- `log`, `errors` – логирование запросов и ошибок
- `hosts {}` – статические хосты (aka_/etc/hosts), использовать `fallthrough` для остальных запросов
- `forward . 1.1.1.1` – перенаправление всех внешних запросов на указанный DNS
- доп. блок: consul.local:53 {forward . 10.150.0.1} - все запросы *.cluster.local перенаправить
- `rewrite name substring svc.cka.example.com svc.cluster.local` - переписать на svc.cluster.local
