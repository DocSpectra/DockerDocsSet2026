---
title: STIG
description: Learn how Docker Hardened Images provide STIG-ready container images with verifiable security scan attestations for government and enterprise compliance requirements.
keywords: docker stig, stig-ready images, stig guidance, openscap docker, secure container images
---

{{< summary-bar feature_name="Docker Hardened Images" >}}

## What is STIG?

[Security Technical Implementation Guides
(STIGs)](https://public.cyber.mil/stigs/) are configuration standards published
by the U.S. Defense Information Systems Agency (DISA). They define security
requirements for operating systems, applications, databases, and other
technologies used in U.S. Department of Defense (DoD) environments.

STIGs help ensure that systems are configured securely and consistently to
reduce vulnerabilities. They are often based on broader requirements like the
DoD's General Purpose Operating System Security Requirements Guide (GPOS SRG).

## Why STIG guidance matters

Following STIG guidance is critical for organizations that work with or support
U.S. government systems. It demonstrates alignment with DoD security standards
and helps:

- Accelerate Authority to Operate (ATO) processes for DoD systems
- Reduce the risk of misconfiguration and exploitable weaknesses
- Simplify audits and reporting through standardized baselines

Even outside of federal environments, STIGs are used by security-conscious
organizations as a benchmark for hardened system configurations.

STIGs are derived from broader NIST guidance, particularly [NIST Special
Publication 800-53](https://csrc.nist.gov/publications/sp800), which defines a
catalog of security and privacy controls for federal systems. Organizations
pursuing compliance with 800-53 or related frameworks (such as FedRAMP) can use
STIGs as implementation guides that help meet applicable control requirements.

## How Docker Hardened Images help apply STIG guidance

Docker Hardened Images (DHIs) include STIG variants that are scanned against
custom STIG-based profiles and include signed STIG scan attestations. These
attestations can support audits and compliance reporting.

While Docker Hardened Images are available to all, the STIG variant requires a
Docker subscription.

Docker creates custom STIG-based profiles for images based on the GPOS SRG and
DoD Container Hardening Process Guide. Because DISA has not published a STIG
specifically for containers, these profiles help apply STIG-like guidance to
container environments in a consistent, reviewable way and are designed to
reduce false positives common in container images.

