---
title: DHI image definitions and catalog layout
description: Declarative image definitions, build frontends, catalog organization, and variant types.
---

Docker Hardened Images (DHI) are built from declarative YAML definition files
instead of traditional Dockerfiles. A single YAML file describes exactly what
goes into an image: packages, users, environment variables, entrypoint, and
metadata. The DHI build system produces a signed image containing only the required
packages, with a Software Bill of Materials (SBOM) and SLSA Build Level 3
provenance.

## How DHI builds differ from Dockerfiles

A Dockerfile is a sequence of imperative instructions: `RUN`, `COPY`, `FROM`.
A DHI definition file is a declarative specification. You describe the desired
state of the image, and the build system figures out how to produce it.

Every DHI definition starts with a syntax directive that tells BuildKit which
DHI build frontend to use. The frontend is the component that parses and
processes YAML definitions instead of the default Dockerfile parser:

```yaml
# syntax=dhi.io/build:2-alpine3.23
```

The frontend version corresponds to the base distribution:

| Distribution        | Syntax directive                       |
|---------------------|----------------------------------------|
| Alpine 3.22         | `# syntax=dhi.io/build:2-alpine3.22`  |
| Alpine 3.23         | `# syntax=dhi.io/build:2-alpine3.23`  |
| Debian 12 (Bookworm)| `# syntax=dhi.io/build:2-debian12`    |
| Debian 13 (Trixie)  | `# syntax=dhi.io/build:2-debian13`    |

The DHI build system reads the YAML, resolves packages from the specified
repositories, assembles the filesystem, creates user accounts, sets metadata,
and produces a signed OCI image.

## Explore the catalog for reference

The [DHI catalog repository](https://github.com/docker-hardened-images/catalog)
is open source under Apache 2.0 and contains every official image definition.
Studying existing definitions is the best way to learn the YAML patterns for
different image types.

The catalog follows this directory structure:

```text
catalog/
├── image/
│   ├── alpine-base/
│   │   ├── alpine-3.23/
│   │   │   ├── 3.23.yaml            # runtime variant
│   │   │   └── 3.23-dev.yaml        # dev variant
│   │   ├── guides.md
│   │   ├── info.yaml
│   │   ├── logo.svg
│   │   └── overview.md
│   ├── nginx/
│   │   ├── alpine-3.22/
│   │   ├── alpine-3.23/
│   │   │   ├── mainline.yaml
│   │   │   ├── mainline-dev.yaml
│   │   │   ├── stable.yaml
│   │   │   └── stable-dev.yaml
│   │   ├── debian-12/
│   │   ├── debian-13/
│   │   ├── bin/
│   │   ├── guides.md
│   │   ├── info.yaml
│   │   ├── logo.svg
│   │   └── overview.md
│   └── redis/
│       ├── debian-13/
│       │   ├── 8.0.yaml              # runtime
│       │   ├── 8.0-dev.yaml          # dev
│       │   ├── 8.0-compat.yaml       # compat runtime
│       │   └── 8.0-compat-dev.yaml   # compat dev
│       ├── guides.md
│       ├── info.yaml
│       ├── logo.svg
│       └── overview.md
├── chart/
└── package/
```

Each image organizes its variants by distribution. Images support multiple
variant types:

- A `runtime` variant is minimal and typically runs as a non-root user.
- A `dev` variant adds a shell, package manager, and development tools.
- A compatibility variant adds common shell utilities such as `bash`,
  `coreutils`, `grep`, and `sed` for use with existing workflows. Compatibility
  images use the `flavor: compat` field alongside a `runtime` or `dev` variant.
- A compatibility-dev variant combines the compatibility packages with dev
  tools.

Some images also support additional flavors such as `sfw` (software framework)
variants. Refer to the catalog for the full list of available variants for each
image.
