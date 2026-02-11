# Task: etcd Snapshot with TLS Certificates

## Objective
Create an etcd snapshot using TLS certificates for authentication.

## Requirements
- etcd endpoint: `https://127.0.0.1:2379`
- Snapshot path: `/srv/data/etcd-snapshot.db`
- CA certificate: `/opt/KUCM00302/ca.crt`
- Client certificate: `/opt/KUCM00302/etcd-client.crt`
- Client key: `/opt/KUCM00302/etcd-client.key`
