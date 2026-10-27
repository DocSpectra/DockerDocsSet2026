---
title: runc, BuildKit, and Moby security advisory (February 2024)
---

## Find guidance

- [Affected versions](#affected-versions)
- [Updates and mitigations](#remediation)
- [Technical details](#technical-details-and-impact)
- [Docker product impact](#how-are-docker-products-affected)
- [Advisory links](#advisory-links)

## Docker Security Advisory: Multiple Vulnerabilities in runc, BuildKit, and Moby

_Last updated February 2, 2024_

We at Docker prioritize the security and integrity of our software and the trust of our users. Security researchers at Snyk Labs identified and reported four security vulnerabilities in the container ecosystem. One of the vulnerabilities, [CVE-2024-21626](https://scout.docker.com/v/CVE-2024-21626), concerns the runc container runtime, and the other three affect BuildKit ([CVE-2024-23651](https://scout.docker.com/v/CVE-2024-23651), [CVE-2024-23652](https://scout.docker.com/v/CVE-2024-23652), and [CVE-2024-23653](https://scout.docker.com/v/CVE-2024-23653)). We want to assure our community that our team, in collaboration with the reporters and open source maintainers, has been diligently working on coordinating and implementing necessary remediations.

We are committed to maintaining the highest security standards. We have published patched versions of runc, BuildKit, and Moby on January 31 and released an update for Docker Desktop on February 1 to address these vulnerabilities. Additionally, our latest BuildKit and Moby releases included fixes for [CVE-2024-23650](https://scout.docker.com/v/CVE-2024-23650) and [CVE-2024-24557](https://scout.docker.com/v/CVE-2024-24557), discovered respectively by an independent researcher and through Docker's internal research initiatives.

## Affected versions

|                        | Versions Impacted         |
|:-----------------------|:--------------------------|
| `runc`                 | <= 1.1.11                 |
| `BuildKit`             | <= 0.12.4                 |
| `Moby (Docker Engine)` | <= 25.0.1 and <= 24.0.8   |
| `Docker Desktop`       | <= 4.27.0                 |

## Remediation

### What should I do if I'm on an affected version?

If you are using affected versions of runc, BuildKit, Moby, or Docker Desktop, make sure to update to the latest versions, linked in the following table:

|                        | Patched Versions          |
|:-----------------------|:--------------------------|
| `runc`                 | >= [1.1.12](https://github.com/opencontainers/runc/releases/tag/v1.1.12)                 |
| `BuildKit`             | >= [0.12.5](https://github.com/moby/buildkit/releases/tag/v0.12.5)                 |
| `Moby (Docker Engine)` | >= [25.0.2](https://github.com/moby/moby/releases/tag/v25.0.2) and >= [24.0.9](https://github.com/moby/moby/releases/tag/v24.0.9)   |
| `Docker Desktop`       | >= [4.27.1](/manuals/desktop/previous-versions/4.20-4.29.md#4271)                 |


If you are unable to update to an unaffected version promptly, follow these best practices to mitigate risk:

* Only use trusted Docker images (such as [Docker Official Images](/manuals/docker-hub/image-library/trusted-content.md#docker-official-images)).
* Don't build Docker images from untrusted sources or untrusted Dockerfiles.
* If you are a Docker Business customer using Docker Desktop and unable to update to v4.27.1, make sure to enable [Hardened Docker Desktop](/manuals/enterprise/security/hardened-desktop/_index.md) features such as:
  * [Enhanced Container Isolation](/manuals/enterprise/security/hardened-desktop/enhanced-container-isolation/_index.md), which mitigates the impact of CVE-2024-21626 in the case of running containers from malicious images.
  * [Image Access Management](/manuals/enterprise/security/hardened-desktop/image-access-management.md), and [Registry Access Management](/manuals/enterprise/security/hardened-desktop/registry-access-management.md), which give organizations control over which images and repositories their users can access.
* For CVE-2024-23650, CVE-2024-23651, CVE-2024-23652, and CVE-2024-23653, avoid using BuildKit frontend from an untrusted source. A frontend image is usually specified as the #syntax line on your Dockerfile, or with `--frontend` flag when using the `buildctl build` command.
* To mitigate CVE-2024-24557, make sure to either use BuildKit or disable caching when building images. From the CLI this can be done via the `DOCKER_BUILDKIT=1` environment variable (default for Moby >= v23.0 if the buildx plugin is installed) or the `--no-cache flag`. If you are using the HTTP API directly or through a client, the same can be done by setting `nocache` to `true` or `version` to `2` for the [/build API endpoint](https://docs.docker.com/reference/api/engine/version/v1.44/#tag/Image/operation/ImageBuild).

### Technical details and impact

#### CVE-2024-21626 (High)

In runc v1.1.11 and earlier, due to certain leaked file descriptors, an attacker can gain access to the host filesystem by causing a newly-spawned container process (from `runc exec`) to have a working directory in the host filesystem namespace, or by tricking a user to run a malicious image and allow a container process to gain access to the host filesystem through `runc run`. The attacks can also be adapted to overwrite semi-arbitrary host binaries, allowing for complete container escapes. Note that when using higher-level runtimes (such as Docker or Kubernetes), this vulnerability can be exploited by running a malicious container image without additional configuration or by passing specific workdir options when starting a container. The vulnerability can also be exploited from within Dockerfiles in the case of Docker.

_The issue has been fixed in runc v1.1.12._

#### CVE-2024-23651 (High)

In BuildKit <= v0.12.4, two malicious build steps running in parallel sharing the same cache mounts with subpaths could cause a race condition, leading to files from the host system being accessible to the build container. This will only occur if a user is trying to build a Dockerfile of a malicious project.

_The issue has been fixed in BuildKit v0.12.5._

#### CVE-2024-23652 (High)

In BuildKit <= v0.12.4, a malicious BuildKit frontend or Dockerfile using `RUN --mount` could trick the feature that removes empty files created for the mountpoints into removing a file outside the container from the host system. This will only occur if a user is using a malicious Dockerfile.

_The issue has been fixed in BuildKit v0.12.5._

#### CVE-2024-23653 (High)

In addition to running containers as build steps, BuildKit also provides APIs for running interactive containers based on built images. In BuildKit <= v0.12.4, it is possible to use these APIs to ask BuildKit to run a container with elevated privileges. Normally, running such containers is only allowed if special `security.insecure` entitlement is enabled both by buildkitd configuration and allowed by the user initializing the build request.

_The issue has been fixed in BuildKit v0.12.5._

#### CVE-2024-23650 (Medium)

In BuildKit <= v0.12.4, a malicious BuildKit client or frontend could craft a request that could lead to BuildKit daemon crashing with a panic.

_The issue has been fixed in BuildKit v0.12.5._

#### CVE-2024-24557 (Medium)

In Moby <= v25.0.1 and <= v24.0.8, the classic builder cache system is prone to cache poisoning if the image is built FROM scratch. Also, changes to some instructions (most important being `HEALTHCHECK` and `ONBUILD`) would not cause a cache miss. An attacker with knowledge of the Dockerfile someone is using could poison their cache by making them pull a specially crafted image that would be considered a valid cache candidate for some build steps.

_The issue has been fixed in Moby >= v25.0.2 and >= v24.0.9._

### How are Docker products affected?

#### Docker Desktop

Docker Desktop v4.27.0 and earlier are affected. Docker Desktop v4.27.1 was released on February 1 and includes runc, BuildKit, and dockerd binaries patches. In addition to updating to this new version, we encourage all Docker users to diligently use Docker images and Dockerfiles and ensure you only use trusted content in your builds.

Before updating, see [Docker Desktop update prerequisites](/manuals/desktop/release-availability.md#before-updating).

#### Docker Build Cloud

Any new Docker Build Cloud builder instances will be provisioned with the latest Docker Engine and BuildKit versions and will, therefore, be unaffected by these CVEs. Updates have also been rolled out to existing Docker Build Cloud builders.

_No other Docker products are affected by these vulnerabilities._

### Advisory links

* Runc
  * [CVE-2024-21626](https://github.com/opencontainers/runc/security/advisories/GHSA-xr7r-f8xq-vfvv)
* BuildKit
  * [CVE-2024-23650](https://github.com/moby/buildkit/security/advisories/GHSA-9p26-698r-w4hx)
  * [CVE-2024-23651](https://github.com/moby/buildkit/security/advisories/GHSA-m3r6-h7wv-7xxv)
  * [CVE-2024-23652](https://github.com/moby/buildkit/security/advisories/GHSA-4v98-7qmw-rqr8)
  * [CVE-2024-23653](https://github.com/moby/buildkit/security/advisories/GHSA-wr6v-9f75-vh2g)
* Moby
  * [CVE-2024-24557](https://github.com/moby/moby/security/advisories/GHSA-xw73-rw38-6vjc)

