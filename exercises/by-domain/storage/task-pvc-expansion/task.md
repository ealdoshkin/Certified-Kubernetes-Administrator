# Task: Expand PersistentVolumeClaim

## Objective
Create a PVC, mount it in a pod, and then expand the PVC capacity.

## Requirements
- PVC name: `pv-volume`
- Storage class: `csi-hostpath-sc`
- Initial capacity: 10 Mi
- Expanded capacity: 70 Mi
- Pod name: `web-server`
- Image: `nginx`
- Mount path: `/usr/share/nginx/html`
- Access mode: ReadWriteOnce
