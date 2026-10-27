---
title: Load environment variables into a service
description: Use env_file and environment to configure container variables.
---

## Environment rules and caveats

See [environment file syntax, path resolution, and precedence](services.md#env_file), [environment entries and quoting](services.md#environment), and [Compose interpolation](interpolation.md).

## Use an environment file

```yml
env_file: .env
```

Relative paths are resolved from the Compose file's parent folder. As absolute paths prevent the Compose
file from being portable, Compose warns you when such a path is used to set `env_file`.

Environment variables declared in the [`environment`](services.md#environment) section override these values. This holds true even if those values are
empty or undefined.

`env_file` can also be a list. The files in the list are processed from the top down. For the same variable
specified in two environment files, the value from the last file in the list stands.

```yml
env_file:
  - ./a.env
  - ./b.env
```

## Use an optional environment file

{{< summary-bar feature_name="Compose required" >}}

The `required` attribute defaults to `true`. When `required` is set to `false` and the `.env` file is missing, Compose silently ignores the entry.

```yml
env_file:
  - path: ./default.env
    required: true # default
  - path: ./override.env
    required: false
```

## Pass raw values

{{< summary-bar feature_name="Compose format" >}}

The `format` attribute lets you use an alternative file format for the `env_file`. When not set, `env_file` is parsed according to the Compose rules outlined in [`Env_file` format](services.md#env_file-format).

`raw` format lets you use an `env_file` with key=value items, but without any attempt from Compose to parse the value for interpolation.
This let you pass values as-is, including quotes and `$` signs.

```yml
env_file:
  - path: ./default.env
    format: raw
```

## Set environment entries

Environment variables can be declared by a single key (no value to equals sign). In this case Compose
relies on you to resolve the value. If the value is not resolved, the variable
is unset and is removed from the service container environment.

Map syntax:

```yml
environment:
  RACK_ENV: development
  SHOW: "true"
  USER_INPUT:
```

Array syntax:

```yml
environment:
  - RACK_ENV=development
  - SHOW=true
  - USER_INPUT
```

When both `env_file` and `environment` are set for a service, values set by `environment` have precedence.

