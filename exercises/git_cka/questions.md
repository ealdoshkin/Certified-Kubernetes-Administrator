## Questions (Tasks)

### Question 1: Schedule Pod on Master Node

Create a Pod `pod1` in `default` using image `httpd:2.4.41-alpine`.

- Container name: `pod1-container`
- Pod must **only** run on a master node (do not add new labels).
- Write to `/opt/course/2/master_schedule_reason` why Pods are not scheduled on masters by default.

### Question 2: Storage with PV, PVC, Deployment

- PV `safari-pv`: capacity 2Gi, `ReadWriteOnce`, `hostPath: /Volumes/Data`, no storageClass.
- PVC `safari-pvc` in `project-tiger`: request 2Gi, `ReadWriteOnce`, no storageClass.
- Deployment `safari` in `project-tiger` running `httpd:2.4.41-alpine` mounting at `/tmp/safari-data`.

### Question 3: RBAC with ServiceAccount, Role, RoleBinding

Create ServiceAccount `processor` in `project-hamster`. Create Role/RoleBinding (both named `processor`) to allow **only** `create` on **Secrets** and **ConfigMaps** in that namespace.

### Question 4: DaemonSet on All Nodes

Namespace: `project-tiger`. Create DaemonSet `ds-important` (image `httpd:2.4-alpine`), labels `id=ds-important`, `uuid=18426a0b-5f59-4e10-923f-c0e078e82462`. Requests: `cpu:10m`, `memory:10Mi`. Must run on **all nodes including masters**.

### Question 5: Deployment with Anti-Affinity or Spread Constraints

Namespace `project-tiger`. Create Deployment `deploy-important` with label `id=very-important`, replicas=3.
Two containers per Pod:

- `container1`: `nginx:1.17.6-alpine`
- `container2`: `kubernetes/pause`
  Ensure **max one Pod per worker node**; with 2 workers, only 2 Pods run, 1 Pending.

### Question 6: Multi-Container Pod with Shared Volume

Create Pod `multi-container-playground` in `default` with three containers: `c1`, `c2`, `c3` and a shared, **non-persistent** volume.

- `c1`: `nginx:1.17.6-alpine`, env `MY_NODE_NAME` = node name.
- `c2`: `busybox:1.31.1`, write `date` every second to `/vol/date.log`.
- `c3`: `busybox:1.31.1`, `tail -f /vol/date.log`.
  Confirm logs in `c3`.

### Question 7: Secrets: Mount + Env Vars

- Create namespace `secret`.
- There is an existing Secret manifest at `/opt/course/19/secret1.yaml` → create it in `secret` and mount read-only at `/tmp/secret1`.
- Create Secret `secret2` in `secret` with `user=user1`, `pass=1234`. Inject as env `APP_USER` and `APP_PASS` in a long-running `busybox:1.31.1` Pod named `secret-pod` that can run on masters (add toleration). Verify.

### Question 8: Upgrade Node and Join Cluster

A node (`cluster3-worker2`) is not part of the cluster and runs an older Kubernetes. Upgrade it to the **exact** version running on `cluster3-master1` and **join** it to the cluster using `kubeadm`.

### Question 9: NetworkPolicy with Egress Control

Namespace `project-snake`. Create NetworkPolicy `np-backend` to allow **only**:

- backend-_ Pods → db1-_ Pods on port **1111**
- backend-_ Pods → db2-_ Pods on port **2222**
  Afterwards, backend → vault on 3333 must be **blocked**. Selector uses label `app`.

### Question 10: Etcd Backup and Restore

- Take an etcd **snapshot** on `cluster3-master1` to `/tmp/etcd-backup.db`.
- Create any test Pod.
- Restore the snapshot and verify the test Pod is gone (state rolled back).
