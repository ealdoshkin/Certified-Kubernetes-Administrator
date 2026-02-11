# Task: Security Context - Linux Capabilities

## Objective
Deploy a Pod with security context that grants specific Linux capabilities.

## Requirements
- Pod name: 'user-id'
- Container name: 'sec-ctx-demo-2'
- Image: 'gcr.io/google-samples/node-hello:1.0'
- Run container with user ID '1000'
- Grant capabilities for:
  - Manipulating system time (SYS_TIME)
  - Network administration (NET_ADMIN)
