---
title: Compose Bridge transformations
description: Transformation inputs, outputs, template syntax, and helper functions.
---

{{< summary-bar feature_name="Compose bridge" >}}

## How it works 

Compose bridge uses transformations to let you convert a Compose model into another form. 

A transformation is packaged as a Docker image that receives the fully-resolved Compose model as `/in/compose.yaml` and can produce any target format file under `/out`.

Compose Bridge includes a default Kubernetes transformation using Go templates, which you can customize by replacing or extending templates.

### Template syntax

Compose Bridge makes use of templates to transform a Compose configuration file into Kubernetes manifests. Templates are plain text files that use the [Go templating syntax](https://pkg.go.dev/text/template). This enables the insertion of logic and data, making the templates dynamic and adaptable according to the Compose model.

When a template is executed, it must produce a YAML file which is the standard format for Kubernetes manifests. Multiple files can be generated as long as they are separated by `---`

Each YAML output file begins with custom header notation, for example:

```yaml
#! manifest.yaml
```

In the following example, a template iterates over services defined in a `compose.yaml` file. For each service, a dedicated Kubernetes manifest file is generated, named according to the service and containing specified configurations.

```yaml
{{ range $name, $service := .services }}
---
#! {{ $name }}-manifest.yaml
# Generated code, do not edit
key: value
## ...
{{ end }}
```

### Input model

You can generate the input model by running `docker compose config`. 

This canonical YAML output serves as the input for Compose Bridge transformations. Within the templates, data from the `compose.yaml` is accessed using dot notation, allowing you to navigate through nested data structures. For example, to access the deployment mode of a service, you would use `service.deploy.mode`:

 ```yaml
# iterate over a yaml sequence
{{ range $name, $service := .services }}
  # access a nested attribute using dot notation
  {{ if eq $service.deploy.mode "global" }}
kind: DaemonSet
  {{ end }}
{{ end }}
```

You can check the [Compose Specification JSON schema](https://github.com/compose-spec/compose-go/blob/main/schema/compose-spec.json) for a full overview of the Compose model. This schema outlines all possible configurations and their data types in the Compose model. 

### Helper functions

As part of the Go templating syntax, Compose Bridge offers a set of YAML helper functions designed to manipulate data within the templates efficiently:

| Function    | Description                                                                                                 |
| ----------- | ----------------------------------------------------------------------------------------------------------- |
| `seconds`   | Converts a [duration](/reference/compose-file/extension.md#specifying-durations) into an integer (seconds). |
| `uppercase` | Converts a string to uppercase.                                                                             |
| `title`     | Capitalizes the first letter of each word.                                                                  |
| `safe`      | Converts a string into a safe identifier (replaces non-lowercase characters with `-`).                      |
| `truncate`  | Removes the first N elements from a list.                                                                   |
| `join`      | Joins list elements into a single string with a separator.                                                  |
| `base64`    | Encodes a string as base64 (used for Kubernetes secrets).                                                   |
| `map`       | Maps values using `“value -> newValue”` syntax.                                                             |
| `indent`    | Indents string content by N spaces.                                                                         |
| `helmValue` | Outputs a Helm-style template value.                                                                        |

In the following example, the template checks if a healthcheck interval is specified for a service, applies the `seconds` function to convert this interval into seconds and assigns the value to the `periodSeconds` attribute.

```yaml
{{ if $service.healthcheck.interval }}
            periodSeconds: {{ $service.healthcheck.interval | seconds }}{{ end }}
{{ end }}
```
