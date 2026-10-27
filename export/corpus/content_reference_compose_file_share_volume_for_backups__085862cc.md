---
title: Share a database volume with a backup service
description: Use a named volume across database and backup services.
---

## Volume configuration and caveats

See [volume declarations](volumes.md), [service mounts and path caveats](services.md#volumes), and [persistent volume context](/manuals/engine/storage/volumes.md).

## Example

The following example shows a two-service setup where a database's data directory is shared with another service as a volume, named
`db-data`, so that it can be periodically backed up.

```yml
services:
  backend:
    image: example/database
    volumes:
      - db-data:/etc/data

  backup:
    image: backup-service
    volumes:
      - db-data:/var/lib/backup/data

volumes:
  db-data:
```

The `db-data` volume is mounted at the `/var/lib/backup/data` and `/etc/data` container paths for backup and backend respectively.

Running `docker compose up` creates the volume if it doesn't already exist. Otherwise, the existing volume is used and is recreated if it's manually deleted outside of Compose.

