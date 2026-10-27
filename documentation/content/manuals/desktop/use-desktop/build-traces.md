---
title: Inspect a Docker Desktop build trace with Jaeger
---

See [Build inspection tabs and metrics](build-inspection-reference.md#outputs-and-artifacts) for trace formats.

## Inspect build traces with Jaeger

Using a Jaeger client, you can import and inspect build traces from Docker
Desktop. The following steps show you how to export a trace from Docker Desktop
and view it in [Jaeger](https://www.jaegertracing.io/):

1. Start Jaeger UI:

   ```console
   $ docker run -d --name jaeger -p "16686:16686" jaegertracing/all-in-one
   ```

2. Open the Builds view in Docker Desktop, and select a completed build.

3. Navigate to the **Build results** section, open the actions menu and select **Download as Jaeger format**.

   <video controls>
     <source src="/assets/video/build-jaeger-export.mp4" type="video/mp4" />
   </video>

4. Go to <http://localhost:16686> in your browser to open Jaeger UI.

5. Select the **Upload** tab and open the Jaeger build trace you just exported.

Now you can analyze the build trace using the Jaeger UI:

![Jaeger UI screenshot](../images/build-ui-jaeger-screenshot.png "Screenshot of a build trace in the Jaeger UI")
