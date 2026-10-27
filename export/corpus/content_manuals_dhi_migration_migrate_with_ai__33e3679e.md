--- 
title: Migrate using Gordon
linktitle: AI-assisted migration
description: Use Gordon to automatically migrate your Dockerfile to Docker Hardened Images
weight: 15
keywords: ai assistant, migrate dockerfile, docker hardened images, automated migration
params:
  sidebar:
    badge:
      color: violet
      text: Experimental
---

{{< summary-bar feature_name="Gordon DHI migration" >}}

You can use Gordon to automatically migrate your
Dockerfile to use Docker Hardened Images (DHI).

## Before you begin

Ensure Gordon is [enabled](/manuals/ai/gordon/_index.md#prerequisites).

For manual migration, see the [migration paths](./_index.md). For migration
considerations, see the [checklist](./checklist.md).

## Migrate your Dockerfile

1. In the terminal, navigate to the directory containing your Dockerfile.
2. Start a conversation with the assistant:
   ```bash
   docker ai
   ```
3. Type:
   ```console
   "Migrate my dockerfile to DHI"
   ```
4. Follow the conversation with the assistant. The assistant will edit your Dockerfile, so when
   it requests access to the filesystem and more, type `yes` to allow the assistant to proceed.

## Review the result

When the migration is complete, you see a success message:

```text
The migration to Docker Hardened Images (DHI) is complete. The updated Dockerfile
successfully builds the image, and no vulnerabilities were detected in the final image.
The functionality and optimizations of the original Dockerfile have been preserved.
```

> [!IMPORTANT]
>
> As with any AI tool, you must verify the assistant's edits and test your image.
