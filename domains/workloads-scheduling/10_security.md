### Pod Security

---

Pod and container level


## SecurityContext (Pod + Container)

```yaml
spec:
  securityContext:
    runAsNonRoot: true # запрет root
    runAsUser: 1000 # явный UID (иначе берётся из image)
    fsGroup: 2000 # права записи в volumes (PVC/emptyDir)

  containers:
    - name: app
      image: nginx
      securityContext:
        readOnlyRootFilesystem: true # root FS только чтение
        allowPrivilegeEscalation: false # запрет setuid/setgid
        privileged: false # нет полного доступа к хосту
        capabilities:
          drop: ["ALL"] # убрать все Linux capabilities
          add: ["NET_BIND_SERVICE"] # только если нужен порт <1024
```

---

## Pod Security Admission (PSA — Namespace)

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: secure
  labels:
    pod-security.kubernetes.io/enforce: restricted # строгая политика
```

Или:

```bash
kubectl label ns secure pod-security.kubernetes.io/enforce=restricted
```

---

## Host Access (почти всегда false)

```yaml
spec:
  hostNetwork: false # нет сети хоста
  hostPID: false # нет процессов хоста
  hostIPC: false # нет IPC хоста
```

Опасный volume:

```yaml
volumes:
  - name: host
    hostPath:
      path: /var/run # прямой доступ к ноде — избегать
```

---

## Seccomp

```yaml
securityContext:
  seccompProfile:
    type: RuntimeDefault # безопасный профиль по умолчанию
    # Unconfined = отключена защита (ошибка)
```

---

## Быстрая проверка

```bash
kubectl get pod <pod> -o yaml | grep -A 5 securityContext
```

---

## Красные флаги (что исправлять)

```yaml
privileged: true # полный доступ к хосту
runAsUser: 0 # root
allowPrivilegeEscalation: true # возможна эскалация
hostNetwork: true # сеть ноды
capabilities: ["ALL"] # лишние права
seccompProfile: Unconfined # нет syscall-фильтра
```

**Мантра:** `nonRoot + noEscalation + drop ALL + restricted PSA + RuntimeDefault`.
