# Kustomize

## Основные команды

```bash
kubectl apply -k <dir>          # Применить конфигурацию
kubectl kustomize <dir>         # Просмотр итогового YAML
kubectl diff -k <dir>           # Показать изменения
kustomize create --autodetect   # Создать kustomization.yaml
kubectl get -k ./overlays/dev   # Посмотреть созданные ресурсы
kustomize edit fix              # Исправить устаревший синтаксис
```

## Ключевые темы экзамена

### 1. Базовая структура

```
app/
├── base/                    # Общие манифесты
│   ├── kustomization.yaml
│   ├── deployment.yaml
│   └── service.yaml
└── overlays/
    └── prod/               # Окружение
        ├── kustomization.yaml
        └── patches/
```

### 2. Важные концепции

- **Селекторы Deployment неизменяемы** - не изменяйте через `commonLabels`
- **Патчи**: используйте `patches:`, а не устаревший `patchesStrategicMerge:`
- **Генераторы**: `configMapGenerator`/`secretGenerator` добавляют хэш к именам для автоперезапуска

### 3. Безопасное добавление меток

```yaml
# patch.yaml (ДЛЯ Deployment)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
spec:
  template:
    metadata:
      labels:
        env: prod # Добавлять ТОЛЬКО здесь
```

### 4. Пример kustomization.yaml

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - ../../base
patches:
  - path: patch.yaml
commonLabels:
  env: prod
configMapGenerator:
  - name: app-config
    literals: [LOG_LEVEL=INFO]
```

## Что проверяют

1. Создать base + overlay
2. Пропатчить Deployment (реплики/образ)
3. Добавить метки без изменения selector
4. Сгенерировать ConfigMap/Secret
5. Отладить через `kubectl kustomize`
