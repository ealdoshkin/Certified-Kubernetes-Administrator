# 🟢 NetworkPolicy

## 1. Применение

- Политика применяется к Pod’ам через `podSelector`.
- Всё, что **не разрешено явно**, блокируется (implicit deny).
- Применяется **в пределах namespace**.
- Для всего namespace → `podSelector: {}`.
- **OR** | **AND** условия (см. пример )
- При создании Egress, разрешаем DNS-query

## 2. Типы трафика

- `Ingress` — входящий
- `Egress` — исходящий
- Можно комбинировать (`policyTypes: Ingress, Egress`)

## 3. Условия (Selectors)

- `from` / `to` → несколько элементов = **OR**
- Можно комбинировать:

  - `podSelector`
  - `namespaceSelector`
  - `ipBlock` (с `except` для исключений)

## 4. Порты

- Указывать не обязательно → разрешены все порты/протоколы
- Можно указывать `protocol: TCP|UDP` + `port`

## 5. Особенности

- DNS блокируется через Egress → нужно разрешать явно (`namespace: kube-system`, Pod: `k8s-app=kube-dns`)
- Нельзя привязываться к именам сервисов
- Политика по умолчанию разрешает весь трафик → полный запрет нужно явно указывать
- Для доступа к целому namespace нужно создать label (если явно не просят)

## 6. ipBlock

- Позволяет разрешать/запрещать диапазоны IP (`cidr`)
- `except` → исключения из диапазона

---

## Команды

```bash
# Посмотреть все NetworkPolicy
kubectl describe netpol

# Посмотреть конкретную политику
kubectl describe netpol <имя> -n <namespace>

# Узнать PodCIDR
kubectl describe nodes <node> | grep Cidr
```

---

## 🔹 Базовый шаблон

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: app-policy
  namespace: secure
spec:
  podSelector:
    matchLabels:
      app: web # Применяется к Pod с label app=web, всё остальное блокируется (для лейбла!)
  policyTypes:
    - Ingress
    - Egress
  ingress:
    - from:
        - podSelector:
            matchLabels:
              app: ingress-nginx # Разрешить от Pod с app=ingress-nginx
        - podSelector:
            matchLabels:
              app: ingress-traeffic # Или от Pod из локального нейспейса (OR)
      ports:
        - protocol: TCP
          port: 443 # Разрешить только TCP 443, иначе все порты разрешены
  egress:
    - to:
        - namespaceSelector:
            matchLabels:
              kubernetes.io/metadata.name: kube-system # Разрешить только к Pod в kube-system
          podSelector:
            matchLabels:
              k8s-app: kube-dns # Только Pod с k8s-app=kube-dns и из kube-system (AND)
      ports:
        - protocol: UDP
          port: 53 # Разрешить DNS только по UDP 53, всё остальное запрещено
```
