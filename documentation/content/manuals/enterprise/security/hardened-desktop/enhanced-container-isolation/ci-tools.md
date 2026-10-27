---
title: Allow CI/CD tools Docker socket access
---

Review [Docker socket configuration and security recommendations](config.md) and [ECI limitations](limitations.md), then use the configuration example below.

For controlled CI/CD container management:

```json
"dockerSocketMount": {
  "imageList": {
    "images": [
      "docker:cli",
      "your-registry.com/ci-tools/*:*"
    ]
  },
  "commandList": {
    "type": "allow",
    "commands": ["ps", "container*", "image*"]
  }
}
```
