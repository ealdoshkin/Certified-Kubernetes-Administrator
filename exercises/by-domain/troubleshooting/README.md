# Troubleshooting (30%)

Exercises covering cluster troubleshooting, node issues, logging, and debugging.

## Tasks

1. **task-sidecar-logging** - Sidecar container for logging
   - Add sidecar container to existing pod
   - Configure volume sharing
   - Set up log collection

2. **task-log-extraction** - Log monitoring and extraction
   - Monitor pod logs
   - Extract specific log lines
   - Write output to files

3. **task-node-notready** - Node troubleshooting (NotReady state)
   - Diagnose node issues
   - Fix node problems
   - Make changes permanent

4. **task-node-status-check** - Node status verification
   - Check node status
   - Filter nodes by taints
   - Count ready nodes

5. **task-pod-troubleshooting** - Troubleshoot pod issues
   - Diagnose pod failures
   - Fix pod configuration issues
   - Common pod problems

6. **task-deployment-troubleshooting** - Troubleshoot deployment issues
   - Diagnose deployment failures
   - Fix pod scheduling issues
   - Resolve scaling problems

7. **task-scheduler-failure** - Troubleshoot scheduler failure
   - Diagnose scheduler issues
   - Fix scheduler configuration
   - Restore scheduler functionality

8. **task-kubelet-failure** - Troubleshoot kubelet failure
   - Diagnose kubelet service issues
   - Fix kubelet configuration
   - Restore kubelet functionality

9. **task-kubeproxy-failure** - Troubleshoot kube-proxy failure
   - Diagnose kube-proxy pod issues
   - Fix ConfigMap problems
   - Restore service connectivity

10. **task-service-connectivity** - Troubleshoot service connectivity
    - Diagnose service access issues
    - Fix endpoint problems
    - Resolve network policy issues

11. **task-liveness-probe** - Liveness probe
    - Create liveness probes
    - Exec, HTTP, TCP probes
    - Configure probe timing

12. **task-readiness-probe** - Readiness probe
    - Create readiness probes
    - Control traffic routing
    - Combined with liveness

13. **task-pod-logs** - Pod logs
    - View pod logs
    - Follow logs
    - Log filtering

14. **task-pod-debugging** - Pod debugging
    - Debug pod errors
    - Check pod status
    - Examine events
    - Resource usage

15. **task-find-failed-probe** - Find pods with failed liveness probes
    - Search across namespaces
    - Extract error events
    - Filter by probe failures

16. **task-cpu-usage-monitoring** - Find pod with highest CPU usage
    - Monitor CPU usage
    - Sort by CPU consumption
    - Identify resource-intensive pods

## Key Concepts

- **Logging**: kubectl logs, log streaming
- **Node Troubleshooting**: kubelet issues, network problems
- **Debugging**: describe, get events, exec into pods
- **Monitoring**: Resource usage, pod status
- **Sidecar Pattern**: Additional containers for logging/monitoring

## Practice Tips

- **HIGHEST PRIORITY** - 30% of exam
- Master kubectl logs and describe commands
- Practice node troubleshooting scenarios
- Learn to read events and diagnose issues
- Understand common error patterns

## Common Troubleshooting Scenarios

- CrashLoopBackOff
- ImagePullError
- Node NotReady
- Pod scheduling failures
- Resource limits exceeded

---

**Exam Weight**: 30% - **HIGHEST PRIORITY** ⭐⭐⭐
