# 🎯 Affinity | Anti-Affinity

Kubernetes предоставляет несколько механизмов для привязки подов к нодам и друг к другу:

| Механизм                         | Тип правила           | Описание                                                                       | Особенности                                                                           |
| :------------------------------- | :-------------------- | :----------------------------------------------------------------------------- | :------------------------------------------------------------------------------------ |
| **nodeName**                     | Прямое назначение     | Жёсткое указание конкретной ноды в spec.nodeName. Taint работает               | Обходит scheduler, не является affinity-механизмом, не балансирует нагрузку.          |
| **nodeSelector**                 | Жёсткое (Node)        | Простой выбор узлов по меткам в `spec.nodeSelector`.                           | Базовый фильтр, часть NodeAffinity.                                                   |
| **Node Affinity**                | Жёсткое/Мягкое (Node) | Расширенный выбор узлов через `matchExpressions` (`In`, `Exists`, `Gt` и др.). | `requiredDuringScheduling...` — жёстко, `preferredDuringScheduling...` — мягко.       |
| **Pod Affinity / Anti-Affinity** | Жёсткое/Мягкое (Pod)  | Размещение пода рядом или подальше от других подов по меткам и topologyKey.    | Работает через `labelSelector` и `topologyKey` (node/zone).                           |
| **Taints & Tolerations**         | Жёсткое (Node)        | Узел отталкивает поды (taint); toleration позволяет запуск.                    | Эффекты: `NoSchedule`, `PreferNoSchedule`, `NoExecute`.                               |
| **Topology Spread Constraints**  | Ограничение (Pod)     | Контроль равномерного распределения подов по topologyKey с учётом maxSkew.     | Объявляется в `spec.topologySpreadConstraints`; лучше для равномерного распределения. |

---

## 📌 Ключевые различия

- **Pod Anti-Affinity vs Taints**: Anti-Affinity — под избегает других **подов**, Taints — нода отталкивает все **поды**.
- **Pod Anti-Affinity vs Topology Spread Constraints**: Anti-Affinity определяет _можно ли_ разместить под; Spread Constraints — _насколько равномерно_ поды распределены.

---

## YAML-примеры с комментариями

### 1. nodeName

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  nodeName: kube-01 # принудительно запускаем Pod на конкретной ноде
  containers:
    - name: nginx
      image: nginx
```

---

### 2. nodeSelector

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  # Жёсткое требование: запуск только на ноде с меткой disktype=ssd
  nodeSelector:
    disktype: ssd
  containers:
    - name: nginx
      image: nginx
```

---

### 3. Node Affinity

**Kubernetes operators**

- **In** — label exists **and equals one of values**
- **NotIn** — label **not equal** to values _(or missing)_
- **Exists** — label **present** ()
- **DoesNotExist** — label **absent**
- **Gt** — label **number > value**
- **Lt** — label **number < value**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  affinity:
    nodeAffinity:
      # Жёсткое требование: только ноды в зоне europe-west1-a
      #
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
          - matchExpressions:
              - key: topology.kubernetes.io/zone
                operator: In
                values: [europe-west1-a]
      # Желательное предпочтение: ноды с GPU
      preferredDuringSchedulingIgnoredDuringExecution:
        - weight: 1
          preference:
            matchExpressions:
              - key: gpu
                operator: Exists
  containers:
    - name: nginx
      image: nginx
```

---

### 4. Pod Affinity / Anti-Affinity

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: web
  labels:
    app: web
spec:
  affinity:
    podAffinity:
      # Жёстко: запуск на той же ноде, что и под с меткой app=cache
      requiredDuringSchedulingIgnoredDuringExecution:
        - topologyKey: kubernetes.io/hostname
          labelSelector:
            matchExpressions:
              - key: app
                operator: In
                values: [cache]
    podAntiAffinity:
      # Предпочтительно: не запускать в той же зоне, где load-balancer
      preferredDuringSchedulingIgnoredDuringExecution:
        - weight: 100
          podAffinityTerm:
            topologyKey: topology.kubernetes.io/zone
            labelSelector:
              matchExpressions:
                - key: app
                  operator: In
                  values: [load-balancer]
  containers:
    - name: web
      image: nginx
```

---

### 5. Taints & Tolerations

```yaml
# На ноде применяем taint:
# "NoSchedule" — блокирует все поды без соответствующей toleration
kubectl taint nodes node1 key=value:NoSchedule

# В поде указываем toleration, чтобы он мог запускаться на такой ноде
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  tolerations:
  - key: "key"
    operator: "Equal"     # Exists - значение не важно
    value: "value"
    effect: "NoSchedule"  # должен совпадать с taint, не трогает уже запущенные поды
                          # PreferNoSchedule запуск если нет алтернативы
                          # NoExecute выселение с tolerationSeconds таймером
  containers:
  - name: nginx
    image: nginx
```

---

### 6. Topology Spread Constraints

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    app: nginx
spec:
  topologySpreadConstraints:
    - maxSkew: 1 # максимальная разница количества подов между доменами топологии
      # Пример: если в зоне A 2 пода, в зоне B 1 под, разница = 1 → допустимо
      topologyKey: topology.kubernetes.io/zone
      # Домен распределения: scheduler смотрит на лейбл ноды
      # Возможные варианты:
      #   - kubernetes.io/hostname → баланс по нодам
      #   - topology.kubernetes.io/zone → баланс по зонам
      #   - topology.kubernetes.io/region → баланс по регионам
      whenUnsatisfiable: DoNotSchedule
      # Действие, если правило не выполнено:
      #   - DoNotSchedule → Pod остаётся Pending, если нарушено maxSkew
      #   - ScheduleAnyway → Pod будет назначен, даже если баланс нарушен
      labelSelector:
        matchLabels:
          app: nginx
          # С помощью labelSelector scheduler учитывает только поды с этой меткой
          # Можно использовать:
          #   - matchLabels → простое соответствие key=value
          #   - matchExpressions → сложные условия (In, NotIn, Exists, DoesNotExist)
  containers:
    - name: nginx
      image: nginx
```

---

## 📝 Схема взаимодействия механизмов (ASCII / Markdown)

```markdown
                  +---------------------+
                  |       Node 1        |  <-- Метки: zone=us-east-1a, disktype=ssd
                  |   Taints: gpu=Yes   |      (отталкивает поды без toleration)
                  +----------+----------+
                             |
           +-----------------+-----------------+
           |                                   |
     Pod A: nginx                        Pod B: web
     nodeSelector: disktype=ssd          podAffinity: рядом с Pod C(cache)
     tolerations: нет                     podAntiAffinity: избегать Pod D(load-balancer)
     NodeAffinity: GPU предпочтительно

                  +---------------------+
                  |       Node 2        |  <-- Метки: zone=us-east-1b
                  +---------------------+
                             |
                           Pod C: cache
                           NodeAffinity: zone=us-east-1b

                  +---------------------+
                  |       Node 3        |  <-- Метки: zone=us-east-1a
                  +---------------------+
                             |
                           Pod D: load-balancer
```

**Легенда:**

- **NodeSelector / NodeAffinity** → фильтруют ноды по меткам.
- **Taints/Tolerations** → нода отталкивает поды без toleration.
- **PodAffinity / PodAntiAffinity** → поды стремятся быть рядом/подальше от других подов.
- **Topology Spread Constraints** → управляют равномерностью распределения подов по топологии.
