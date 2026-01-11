Below is a **structured, practical CKA preparation track** built as **hands-on tasks**, not theory.
Each task mirrors **real exam objectives**, increases in difficulty, and is meant to be done **step-by-step in a terminal** (bash, exam-safe).

Assumptions (aligned with CKA exam):

* You use **bash**
* `kubectl` is available
* Alias `k=kubectl`
* No internet access during tasks
* Speed and accuracy matter more than elegance

---

## PHASE 1 — Core Speed & Muscle Memory (Mandatory)

### Task 1.1 — Fast Pod Creation (Imperative)

**Goal:** Create and verify a running Pod in under **30 seconds**.

Steps:

1. Create a Pod named `nginx-pod` using image `nginx:1.25`
2. Ensure it runs in namespace `default`
3. Verify it is `Running`

Expected commands:

* `kubectl run`
* `kubectl get pod`
* `kubectl describe pod`

Checkpoint:

* Pod status = Running
* No YAML files used

---

### Task 1.2 — YAML Generation Without Editors

**Goal:** Generate clean YAML fast.

Steps:

1. Generate YAML for a Pod named `busybox-pod` (image `busybox`)
2. Command should sleep for 3600 seconds
3. Save YAML to `busybox.yaml`
4. Create the Pod from the file

Constraints:

* No manual typing of YAML
* Use `--dry-run=client -o yaml`

---

### Task 1.3 — Edit Live Object Safely

**Goal:** Modify a running Pod.

Steps:

1. Edit `busybox-pod`
2. Change sleep time to `7200`
3. Save and exit editor
4. Verify the change is applied

Exam focus:

* `kubectl edit`
* vi key usage
* Object recreation awareness

---

## PHASE 2 — Workloads (High Weight)

### Task 2.1 — Deployment Creation

**Goal:** Create a Deployment correctly the first time.

Steps:

1. Create a Deployment named `web`
2. Image: `nginx:1.25`
3. Replicas: 3
4. Namespace: `apps`
5. Verify all Pods are running

Hidden skills tested:

* Namespace creation
* Deployment rollout
* ReplicaSet behavior

---

### Task 2.2 — Scale Under Pressure

**Goal:** Modify replicas fast.

Steps:

1. Scale Deployment `web` to 5 replicas
2. Confirm scaling
3. Identify ReplicaSet name

---

### Task 2.3 — Rolling Update + Rollback

**Goal:** Demonstrate rollout control.

Steps:

1. Update image to `nginx:1.26`
2. Watch rollout status
3. Roll back to previous version
4. Confirm Pods use old image

Commands tested:

* `kubectl set image`
* `kubectl rollout status`
* `kubectl rollout undo`

---

## PHASE 3 — Services & Networking

### Task 3.1 — ClusterIP Service

**Goal:** Expose Pods internally.

Steps:

1. Expose Deployment `web`
2. Service name: `web-svc`
3. Port: 80 → TargetPort: 80
4. Verify Service and Endpoints

---

### Task 3.2 — NodePort Service

**Goal:** External access.

Steps:

1. Create a NodePort Service for `web`
2. NodePort: `30080`
3. Verify Service mapping

Exam trick:

* Verify endpoints, not just Service existence

---

### Task 3.3 — DNS Resolution Test

**Goal:** Validate Service discovery.

Steps:

1. Run a temporary Pod using `busybox`
2. Test DNS resolution of `web-svc`
3. Exit and delete the Pod

---

## PHASE 4 — Storage (Common Failure Area)

### Task 4.1 — PersistentVolume

**Goal:** Static provisioning.

Steps:

1. Create a PV:

   * Name: `pv-data`
   * Capacity: 1Gi
   * AccessMode: ReadWriteOnce
   * HostPath: `/data/pv`
2. Verify PV is Available

---

### Task 4.2 — PersistentVolumeClaim

**Goal:** Correct binding.

Steps:

1. Create a PVC:

   * Name: `pvc-data`
   * Request: 1Gi
   * AccessMode: ReadWriteOnce
2. Verify PVC is Bound

---

### Task 4.3 — Pod Using PVC

**Goal:** Mount storage correctly.

Steps:

1. Create a Pod using `busybox`
2. Mount PVC at `/mnt/data`
3. Write a file into the volume
4. Verify file exists

---

## PHASE 5 — Configuration (ConfigMaps & Secrets)

### Task 5.1 — ConfigMap From Literal

**Goal:** Fast config injection.

Steps:

1. Create ConfigMap `app-config`
2. Key: `APP_ENV=prod`
3. Mount into Pod as env var
4. Verify inside container

---

### Task 5.2 — Secret Creation

**Goal:** Correct encoding handling.

Steps:

1. Create Secret `db-secret`
2. Key: `password=admin123`
3. Inject as env var
4. Verify value inside Pod

---

## PHASE 6 — Troubleshooting (High Value)

### Task 6.1 — CrashLoopBackOff

**Goal:** Diagnose quickly.

Steps:

1. Create a Pod that exits immediately
2. Observe status
3. Identify failure reason
4. Fix command
5. Pod becomes Running

Tools:

* `kubectl logs`
* `kubectl describe`

---

### Task 6.2 — ImagePullBackOff

**Goal:** Identify image issues.

Steps:

1. Deploy Pod with invalid image
2. Detect failure
3. Fix image
4. Confirm successful pull

---

## PHASE 7 — Node & Scheduling

### Task 7.1 — Node Labeling

**Goal:** Control scheduling.

Steps:

1. Label a node `disk=ssd`
2. Create Pod that runs only on that node
3. Verify scheduling

---

### Task 7.2 — Taints & Tolerations

**Goal:** Advanced scheduling.

Steps:

1. Taint a node
2. Pod fails to schedule
3. Add toleration
4. Pod schedules successfully
