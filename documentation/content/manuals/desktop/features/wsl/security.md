---
title: WSL 2 security in Docker Desktop
---

## WSL 2 security in Docker Desktop

Docker Desktop's WSL 2 integration works within WSL's existing security model and does not introduce security risks beyond standard WSL behavior.

Docker Desktop runs inside its own `docker-desktop` WSL distribution, isolated from other distributions in the same way any two WSL distributions are isolated from each other. Interaction between Docker Desktop and other distributions only occurs when you explicitly enable WSL integration for those distributions. This feature allows easy access to the Docker CLI from integrated distributions. 

WSL is designed to aid interoperability between Windows and Linux environments. Its file system is accessible from the Windows host `\\wsl$`, meaning Windows processes can read and modify files within WSL. This behavior is not specific to Docker Desktop, but rather a core aspect of WSL itself.

For environments that require stricter isolation:

- Run Docker Desktop in Hyper-V mode instead of WSL 2 to avoid the shared-kernel model entirely.
- Enable [Enhanced Container Isolation](/manuals/enterprise/security/hardened-desktop/enhanced-container-isolation/_index.md) to add an additional layer of protection around container workloads regardless of backend.
