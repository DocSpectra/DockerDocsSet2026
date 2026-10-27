---
title: Compose file merging rules
description: Path resolution and rules for merging Compose service configurations.
---

## Merging rules 

- Paths are evaluated relative to the base file. When you use multiple Compose files, you must make sure all paths in the files are relative to the base Compose file (the first Compose file specified
with `-f`). This is required because override files need not be valid
Compose files. Override files can contain small fragments of configuration.
Tracking which fragment of a service is relative to which path is difficult and
confusing, so to keep paths easier to understand, all paths must be defined
relative to the base file.

   >[!TIP]
   >
   > You can use `docker compose config` to review your merged configuration and avoid path-related issues.

- Compose copies configurations from the original service over to the local one.
If a configuration option is defined in both the original service and the local
service, the local value replaces or extends the original value.

   - For single-value options like `image`, `command` or `mem_limit`, the new value replaces the old value.

      original service:

      ```yaml
      services:
        myservice:
          # ...
          command: python app.py
      ```

      local service:

      ```yaml
      services:
        myservice:
          # ...
          command: python otherapp.py
      ```

      result:

      ```yaml
      services:
        myservice:
          # ...
          command: python otherapp.py
      ```

   - For the multi-value options `ports`, `expose`, `external_links`, `dns`, `dns_search`, and `tmpfs`, Compose concatenates both sets of values:

      original service:

      ```yaml
      services:
        myservice:
          # ...
          expose:
            - "3000"
      ```

      local service:

      ```yaml
      services:
        myservice:
          # ...
          expose:
            - "4000"
            - "5000"
      ```

      result:

      ```yaml
      services:
        myservice:
          # ...
          expose:
            - "3000"
            - "4000"
            - "5000"
      ```

   - In the case of `environment`, `labels`, `volumes`, and `devices`, Compose "merges" entries together with locally defined values taking precedence. For `environment` and `labels`, the environment variable or label name determines which value is used:

      original service:

      ```yaml
      services:
        myservice:
          # ...
          environment:
            - FOO=original
            - BAR=original
      ```

      local service:

      ```yaml
      services:
        myservice:
          # ...
          environment:
            - BAR=local
            - BAZ=local
      ```

     result:

      ```yaml
      services:
        myservice:
          # ...
          environment:
            - FOO=original
            - BAR=local
            - BAZ=local
      ```

   - Entries for `volumes` and `devices` are merged using the mount path in the container:

      original service:

      ```yaml
      services:
        myservice:
          # ...
          volumes:
            - ./original:/foo
            - ./original:/bar
      ```

      local service:

      ```yaml
      services:
        myservice:
          # ...
          volumes:
            - ./local:/bar
            - ./local:/baz
      ```

      result:

      ```yaml
      services:
        myservice:
          # ...
          volumes:
            - ./original:/foo
            - ./local:/bar
            - ./local:/baz
      ```

For more merging rules, see [Merge and override](/reference/compose-file/merge.md) in the Compose Specification. 


## Limitations

Docker Compose supports relative paths for the many resources to be included in the application model: build context for service images, location of file defining environment variables, path to a local directory used in a bind-mounted volume.
With such a constraint, code organization in a monorepo can become hard as a natural choice would be to have dedicated folders per team or component, but then the Compose files relative paths become irrelevant.
