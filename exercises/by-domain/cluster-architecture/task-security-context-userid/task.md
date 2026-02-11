# Task: Security Context - User ID Configuration

## Objective
Deploy a Pod with multiple containers and configure user IDs at pod and container levels.

## Requirements
- Pod name: 'user-id'
- Containers: 'sec-ctx-demo-2' and 'second-container'
- Image for 'sec-ctx-demo-2': 'gcr.io/google-samples/node-hello:1.0'
- Pod-level runAsUser: '1000'
- Container 'sec-ctx-demo-2' runAsUser: '2000' (overrides pod-level)
- Container 'sec-ctx-demo-2' should not allow privilege escalation
