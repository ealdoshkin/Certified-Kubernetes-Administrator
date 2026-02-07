# CKA commands and files

## This repository contains various commands to work with kubernetes

## RBAC

- Check if user has permissions
```sh
kubectl auth can-i create deployments --as dev-user
```

- Kubeapi server authorization flag has modes of roles available for cluster

- ResourceNames are specific names like names of pods,deployments etc

- Check on of clusteroles or bindings in cluster
```sh
kubectl get clusterrolebindings --no-headers | wc -l
```

## QUestions and Solutions

- Solution in pinku-user.yaml
```
You have been assigned the task of setting up Role-Based Access Control (RBAC) for the user 'pinku' within the 'argo' namespace of your Kubernetes cluster. The user 'pinku' requires specific access rights to manage resources within this namespace.

Create a Role named 'pinku-role' in the 'argo' namespace with the following permissions:

API groups: [""], ["apps"], ["extensions"]
Resources: ["pods"], ["deployments"], ["services"], ["ingress"]
Verbs: ["get"], ["watch"], ["list"]
Bind the Role 'pinku-role' to the user 'pinku' within the 'argo' namespace using a RoleBinding named 'pinku-role-binding'.

```

- Solution using imperative commands

<details><summary>show</summary>
<p>

```bash
# Step 1: Create the 'pinku-role' Role in the 'argo' namespace
kubectl create role pinku-role --namespace=argo \
  --verb=get,watch,list \
  --resource=pods,deployments,services,ingress

# Step 2: Bind the 'pinku-role' Role to the 'pinku' user within the 'argo' namespace using RoleBinding
kubectl create rolebinding pinku-role-binding --namespace=argo \
  --role=pinku-role \
  --user=pinku

# Step 3: Test if access is working fine
kubectl auth can-i get pods --namespace argo --as pinku
kubectl auth can-i list services --namespace argo --as pinku
kubectl auth can-i watch deployments --namespace argo --as pinku
kubectl auth can-i create ingress --namespace argo --as pinku
```
