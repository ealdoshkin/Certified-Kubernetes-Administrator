# Workloads & Scheduling (15%)

Exercises covering deployments, pods, scheduling, and workload management.

## Tasks

1. **task-pod-cpu-monitoring** - Pod CPU usage monitoring
   - Monitor pod CPU usage
   - Find high CPU consuming pods
   - Extract metrics

2. **task-pod-node-selector** - Pod scheduling with node selector
   - Schedule pod on specific node
   - Use node selectors

3. **task-deployment-rollback** - Deployment rollback operations
   - Create deployment
   - Perform rolling update
   - Rollback to previous version

4. **task-deployment-scale** - Deployment scaling
   - Scale deployment up/down
   - Manage replicas

5. **task-deployment-mixed** - Mixed deployment operations
   - Scaling deployments
   - Pod creation
   - CPU monitoring

6. **task-multi-container-pod** - Multi-container pod creation
   - Create pod with multiple containers
   - Configure container images

7. **task-node-drain** - Node drain and pod rescheduling
   - Drain node
   - Reschedule pods
   - Make node unavailable

8. **task-pod-namespace** - Pod creation in namespace
   - Create namespace
   - Create pod in namespace

9. **task-configmap** - Create and use ConfigMaps
   - Create ConfigMap with single/multi-line values
   - Mount ConfigMap as volume
   - Use ConfigMap as environment variables

10. **task-secret** - Create secrets
    - Create secrets with base64 encoded values
    - Use secrets in deployments

11. **task-node-affinity** - Pod scheduling with node affinity
    - Configure required node affinity
    - Configure preferred node affinity
    - Use weight for preferred affinity

12. **task-secret-mysql** - Secret for MySQL deployment
    - Create secret with username/password
    - Use secret in MySQL deployment
    - Environment variables from secret

13. **task-secret-web-app** - Multi-container pod with secrets
    - Secret as environment variables
    - Secret as volume mounts
    - Multi-container pod configuration

14. **task-secret-update** - Update existing secret
    - Update secret values
    - Propagate changes to pods
    - Volume mounts vs environment variables

15. **task-configmap-basic** - ConfigMap basics
    - Create from literals, files, env files
    - Display ConfigMap values
    - Custom keys

16. **task-configmap-env** - ConfigMap as environment variables
    - Single key as env var
    - All keys as env vars
    - envFrom configuration

17. **task-configmap-volume** - Mount ConfigMap as volume
    - ConfigMap volume mount
    - Access ConfigMap as files
    - Multi-container volume sharing

18. **task-deployment-rollout** - Deployment rollout management
    - Create and update deployments
    - View rollout status
    - Pause and resume rollouts

19. **task-deployment-rollback** - Deployment rollback
    - Rollback to previous version
    - Rollback to specific revision
    - Handle failed rollouts

20. **task-hpa** - Horizontal Pod Autoscaler
    - Create HPA
    - Configure autoscaling
    - Monitor scaling behavior

21. **task-job-basic** - Job basics
    - Create simple jobs
    - Jobs with completions
    - Jobs with parallelism
    - Job timeouts

22. **task-cronjob** - CronJob
    - Create scheduled jobs
    - Cron schedule format
    - Concurrency policies

23. **task-node-affinity** - Node affinity
    - nodeSelector
    - Required node affinity
    - Preferred node affinity

24. **task-taints-tolerations** - Taints and tolerations
    - Taint nodes
    - Create pods with tolerations
    - Control plane tolerations

25. **task-resource-requests-limits** - Resource requests and limits
    - Configure CPU and memory
    - Requests vs limits
    - Resource units

26. **task-resourcequota** - Resource quota
    - Create ResourceQuota
    - Limit namespace resources
    - Enforce resource limits

27. **task-init-container** - Init containers
    - Add init container to pod
    - Setup tasks before main container
    - Shared volumes with init containers

28. **task-daemonset** - DaemonSet
    - Create DaemonSet
    - Ensure one pod per node
    - Respect node taints

29. **task-custom-columns** - Custom columns output
    - Format kubectl output
    - Use custom-columns
    - JSONPath expressions

30. **task-sort-resources** - Sort resources
    - Sort pods by name
    - Sort PVs by capacity
    - Use --sort-by flag

31. **task-pod-ip-extraction** - Extract pod IP
    - Get pod IP address
    - Use JSONPath
    - Multiple extraction methods

32. **task-service-endpoints** - List pods implementing service
    - Find pods behind service
    - Use service selectors
    - Extract from endpoints

## Key Concepts

- **Deployments**: Manage ReplicaSets and rolling updates
- **Pods**: Basic workload unit
- **Scheduling**: Node selectors, affinity, taints/tolerations
- **Scaling**: Horizontal and vertical scaling
- **Rollbacks**: Reverting to previous deployment version

## Practice Tips

- Master deployment operations (very common)
- Understand pod scheduling mechanisms
- Practice scaling operations
- Know how to perform rollbacks

---

**Exam Weight**: 15% - Core workload concepts
