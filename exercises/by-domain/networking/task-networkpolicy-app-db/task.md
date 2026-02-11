# Task: NetworkPolicy - App to Database on Specific Port

## Objective

Allow ingress traffic from app namespace to db namespace pods, but only on port 3306 (MySQL).

## Requirements

- "app" namespace contains frontend pods
- "db" namespace contains database pods
- Allow ingress traffic from app pods to db pods only on port 3306
