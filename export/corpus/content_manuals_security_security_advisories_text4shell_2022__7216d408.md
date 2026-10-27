---
title: Text4Shell CVE-2022-42889 (October 2022)
---

## Find guidance

- [Scan images on Docker Hub](#scan-images-on-docker-hub)
- [Docker Official Images](#docker-official-images-impacted-by-cve-2022-42889)

## Text4Shell CVE-2022-42889

_Last updated October 2022_

[CVE-2022-42889](https://nvd.nist.gov/vuln/detail/CVE-2022-42889) has been discovered in the popular Apache Commons Text library. Versions of this library up to but not including 1.10.0 are affected by this vulnerability.

We strongly encourage you to update to the latest version of [Apache Commons Text](https://commons.apache.org/proper/commons-text/download_text.cgi).

### Scan images on Docker Hub

Docker Hub security scans triggered after 1200 UTC 21 October 2021 are now
correctly identifying the Text4Shell CVE. Scans before this date do not
currently reflect the status of this vulnerability. Therefore, we recommend that
you trigger scans by pushing new images to Docker Hub to view the status of
the Text4Shell CVE in the vulnerability report. For detailed instructions, see [Scan images on Docker Hub](/manuals/docker-hub/repos/manage/vulnerability-scanning.md).

### Docker Official Images impacted by CVE-2022-42889

A number of [Docker Official Images](/manuals/docker-hub/image-library/trusted-content.md#docker-official-images) contain the vulnerable versions of
Apache Commons Text. The following lists Docker Official Images that
may contain the vulnerable versions of Apache Commons Text:

- [bonita](https://hub.docker.com/_/bonita)
- [Couchbase](https://hub.docker.com/_/couchbase)
- [Geonetwork](https://hub.docker.com/_/geonetwork)
- [neo4j](https://hub.docker.com/_/neo4j)
- [sliverpeas](https://hub.docker.com/_/sliverpeas)
- [solr](https://hub.docker.com/_/solr)
- [xwiki](https://hub.docker.com/_/xwiki)

We have updated
Apache Commons Text in these images to the latest version. Some of these images may not be
vulnerable for other reasons. We recommend that you also review the guidelines published on the upstream websites.

