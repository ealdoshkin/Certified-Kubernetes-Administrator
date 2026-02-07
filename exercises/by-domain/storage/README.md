# Storage Domain Exercises (10%)

Storage-related exercises covering Persistent Volumes, Persistent Volume Claims, and storage classes.

## Tasks

1. **task-pvc-mount-patch** - PVC creation, mounting to pod, and capacity patching
   - Create PVC with storage class
   - Mount PVC to pod
   - Patch PVC capacity

2. **task-pv-hostpath** - Persistent Volume with hostPath (2Gi, ReadWriteOnce)
   - Create PV with hostPath type
   - Configure access mode and capacity

3. **task-pv-hostpath-large** - Persistent Volume with hostPath (10Gi, ReadWriteOnce)
   - Create larger PV with hostPath type
   - Configure access mode and capacity

4. **task-emptydir-volume** - emptyDir volume
   - Create emptyDir volume
   - Multi-container volume sharing
   - Temporary storage

5. **task-pv-pvc-basic** - PV and PVC basics
   - Create PersistentVolume
   - Create PersistentVolumeClaim
   - Bind and mount in pod

6. **task-pvc-expansion** - Expand PersistentVolumeClaim
   - Create PVC with initial size
   - Expand PVC capacity
   - Patch or edit PVC

## Key Concepts

- **PersistentVolume (PV)**: Cluster-level storage resource
- **PersistentVolumeClaim (PVC)**: User's request for storage
- **StorageClass**: Defines storage provisioning
- **Access Modes**: ReadWriteOnce, ReadOnlyMany, ReadWriteMany
- **Volume Types**: hostPath, emptyDir, NFS, CSI

## Practice Tips

- Understand the difference between PV and PVC
- Know when to use different access modes
- Practice patching PVC capacity
- Learn storage class configuration

---

**Exam Weight**: 10% - Smallest domain but still important
