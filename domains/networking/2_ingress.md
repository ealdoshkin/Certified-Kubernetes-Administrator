# Ingress

### 1️⃣ Проверка Ingress / TLS / Events

```bash
kubectl describe ingress <ingress-name> -n <namespace>
# проверяем:
# - TLS Secret
# - Endpoints
# - Events
```

---

### 2️⃣ Важные аннотации (NGINX)

```yaml
metadata:
  annotations:
    nginx.ingress.kubernetes.io/ssl-redirect: "true"       # HTTP → HTTPS
    nginx.ingress.kubernetes.io/force-ssl-redirect: "true" # принудительный redirect
    nginx.ingress.kubernetes.io/backend-protocol: https    # backend HTTPS
    nginx.ingress.kubernetes.io/rewrite-target: /          # переписывание пути
    nginx.ingress.kubernetes.io/use-regex: "true"          # поддержка regex в path
    nginx.ingress.kubernetes.io/canary: "true"            # включить canary
    nginx.ingress.kubernetes.io/canary-weight: "10"       # % трафика для canary
```

> Для CKA чаще всего нужны: **ssl-redirect / force-ssl-redirect / rewrite-target / use-regex**
> Пример: path: /v1/app → сервис ждёт / → rewrite-target: /.

---

### 3️⃣ Класс Ingress

```bash
kubectl get ingressclass -A
```

```yaml
spec:
  ingressClassName: nginx  # указываем нужный контроллер
```

* Без ingressClassName → Ingress может игнорироваться контроллером
* Позволяет иметь несколько контроллеров в кластере

---

### 4️⃣ Типы путей (`pathType`)

| Тип    | Описание                     |
| ------ | ---------------------------- |
| Prefix | Совпадение по приставке пути |
| Exact  | Точное совпадение пути       |

> Classic trap: `/app` + `Exact` не совпадет с `/app/`

---

### 5️⃣ Отключение HTTP (только HTTPS)

```yaml
metadata:
  annotations:
    nginx.ingress.kubernetes.io/force-ssl-redirect: "true" # редирект HTTP → HTTPS
```

* Для полного отключения HTTP (порт 80) → настройка **Ingress Controller**:

  * NGINX: `--http-port=0 --https-port=443`
* Kubernetes Ingress YAML сам по себе порт 80 не отключает

---


### Проверка host header


### 6️⃣ Краткие советы / трюки для CKA

* Ingress → Service.port, **не targetPort**
* TLS Secret должен быть в **том же namespace**
* Multi-host Ingress → проверяй **host header** `curl -k -H "Host: k8s.dev" https://host`
* 404 чаще всего: **host/path mismatch** или **нет ingressClass**
* Always specify `pathType` для предсказуемого поведения

