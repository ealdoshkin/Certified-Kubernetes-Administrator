# Task: CronJob

## Objective
Create and manage CronJobs for scheduled tasks.

## Solution

### Create CronJob
```bash
# Create CronJob using imperative command
kubectl create cronjob hello --image=busybox --schedule="*/1 * * * *" -- date; echo Hello from the Kubernetes cluster

# Or using YAML
cat <<EOF | kubectl apply -f -
apiVersion: batch/v1
kind: CronJob
metadata:
  name: hello
spec:
  schedule: "*/1 * * * *"  # every minute
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: hello
            image: busybox
            command:
            - /bin/sh
            - -c
            - date; echo Hello from the Kubernetes cluster
          restartPolicy: OnFailure
EOF
```

## Cron Schedule Format
```
┌───────────── minute (0 - 59)
│ ┌───────────── hour (0 - 23)
│ │ ┌───────────── day of month (1 - 31)
│ │ │ ┌───────────── month (1 - 12)
│ │ │ │ ┌───────────── day of week (0 - 6) (Sunday to Saturday)
│ │ │ │ │
* * * * *
```

### Examples
- `*/1 * * * *` - Every minute
- `0 * * * *` - Every hour
- `0 0 * * *` - Every day at midnight
- `0 0 * * 0` - Every Sunday at midnight
- `0 9 * * 1-5` - Every weekday at 9 AM

## Key Concepts
- **CronJob**: Creates Jobs on a schedule
- **schedule**: Cron format schedule
- **jobTemplate**: Template for creating Jobs
- **successfulJobsHistoryLimit**: Keep N successful jobs
- **failedJobsHistoryLimit**: Keep N failed jobs

## Advanced CronJob Configuration
```yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: hello
spec:
  schedule: "*/1 * * * *"
  startingDeadlineSeconds: 10  # start job within 10 seconds of schedule
  concurrencyPolicy: Forbid  # don't run concurrent jobs
  successfulJobsHistoryLimit: 3  # keep 3 successful jobs
  failedJobsHistoryLimit: 1  # keep 1 failed job
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: hello
            image: busybox
            command: ["echo", "hello"]
          restartPolicy: OnFailure
```

## Concurrency Policies
- **Allow**: Default, allows concurrent jobs
- **Forbid**: Prevents concurrent jobs
- **Replace**: Cancels currently running job and replaces it

## Verification
```bash
# List CronJobs
kubectl get cronjobs

# Describe CronJob
kubectl describe cronjob hello

# List Jobs created by CronJob
kubectl get jobs -l app=hello

# View logs from latest job
kubectl logs -l job-name=hello-<timestamp>

# Check CronJob status
kubectl get cronjob hello -o yaml
```

## Common Use Cases
- Scheduled backups
- Database maintenance
- Report generation
- Cleanup tasks
- Health checks

## Troubleshooting
```bash
# Check CronJob status
kubectl get cronjob hello

# Check if jobs are being created
kubectl get jobs

# Check job logs
kubectl logs job/hello-<timestamp>

# Suspend CronJob
kubectl patch cronjob hello -p '{"spec":{"suspend":true}}'

# Resume CronJob
kubectl patch cronjob hello -p '{"spec":{"suspend":false}}'
```
