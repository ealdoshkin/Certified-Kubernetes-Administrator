# Task: etcd Snapshot with TLS Certificates

## Objective
Create an etcd snapshot using TLS certificates for authentication.

## Requirements
- etcd endpoint: `https://127.0.0.1:2379`
- Snapshot path: `/srv/data/etcd-snapshot.db`
- CA certificate: `/opt/KUCM00302/ca.crt`
- Client certificate: `/opt/KUCM00302/etcd-client.crt`
- Client key: `/opt/KUCM00302/etcd-client.key`

## Solution

### Create etcd Snapshot with TLS
```bash
ETCDCTL_API=3 etcdctl snapshot save /srv/data/etcd-snapshot.db \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/opt/KUCM00302/ca.crt \
  --cert=/opt/KUCM00302/etcd-client.crt \
  --key=/opt/KUCM00302/etcd-client.key
```

## Key Concepts
- **etcdctl**: Command-line tool for etcd
- **ETCDCTL_API=3**: Use etcd API v3
- **TLS Certificates**: Required for secure etcd access
- **Snapshot**: Backup of etcd data

## etcd Snapshot Commands

### Create Snapshot
```bash
ETCDCTL_API=3 etcdctl snapshot save <snapshot-file> \
  --endpoints=<etcd-endpoint> \
  --cacert=<ca-cert> \
  --cert=<client-cert> \
  --key=<client-key>
```

### View Snapshot Status
```bash
ETCDCTL_API=3 etcdctl snapshot status /srv/data/etcd-snapshot.db
```

### Restore from Snapshot
```bash
ETCDCTL_API=3 etcdctl snapshot restore /srv/data/etcd-snapshot.db \
  --data-dir=/var/lib/etcd-backup
```

## Verification
```bash
# Check snapshot file exists
ls -lh /srv/data/etcd-snapshot.db

# Check snapshot status
ETCDCTL_API=3 etcdctl snapshot status /srv/data/etcd-snapshot.db

# Verify certificates exist
ls -la /opt/KUCM00302/
```

## Important Notes
- Must use ETCDCTL_API=3 for etcd v3
- Certificates must be valid and accessible
- Snapshot includes all etcd data
- Snapshot is cluster state backup

## Common Issues
- Certificate path errors
- Permission denied
- etcd not accessible
- Wrong API version
