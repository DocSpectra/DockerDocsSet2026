---
title: Using lifecycle hooks with Compose
linkTitle: Use lifecycle hooks
weight: 20
description: Learn how to use Docker Compose lifecycle hooks like post_start and pre_stop to customize container behavior.
keywords: docker compose lifecycle hooks, post_start, pre_stop, docker compose entrypoint, docker container stop hooks, compose hook commands
---

{{< summary-bar feature_name="Compose lifecycle hooks" >}}

## Services lifecycle hooks

See [Compose lifecycle hook behavior](../intro/lifecycle-hooks.md) for hook privileges, timing, and stop exceptions.

### Post-start hooks

See [Post-start timing](../intro/lifecycle-hooks.md#post-start-hooks).

In the example provided:

- The hook is used to change the ownership of a volume to a non-root user (because volumes 
are created with root ownership by default).
- After the container starts, the `chown` command changes the ownership of the `/data` directory to user `1001`.

```yaml
services:
  app:
    image: backend
    user: 1001
    volumes:
      - data:/data    
    post_start:
      - command: chown -R 1001:1001 /data
        user: root

volumes:
  data: {} # a Docker volume is created with root ownership
```

### Pre-stop hooks

See [Pre-stop timing and exceptions](../intro/lifecycle-hooks.md#pre-stop-hooks).

In the following example, before the container stops, the `./data_flush.sh` script is 
run to perform any necessary cleanup.

```yaml
services:
  app:
    image: backend
    pre_stop:
      - command: ./data_flush.sh
```

## Reference information

- [`post_start`](/reference/compose-file/services.md#post_start)
- [`pre_stop`](/reference/compose-file/services.md#pre_stop)
