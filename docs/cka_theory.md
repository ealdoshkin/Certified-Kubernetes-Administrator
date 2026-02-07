# CKA. Theory

kube-sheduler - отслеживает новые поды, и назначает их на ноды с учетом ресурсов и политик
kube-controller-manager - набор служебных тасок (котроль состояния кластера, создание сущностей в кластере JOB, SA)
kubelet - запуск подов
kube-proxy - опциональный процесс настройки сети
CNI
CRI
DNS

Механизм работы с логами kube logs

POD - минимальная исполняемая среда в кластере (набор контейнеров)
ReplicaSet - запуск реплик пода, Deployment реплика сэт с выкаткой
StatefulSet - static names (pods, storage)


## Load Balance

- Cloud Provider
- HAProxy+keepalived (стандарт)
- Nginx (сложно в настройке)
- KubeVIP/Metalb (декларировано в кластере)


## Limits

- No more than 110 pods per node
- No more than 5,000 nodes
- No more than 150,000 total pods
- No more than 300,000 total containers



targetPort - порт пода


## Packages

 Metrics server - взаимодействует с kubelet на предмет состояния подов
 Kube-state-metrics - опрашивает Api и состояние объектов в кластере
