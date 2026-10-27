---
title: Choose a volume export destination
---

{{< tabs >}}
{{< tab name="Local or Hub storage" >}}

- **Local file**: Specify a file name and select a folder.
- **Local image**: Select a local image to export the content to. Any
 existing data in the image will be replaced by the exported content.
- **New image**: Specify a name for the new image.
- **Registry**: Specify a Docker Hub repository.

{{< /tab >}}
{{< tab name="External cloud storage" >}}

You must have a [Docker Business subscription](https://www.docker.com/pricing?ref=Docs&refAction=DocsDesktopVolumes) to export to an external cloud provider.

Select your cloud provider and then specify the URL to upload to the storage.
Refer to the following documentation for your cloud provider to learn how to
obtain a URL.

- Amazon Web Services: [Create a presigned URL of Amazon S3 using an AWS SDK](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example_s3_Scenario_PresignedUrl_section.html)
- Microsoft Azure: [Generate a SAS token and URL](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/api/connection-strings/generate-sas-token)
- Google Cloud: [Create a signed URL to upload an object](https://cloud.google.com/storage/docs/access-control/signing-urls-with-helpers#upload-object)

{{< /tab >}}
{{< /tabs >}}
