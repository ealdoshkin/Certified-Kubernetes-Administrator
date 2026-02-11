# Task 13: Add Init Container to Existing Pod Spec

**Objective:** Add an init container to a pod spec that creates a file and validates it.

**Requirements:**
- Pod spec file: `/opt/KUCC00108/pod-spec-KUCC00108.yaml`
- Init container should create: `/workdir/calm.txt`
- Main container should check for file existence
- If file doesn't exist, pod should exit with an error
- The pod should use an `emptyDir` volume for sharing files between containers
