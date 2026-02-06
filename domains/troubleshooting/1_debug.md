# Debug

Ephemeral Debug Containers:

```bash
# For troubleshooting without modifying pod spec
kubectl debug <pod-name> -it --image=busybox --target=<container-name>
```
