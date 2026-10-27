---
title: Vulnerability Exploitability eXchange (VEX)
---

Vulnerability Exploitability eXchange (VEX) is a standard format for
documenting vulnerabilities in the context of a software package or product.

## Statuses and document structure

The VEX standard is defined by a working group by the United States
Cybersecurity and Infrastructure Security Agency (CISA). At the core of VEX are
exploitability assessments. These assessments describe the status of a given
CVE for a product. The possible vulnerability statuses in VEX are:

- Not affected: No remediation is required regarding this vulnerability.
- Affected: Actions are recommended to remediate or address this vulnerability.
- Fixed: These product versions contain a fix for the vulnerability.
- Under investigation: It is not yet known whether these product versions are affected by the vulnerability. An update will be provided in a later release.

There are multiple implementations and formats of VEX. Docker Scout supports
the [OpenVex](https://github.com/openvex/spec) implementation. Regardless of
the specific implementation, the core idea is the same: to provide a framework
for describing the impact of vulnerabilities. Key components of VEX regardless
of implementation includes:

VEX document
: A type of security advisory for storing VEX statements.
  The format of the document depends on the specific implementation.

VEX statement
: Describes the status of a vulnerability in a product,
  whether it's exploitable, and whether there are ways to remediate the issue.

Justification and impact
: Depending on the vulnerability status, statements include a justification
  or impact statement describing why a product is or isn't affected.

Action statements
: Describe how to remediate or mitigate the vulnerability.
