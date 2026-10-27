---
title: Docker Scout exception behavior
---

Vulnerabilities found in container images sometimes need additional context.
Just because an image contains a vulnerable package, it doesn't mean that the
vulnerability is exploitable. **Exceptions** in Docker Scout lets you
acknowledge accepted risks or address false positives in image analysis.

By negating non-applicable vulnerabilities, you can make it easier for yourself
and downstream consumers of your images to understand the security implications
of a vulnerability in the context of an image.

In Docker Scout, exceptions are automatically factored into the results.
If an image contains an exception that flags a CVE as non-applicable,
then that CVE is excluded from analysis results.

## Creation methods

To create an exception for an image, you can:

- Create an exception in the GUI of Docker Scout Dashboard or Docker Desktop.
- Create a VEX document and attach it to the image.

The recommended way to create exceptions is to use Docker Scout Dashboard or
Docker Desktop. The GUI provides a user-friendly interface for creating
exceptions, and it's easy to manage exceptions for multiple images. It also lets
you create exceptions for multiple images, or your entire organization, all at
once.

## Visibility

To view exceptions for images, you need to have the appropriate permissions.

- Exceptions created using the GUI
  are visible to members of your Docker organization. Unauthenticated users or
  users who aren't members of your organization cannot see these exceptions.
- Exceptions created using VEX documents
  are visible to anyone who can pull the image, since the VEX document is
  stored in the image manifest or on filesystem of the image.
