# Task 6: Create Persistent Volume

**Objective:** Create a persistent volume with specific parameters.

**Requirements:**
- PV name: `app-data`
- Capacity: 2Gi
- Access mode: ReadWriteMany
- Type: hostPath
- Path: `/srv/app-data`
- Storage class: `shared`
