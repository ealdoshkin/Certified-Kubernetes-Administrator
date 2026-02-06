# Liveness and Readiness probe

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: probe-demo
  labels:
    app: probe-demo
spec:
  containers:
    - name: demo-app
      image: busybox
      command: ["sh", "-c", "sleep 3600"] # Контейнер просто "живет" для демонстрации
      # ------------------- Startup Probe -------------------
      startupProbe:
        # Проверка, что контейнер полностью стартовал (например, создал файл /app/started.txt)
        exec:
          command: ["cat", "/app/started.txt"]
        # Кол-во последовательных неудач перед тем как контейнер будет перезапущен
        failureThreshold: 30
        # Интервал между проверками (секунды)
        periodSeconds: 10
        # StartupProbe игнорирует LivenessProbe до успешного прохождения
        initialDelaySeconds: 0
      # ------------------- Liveness Probe -------------------
      livenessProbe:
        # Проверка, "жив" ли контейнер (например, отвечает ли HTTP /healthz)
        httpGet:
          path: /healthz
          port: 8080
        # Ждём перед первой проверкой, чтобы контейнер успел стартовать
        initialDelaySeconds: 10
        # Интервал между проверками
        periodSeconds: 5
        # Кол-во неудач подряд, после которых контейнер будет перезапущен
        failureThreshold: 3
      # ------------------- Readiness Probe -------------------
      readinessProbe:
        # Проверка готовности контейнера принимать трафик (TCP / порт)
        tcpSocket:
          port: 8080
        initialDelaySeconds: 5
        periodSeconds: 5
        failureThreshold: 3
        # Если превысит threshold:
        # - Pod помечается NotReady
        # - Трафик через Service не идет к контейнеру
        # - Контейнер НЕ перезапускается
        # ------------------- Ресурсы -------------------
      # ------------------- Volume Mounts -------------------
      volumeMounts:
        - name: work-dir
          mountPath: /app # Используется startupProbe для проверки наличия файла
  # ------------------- Volumes -------------------
  volumes:
    - name: work-dir
      emptyDir: {} # Эфемерный общий том, доступный контейнеру для проверки и обмена файлами
```
