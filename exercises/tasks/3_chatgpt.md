# Emulate

## Section 1: Core Objects (25%)

1. Create a Pod `web` using image `nginx`, expose port 80.
2. Add environment variable `ENV=prod` to the Pod.
3. Verify the environment variable from inside the container.
4. Create the same Pod in namespace `dev`.

---

## Section 2: Workloads & Updates (20%)

5. Create a Deployment `api-server`:

   - image: `nginx:1.20`
   - replicas: 3

6. Update the Deployment image to `nginx:1.21`.
7. Roll back the Deployment to the previous version.
8. Confirm the rollout history.

---

## Section 3: Scheduling (10%)

9. Label a node with `disk=ssd`.
10. Create a Pod that schedules only on nodes with `disk=ssd`.
11. Taint a node and observe scheduling failure.
12. Add toleration so the Pod schedules successfully.

---

## Section 4: Storage (20%)

13. Create a PersistentVolume:

- name: `data-pv`
- capacity: `2Gi`
- accessMode: `ReadWriteMany`
- hostPath: `/srv/data`

14. Create a PVC that binds to `data-pv`.
15. Create a Pod that mounts the PVC at `/var/data`.
16. Verify the PV status changes to `Bound`.

---

## Section 5: Troubleshooting (15%)

17. Create a Pod that exits immediately.
18. Diagnose why the Pod is failing.
19. Fix the Pod so it reaches `Running`.
20. Use logs and describe appropriately.



---

## Section 6: Logging & Output (10%)

21. Extract logs from Pod `frontend`.
22. Filter logs for the word `started`.
23. Save the output to `/opt/error-logs`.

---

## Section 7: Inspection & Formatting (Bonus / Speed)

24. List all Pods with:

- name
- namespace
  using `jsonpath`.

25. List Pods using custom columns.
26. List all PersistentVolumes sorted by capacity and save output to:
    `/opt/volume_list`.
