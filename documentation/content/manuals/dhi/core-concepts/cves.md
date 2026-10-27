---
title: Common Vulnerabilities and Exposures (CVEs)
linktitle: CVEs
description: Understand what CVEs are, how Docker Hardened Images reduce exposure, and how to scan images for vulnerabilities using popular tools.
keywords: docker cve scan, grype vulnerability scanner, trivy image scan, vex attestation, secure container images
---

## What are CVEs?

CVEs are publicly disclosed cybersecurity flaws in software or hardware. Each
CVE is assigned a unique identifier (e.g., CVE-2024-12345) and includes a
standardized description, allowing organizations to track and address
vulnerabilities consistently.

In the context of Docker, CVEs often pertain to issues within base images, or
application dependencies. These vulnerabilities can range from minor bugs to
critical security risks, such as remote code execution or privilege escalation.

## Why are CVEs important?

Regularly scanning and updating Docker images to mitigate CVEs is crucial for
maintaining a secure and compliant environment. Ignoring CVEs can lead to severe
security breaches, including:

- Unauthorized access: Exploits can grant attackers unauthorized access to
  systems.
- Data breaches: Sensitive information can be exposed or stolen.
- Service disruptions: Vulnerabilities can be leveraged to disrupt services or
  cause downtime.
- Compliance violations: Failure to address known vulnerabilities can lead to
  non-compliance with industry regulations and standards.

## How Docker Hardened Images help mitigate CVEs

Docker Hardened Images (DHIs) are crafted to minimize the risk of CVEs from the
outset. By adopting a security-first approach, DHIs offer several advantages in
CVE mitigation:

- Reduced attack surface: DHIs are built using a distroless approach, stripping
  away unnecessary components and packages. This reduction in image size, up to
  95% smaller than traditional images, limits the number of potential
  vulnerabilities, making it harder for attackers to exploit unneeded software.

- Faster CVE remediation: Maintained by Docker with an [enterprise-grade SLA](https://docs.docker.com/go/dhi-sla/),
  DHIs are continuously updated to address known vulnerabilities. Critical and
  high-severity CVEs are patched quickly, ensuring that your containers remain
  secure without manual intervention.

- Proactive vulnerability management: By utilizing DHIs, organizations can
  proactively manage vulnerabilities. The images come with CVE and Vulnerability
  Exposure (VEX) feeds, enabling teams to stay informed about potential threats
  and take necessary actions promptly.

## VEX context

Docker Hardened Images include signed [VEX (Vulnerability Exploitability
eXchange)](./vex.md) attestations that identify vulnerabilities not relevant to the image’s
runtime behavior.

See the [VEX standard and document structure](/manuals/security/vex.md) and [DHI VEX status reference](vex.md#vex-status-reference).
