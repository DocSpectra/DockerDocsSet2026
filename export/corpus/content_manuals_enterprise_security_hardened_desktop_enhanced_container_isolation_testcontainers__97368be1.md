---
title: Allow Testcontainers Docker socket access
---

Review [Docker socket configuration and security recommendations](config.md) and [ECI limitations](limitations.md), then use the configuration example below.

For Java/Python testing with Testcontainers:

```json
"dockerSocketMount": {
  "imageList": {
    "images": [
      "docker.io/testcontainers/ryuk:*",
      "testcontainers/*:*"
    ]
  },
  "commandList": {
    "type": "deny",
    "commands": ["push", "build"]
  }
}
```
