---
title: Securing your software supply chain with Docker Scout
linkTitle: Docker Scout
summary: |
  Enhance container security by automating vulnerability detection and
  remediation.
description: |
  Learn how to use Docker Scout to enhance container security by automating
  vulnerability detection and remediation, ensuring compliance, and protecting
  your development workflow.
tags: [product-demo]
aliases:
  - /learning-paths/docker-scout/
params:
  image: images/learning-paths/scout.png
  time: 20 minutes
  resource_links:
    - title: Docker Scout overview
      url: /scout/
    - title: Docker Scout quickstart
      url: /scout/quickstart/
    - title: Install Docker Scout
      url: /scout/install/
---

When container images are insecure, significant risks can arise. Around 60% of
organizations have reported experiencing at least one security breach or
vulnerability incident within a year, [resulting in operational
disruption][CSA]. These incidents often result in considerable downtime, with
44% of affected companies experiencing over an hour of downtime per event. The
financial impact is substantial, with [the average data breach cost reaching
$4.45 million][IBM]. This highlights the critical importance of maintaining
robust container security measures.

Docker Scout enhances container security by providing automated vulnerability
detection and remediation, addressing insecure container images, and ensuring
compliance with security standards.

[CSA]: https://cloudsecurityalliance.org/blog/2023/09/21/2023-global-cloud-threat-report-cloud-attacks-are-lightning-fast
[IBM]: https://www.ibm.com/reports/data-breach

## What you'll learn

- Define Secure Software Supply Chain (SSSC)
- Review SBOMs and how to use them
- Detect and monitor vulnerabilities

## Follow the guide

1. [Why Docker Scout?](./why.md)
2. [Docker Scout demo](./demo.md)
3. [Software supply chain security](./s3c.md)
4. [Software Bill of Materials](./sbom.md)
5. [Attestations](./attestations.md)
6. [Remediation](./remediation.md)

See also [Common challenges and questions](./common-questions.md).

## Try the tasks

- [Install Docker Scout](/manuals/scout/install.md)
- [Analyze and fix the example image](/manuals/scout/quickstart.md)
- [Choose a Docker Scout task](/manuals/scout/_index.md#choose-a-task)

## Tools integration

Works well with Docker Desktop, GitHub Actions, Jenkins, Kubernetes, and
other CI solutions.

## Who’s this for?

- DevOps engineers who need to integrate automated security checks into CI/CD
  pipelines to enhance the security and efficiency of their workflows.
- Developers who want to use Docker Scout to identify and remediate
  vulnerabilities early in the development process, ensuring the production of
  secure container images.
- Security professionals who must enforce security compliance, conduct
  vulnerability assessments, and ensure the overall security of containerized
  applications.

<div id="scout-lp-survey-anchor"></div>
