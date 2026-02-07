# Task: Job Basics

## Objective
Create and manage Kubernetes Jobs for one-time tasks.

## Task 1: Create Simple Job
```bash
# Create job that calculates pi
kubectl create job pi --image=perl:5.34 -- perl -Mbignum=bpi -wle 'print bpi(2000)'

# Wait for completion
kubectl wait --for=condition=complete --timeout=60s job/pi

# Get output
kubectl logs job/pi
```

## Task 2: Create Job with Command
```bash
# Create job with command
kubectl create job hello --image=busybox -- echo hello;sleep 30;echo world

# Follow logs
kubectl logs -f job/hello

# Check status
kubectl get job hello
kubectl describe job hello
```

## Task 3: Create Job with Completions
```bash
# Create job that runs 5 times sequentially
cat <<EOF | kubectl apply -f -
apiVersion: batch/v1
kind: Job
metadata:
  name: hello-completions
spec:
  completions: 5  # run 5 times
  template:
    spec:
      containers:
      - name: hello
        image: busybox
        command: ["echo", "hello world"]
      restartPolicy: OnFailure
EOF

# Check status
kubectl get job hello-completions
kubectl get pods -l job-name=hello-completions
```

## Task 4: Create Job with Parallelism
```bash
# Create job that runs 5 times in parallel
cat <<EOF | kubectl apply -f -
apiVersion: batch/v1
kind: Job
metadata:
  name: hello-parallel
spec:
  completions: 5
  parallelism: 5  # run 5 in parallel
  template:
    spec:
      containers:
      - name: hello
        image: busybox
        command: ["echo", "hello world"]
      restartPolicy: OnFailure
EOF

# Check status
kubectl get job hello-parallel
kubectl get pods -l job-name=hello-parallel
```

## Task 5: Create Job with Active Deadline
```bash
# Create job with timeout
cat <<EOF | kubectl apply -f -
apiVersion: batch/v1
kind: Job
metadata:
  name: hello-timeout
spec:
  activeDeadlineSeconds: 30  # terminate after 30 seconds
  template:
    spec:
      containers:
      - name: hello
        image: busybox
        command: ["sleep", "60"]  # will be terminated
      restartPolicy: OnFailure
EOF

# Check status (will be terminated)
kubectl get job hello-timeout
kubectl describe job hello-timeout
```

## Task 6: Delete Jobs
```bash
# Delete job (pods remain)
kubectl delete job pi

# Delete job and pods
kubectl delete job pi --cascade=orphan
```

## Key Concepts
- **Job**: Runs pods until completion
- **completions**: Number of successful completions required
- **parallelism**: Number of pods running in parallel
- **activeDeadlineSeconds**: Maximum time job can run
- **restartPolicy**: OnFailure or Never (not Always)

## Job States
- **Active**: Job is running
- **Complete**: All completions succeeded
- **Failed**: Job failed
- **Suspended**: Job is suspended

## Verification
```bash
# List jobs
kubectl get jobs

# Describe job
kubectl describe job <job-name>

# Get job pods
kubectl get pods -l job-name=<job-name>

# View logs
kubectl logs job/<job-name>
```

## Use Cases
- Database migrations
- Batch processing
- One-time tasks
- Data processing
- Backup operations
