# Backup Strategy

## Database Backup

A PostgreSQL backup script is provided in:

```
backup/backup.sh
```

Example:

```bash
./backup.sh
```

Backups are stored with timestamps.

---

## Restore Strategy

Restore using PostgreSQL:

```bash
psql
```

or

```bash
pg_restore
```

---

## Docker Volumes

Persistent data is stored inside Docker volumes.

Volumes survive container recreation.

---

## Future Improvements

- Daily Cron Jobs
- AWS S3 Backup
- Automated Snapshot Policy