---
title: Allow development tools Docker socket access
---

Review [Docker socket configuration and security recommendations](config.md) and [ECI limitations](limitations.md), then use the configuration example below.

For local development with Docker-in-Docker:

```json
"dockerSocketMount": {
  "imageList": {
    "images": [
      "docker:dind",
      "docker:cli"
    ]
  },
  "commandList": {
    "type": "deny",
    "commands": ["system*"]
  }
}
```
