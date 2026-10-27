---
title: Software bills of materials
---

A Bill of Materials (BOM) is a list of materials, parts, and the quantities of
each needed to manufacture a product. For example, a BOM for a computer might
list the motherboard, CPU, RAM, power supply, storage devices, case, and other
components, along with the quantities of each that are needed to build the
computer.

A Software Bill of Materials (SBOM) is a list of all the components that make
up a piece of software. This includes open source and third-party components,
as well as any custom code that has been written for the software. An SBOM is
similar to a BOM for a physical product, but for software.

In the context of software supply chain security, SBOMs can help with
identifying and mitigating security and compliance risks in software. By
knowing exactly what components are used in a piece of software, you can
quickly identify and patch vulnerabilities in your components, or determine if
a component is licensed in a way that is incompatible with your project.

The inventory includes libraries and dependencies used in building a software
application, documenting each component's version, origin, and relationship to
other components. Think of it as a "recipe" for your software, detailing every
ingredient and how they come together.

## Contents of an SBOM

An SBOM typically includes the following information:

- The name of the software, such as the name of a library or framework, that
  the SBOM describes.
- The version of the software.
- The license under which the software is distributed.
- A list of other components that the software depends on.

Metadata describing software artifacts may also include authors and a unique
package identifier.

## Why are SBOMs important?

In today's software landscape, applications often comprise numerous components
from various sources, including open-source libraries, third-party services, and
proprietary code. This complexity can obscure visibility into potential
vulnerabilities and complicate compliance efforts. SBOMs address these
challenges by providing a detailed inventory of all components within an
application.

The significance of SBOMs is underscored by several key factors:

- Enhanced transparency: SBOMs offer a comprehensive view of all components that
  constitute an application, enabling organizations to identify and assess risks
  associated with third-party libraries and dependencies.

- Proactive vulnerability management: By maintaining an up-to-date SBOM,
  organizations can swiftly identify and address vulnerabilities in software
  components, reducing the window of exposure to potential exploits.

- Regulatory compliance: Many regulations and industry standards now require
  organizations to maintain control over the software components they use. An
  SBOM facilitates compliance by providing a clear and accessible record.

- Improved incident response: In the event of a security breach, an SBOM
  enables organizations to quickly identify affected components and take
  appropriate action, minimizing potential damage.
