# RBAC

## Основные ресурсы RBAC

- Role
- ClusterRole
- RoleBinding
- ClusterRoleBinding

**Verbs:** get, list, watch, create, update, patch, delete, deletecollection, bind, escalate, impersonate
**Resources**: **ns**: pods, pods/exec, deployments, services, configmaps, secrets, **cluster**: namespaces, nodes, pv, crd, sc

## Traps

- **RoleBinding может работать с Role или ClusterRole** в пределах ns
- (aka sudo) Чтобы создавать Role|RoleBinding с повышенными правами нужны: bind, escalate. Создаем себе ClusterRole.
- Используем Group: system:authenticated - группа чтобы дать всем user и sa права.

## Встроенные (Basic) ClusterRole

| ClusterRole Name          | Purpose                                                               |
| ------------------------- | --------------------------------------------------------------------- |
| cluster-admin             | Super-user access (full control over all resources in the cluster)    |
| admin                     | Admin access within a namespace (most resources, except RBAC)         |
| edit                      | Allows read/write access to most resources in a namespace             |
| view                      | Read-only access to most resources in a namespace                     |
| system:auth-delegator     | Used for delegated authentication/authorization checks                |
| system:basic-user         | Minimal access for authenticated users (e.g., discover API endpoints) |
| system:discovery          | Access to API discovery endpoints                                     |
| system:public-info-viewer | Read access to non-sensitive cluster info (e.g., nodes, namespaces)   |
| system:node               | Access for kubelets (node management)                                 |

Удобно посмотреть:
```sh
 k describe clusterrole cluster-admin
```

## User vs ServiceAccount

- User создается с помощью сертификата (не хранится в кластере) или OIDC
- User из сертификата: `"/CN=jane/O=developers"`
- `--resource-name=readablepod` — правило применяется только к указанному ресурсу

## Команды

**Просмотр текущего kubeconfig:**

```bash
kubectl config view
```

**Посмотреть кто я есть:**

```bash
k auth whoami
```

Посмотреть все права пользователя:

```sh
kubectl auth can-i --list --as=system:serviceaccount:admin-tools:kubectl-view-sa

```

**Проверить действие от пользователя:**

```bash
# Помним про impersonate
kubectl auth can-i get pods --as=serviceaccount:default:my-sa
```

**Создать ServiceAccount:**

```bash
k create serviceaccount my-sa -oyaml --dry-run=client
```

**Создать Role:**

```bash
k create role pod-read --verb=get,list,watch --resource=pods -oyaml --dry-run=client
```

**Роль на все ресурсы и все действия:**

```bash
k create role namespace-admin --verb="*" --resource="*" --dry-run=client -oyaml
```

**Создать RoleBinding:**

```bash
k create rolebinding my-sa-pod-read --role=pod-read --serviceaccount=default:my-sa -oyaml --dry-run=client
```

Найти aggregation ClusterRole (агреггированные правила):

```sh
kubectl get clusterrole -l rbac.authorization.k8s.io/aggregate-to-view=true
```

Могу ли я проверять и представляться правами других пользователей:

```sh
kubectl auth can-i impersonate users

```

## Использование ServiceAccount

### В кластере (curl)

Pod, использующий curl для вызова Kubernetes API:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: api-client-pod
spec:
  serviceAccountName: api-access-sa
  containers:
    - name: curl-client
      image: curlimages/curl:latest
      command: ["sh", "-c"]
      args:
        - |
          TOKEN=$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)
          CACERT=/var/run/secrets/kubernetes.io/serviceaccount/ca.crt

          # Call Kubernetes API
          while true; do
            echo "=== Getting nodes ==="
            curl -s -H "Authorization: Bearer $TOKEN" \
              --cacert $CACERT \
              https://kubernetes.default.svc/api/v1/nodes

            sleep 60
          done
```

### Вне кластера (kubectl)

**Сгенерировать токен:**

```bash
TOKEN=$(kubectl create token -n admin-tools kubectl-view-sa)
```

**Быстрая проверка:**

```bash
k get pods -A --token $TOKEN --server https://192.168.122.234:8443 --insecure-skip-tls-verify=true
```

**Создать kubeconfig:**

```bash

# Create cluster
kubectl config set-cluster my-cluster \
  --server=https://192.168.122.234:8443 \
  --certificate-authority=/mnt/data/vm/minikube/.minikube/ca.crt \
  --embed-certs=true \
  --kubeconfig=kubeconfig

# Create user
kubectl config set-credentials kubectl-view-sa --token=$TOKEN --kubeconfig=kubeconfig

# Create context
kubectl config set-context view-context \
  --cluster=my-cluster \
  --user=kubectl-view-sa \
  --namespace=admin-tools --kubeconfig=kubeconfig

# Set default context
kubectl config use-context view-context --kubeconfig=kubeconfig
```

Не монтировать SA в под:
```yaml
automountServiceAccountToken: false
```

## Kubeconfig

Указать контекст можно через kubectl:

```sh
kubectl --context
```

Работа с kubeconfig:

```sh
k config get-contexts
k config set-context minikube --user=minikube --namespace=default
k config use-context minikube
```
