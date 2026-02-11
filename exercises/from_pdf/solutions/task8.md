# Solution for Task 8: List PVs Sorted by Capacity

```bash
# 1. Create directory if it doesn't exist
mkdir -p /opt/KUCC00102

# 2. List PVs sorted by capacity and save to file
kubectl get pv --sort-by='.spec.capacity.storage' > /opt/KUCC00102/volume_list

# 3. Verify the file was created and contains the expected output
cat /opt/KUCC00102/volume_list
```

This will create a file named `volume_list` in the `/opt/KUCC00102` directory containing all persistent volumes sorted by their storage capacity.
