---
title: Image attestations and provenance
---

Build attestations describe how an image was built, and what it contains. The
attestations are created at build-time by BuildKit, and become attached to the
final image as metadata.

The purpose of attestations is to make it possible to inspect an image and see
where it comes from, who created it and how, and what it contains. This enables
you to make informed decisions about how an image impacts the supply chain security
of your application. It also enables the use of policy engines for validating
images based on policy rules you've defined.

Two types of build attestations are available:

- [Software Bill of Material (SBOM)](sbom.md): list of software artifacts that an image
  contains, or that were used to build the image.
- Provenance: how an image was built.

## Purpose of attestations

The use of open source and third-party packages is more widespread than ever
before. Developers share and reuse code because it helps increase productivity,
allowing teams to create better products, faster.

Importing and using code created elsewhere without vetting it introduces a
severe security risk. Even if you do review the software that you consume, new
zero-day vulnerabilities are frequently discovered, requiring development teams
take action to remediate them.

Build attestations make it easier to see the contents of an image, and where it
comes from. Use attestations to analyze and decide whether to use an image, or
to see if images you are already using are exposed to vulnerabilities.

You can create attestations by using `docker buildx build` with the
`--provenance` and `--sbom` flags. Attestations attach to the image index,
allowing you to inspect them without pulling the entire image. Docker Scout
leverages this metadata to give you more precise recommendations and better
control over your image's security.
