# Task: NetworkPolicy - Restrict Database Access to Admin Pod

## Objective
Restrict all inbound traffic to database pods except from a specific admin pod.

## Requirements
- Namespace: "data"
- Database pods running in "data" namespace
- Restrict all inbound traffic except from pod named "admin"
