---
description: Docker security announcements
keywords: Docker, CVEs, security, notice, Log4J 2, Log4Shell, Text4Shell, announcements
title: Docker security announcements
linkTitle: Security announcements
outputs: ["HTML", "markdown", "RSS"]
layout: security-announcements
weight: 80
toc_min: 1
toc_max: 2
---

[Subscribe to security RSS feed](/security/security-announcements/index.xml)

## Find guidance

- [Docker Desktop security updates](#docker-desktop-4670-security-update-cve-2026-33990)
- [SSO password login deprecation](#deprecation-of-password-logins-on-cli-when-sso-enforced)
- [SOC 2 and ISO 27001](#soc-2-type-2-attestation-and-iso-27001-certification)
- [runc, BuildKit, and Moby advisory](security-advisories/container-components-2024.md)
- [Text4Shell advisory](security-advisories/text4shell-2022.md)
- [Log4j advisory](security-advisories/log4j-2021.md)

For update prerequisites, see [Docker Desktop release availability](/manuals/desktop/release-availability.md).

## Docker Desktop 4.67.0 security update: CVE-2026-33990

A vulnerability in Docker Desktop was fixed on March 30 in the [4.67.0](/manuals/desktop/previous-versions/4.60-4.69.md#4670) release:

- Addressed [CVE-2026-33990](https://www.cve.org/cverecord?id=CVE-2026-33990), SSRF in Docker Model Runner OCI Registry Client


## Docker Desktop 4.62.0 security update: CVE-2026-28400

A vulnerability in Docker Desktop was fixed on February 23 in the [4.62.0](/manuals/desktop/previous-versions/4.60-4.69.md#4620) release:

- Addressed [CVE-2026-28400](https://www.cve.org/cverecord?id=CVE-2026-28400), runtime flag injection in Docker Model Runner.

## Docker Desktop 4.62.0 security update: CVE-2026-2664

A vulnerability in Docker Desktop was fixed on February 23 in the [4.62.0](/manuals/desktop/previous-versions/4.60-4.69.md#4620) release:

- Fixed [CVE-2026-2664](https://www.cve.org/cverecord?id=CVE-2026-2664), out of bounds read in gRPC-FUSE kernel module.

## Docker Desktop 4.54.0 security update: CVE-2025-13743

A vulnerability in Docker Desktop was fixed on December 4 in the [4.54.0](/manuals/desktop/previous-versions/4.50-4.59.md#4540) release:

- Fixed [CVE-2025-13743](https://www.cve.org/cverecord?id=CVE-2025-13743) where Docker Desktop diagnostics bundles were found to include expired Hub PATs in log output due to error object serialization.

## Docker Desktop 4.49.0 security update: CVE-2025-9164

A vulnerability in Docker Desktop for Windows was fixed on October 23 in the [4.49.0](/manuals/desktop/previous-versions/4.40-4.49.md#4490) release:

- Fixed [CVE-2025-9164](https://www.cve.org/cverecord?id=CVE-2025-9164) where the Docker Desktop for Windows installer was vulnerable to DLL hijacking due to insecure DLL search order. The installer searches for required DLLs in the user's Downloads folder before checking system directories, allowing local privilege escalation through malicious DLL placement.

## Docker Desktop 4.47.0 security update: CVE-2025-10657

A vulnerability in Docker Desktop was fixed on September 25 in the [4.47.0](/manuals/desktop/previous-versions/4.40-4.49.md#4470) release:

- Fixed [CVE-2025-10657](https://www.cve.org/CVERecord?id=CVE-2025-10657) where the Enhanced Container Isolation [Docker Socket command restrictions](../enterprise/security/hardened-desktop/enhanced-container-isolation/config.md#command-restrictions) feature was not working properly in Docker Desktop 4.46.0 only (the configuration for it was being ignored).

## Docker Desktop 4.44.3 security update: CVE-2025-9074

_Last updated August 20, 2025_

A vulnerability in Docker Desktop was fixed on August 20 in the [4.44.3](/manuals/desktop/previous-versions/4.40-4.49.md#4443) release:

- Fixed [CVE-2025-9074](https://www.cve.org/CVERecord?id=CVE-2025-9074) where a malicious container running on Docker Desktop could access the Docker Engine and launch additional containers without requiring the Docker socket to be mounted. This could allow unauthorized access to user files on the host system. Enhanced Container Isolation (ECI) does not mitigate this vulnerability.


## Docker Desktop 4.44.0 security update: CVE-2025-23266

_Last updated July 31, 2025_

We are aware of [CVE-2025-23266](https://nvd.nist.gov/vuln/detail/CVE-2025-23266), a critical vulnerability affecting the NVIDIA Container Toolkit in CDI mode up to version 1.17.7. Docker Desktop includes version 1.17.8, which is not impacted. However, older versions of Docker Desktop that bundled earlier toolkit versions may be affected if CDI mode was manually enabled. Upgrade to Docker Desktop 4.44 or later to ensure you're using the patched version.

## Docker Desktop 4.43.0 security update: CVE-2025-6587

_Last updated July 03, 2025_

A vulnerability in Docker Desktop was fixed on July 03 in the [4.43.0](/manuals/desktop/previous-versions/4.40-4.49.md#4430) release:

- Fixed [CVE-2025-6587](https://www.cve.org/CVERecord?id=CVE-2025-6587) where sensitive system environment variables were included in Docker Desktop diagnostic logs, allowing for potential secret exposure.

## Docker Desktop 4.41.0 Security Update: CVE-2025-3224, CVE-2025-4095, and CVE-2025-3911

_Last updated May 15, 2025_

Three vulnerabilities in Docker Desktop were fixed on April 28 in the [4.41.0](/manuals/desktop/previous-versions/4.40-4.49.md#4410) release.

- Fixed [CVE-2025-3224](https://www.cve.org/CVERecord?id=CVE-2025-3224) allowing an attacker with access to a user machine to perform an elevation of privilege when Docker Desktop updates.
- Fixed [CVE-2025-4095](https://www.cve.org/CVERecord?id=CVE-2025-4095) where Registry Access Management (RAM) policies were not enforced when using a MacOS configuration profile, allowing users to pull images from unapproved registries.
- Fixed [CVE-2025-3911](https://www.cve.org/CVERecord?id=CVE-2025-3911) allowing an attacker with read access to a user's machine to obtain sensitive information from Docker Desktop log files, including environment variables configured for running containers.

We strongly encourage you to update to Docker Desktop [4.41.0](/manuals/desktop/previous-versions/4.40-4.49.md#4410).

## Docker Desktop 4.34.2 Security Update: CVE-2024-8695 and CVE-2024-8696

_Last updated September 13, 2024_

Two remote code execution (RCE) vulnerabilities in Docker Desktop related to Docker Extensions were reported by [Cure53](https://cure53.de/) and were fixed on September 12 in the [4.34.2](/manuals/desktop/previous-versions/4.30-4.39.md#4342) release.

- [CVE-2024-8695](https://www.cve.org/cverecord?id=CVE-2024-8695): A remote code execution (RCE) vulnerability via crafted extension description/changelog could be abused by a malicious extension in Docker Desktop before 4.34.2. [Critical]
- [CVE-2024-8696](https://www.cve.org/cverecord?id=CVE-2024-8696): A remote code execution (RCE) vulnerability via crafted extension publisher-url/additional-urls could be abused by a malicious extension in Docker Desktop before 4.34.2. [High]

No existing extensions exploiting the vulnerabilities were found in the Extensions Marketplace. The Docker Team will be closely monitoring and diligently reviewing any requests for publishing new extensions.

We strongly encourage you to update to Docker Desktop [4.34.2](/manuals/desktop/previous-versions/4.30-4.39.md#4342). If you are unable to update promptly, you can [disable Docker Extensions](/manuals/extensions/settings-feedback.md#turn-on-or-turn-off-extensions) as a workaround.

## Deprecation of password logins on CLI when SSO enforced

_Last updated July, 2024_

When [SSO enforcement](/manuals/enterprise/security/single-sign-on/connect.md) was first introduced, Docker provided a grace period to continue to let passwords be used on the Docker CLI when authenticating to Docker Hub. This was allowed so organizations could more easily use SSO enforcement. It is recommended that administrators configuring SSO encourage users using the CLI [to switch over to Personal Access Tokens](/manuals/security/access-tokens.md#use-personal-access-tokens) in anticipation of this grace period ending.

On September 16, 2024 the grace period will end and passwords will no longer be able to authenticate to Docker Hub via the Docker CLI when SSO is enforced. Affected users are required to switch over to using PATs to continue signing in.

At Docker, we want the experience to be the most secure for our developers and organizations and this deprecation is an essential step in that direction.

## SOC 2 Type 2 attestation and ISO 27001 certification

_Last updated June, 2024_

Docker is pleased to announce that we have received our SOC 2 Type 2 attestation and ISO 27001 certification with no exceptions or major non-conformities.

Security is a fundamental pillar to Docker's operations, which is embedded into our overall mission and company strategy. Docker's products are core to our user community and our SOC 2 Type 2 attestation and ISO 27001 certification demonstrate Docker's ongoing commitment to security to our user base.

For more information, see the [Blog announcement](https://www.docker.com/blog/docker-announces-soc-2-type-2-attestation-iso-27001-certification/).

## Docker Security Advisory: Multiple Vulnerabilities in runc, BuildKit, and Moby

See [affected versions, updates, mitigations, and technical details](security-advisories/container-components-2024.md).

## Text4Shell CVE-2022-42889

See [affected versions, scanning guidance, and Docker Official Images](security-advisories/text4shell-2022.md).

## Log4j 2 CVE-2021-44228

See [affected versions, updates, and scanning guidance](security-advisories/log4j-2021.md).

## Docker Official Images impacted by Log4j 2 CVE

See [patched versions and image-specific exceptions](security-advisories/log4j-2021.md#docker-official-images-impacted-by-log4j-2-cve).

