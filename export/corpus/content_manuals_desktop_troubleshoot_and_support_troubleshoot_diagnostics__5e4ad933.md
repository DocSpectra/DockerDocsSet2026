---
title: "Collect Docker Desktop diagnostics"
tags: [Troubleshooting]
---

## Diagnose

> [!TIP]
>
> If you do not find a solution in troubleshooting, browse the GitHub repositories or create a new issue on the [Docker Desktop issue tracker](https://github.com/docker/desktop-feedback).

### Diagnose from the app

Open the [Troubleshoot menu](menu.md#troubleshoot-menu).

1. From **Troubleshoot**, select **Get support**. This opens the in-app Support page and starts collecting the diagnostics.
   > [!NOTE]
   >
   > Gathering diagnostics may take several minutes. Don't close Docker Desktop while the diagnostics are being collected.
2. When the diagnostics collection process is complete, select **Upload to get a Diagnostic ID**.
3. When the diagnostics are uploaded, Docker Desktop prints a diagnostic ID. Copy this ID.
4. [Use your diagnostics ID to get help](#use-your-diagnostics-id-to-get-help), using the ID copied in step 3.

### Diagnose from an error message

1. When an error message appears, select **Gather diagnostics**.
   > [!NOTE]
   >
   > Gathering diagnostics may take several minutes. Don't close Docker Desktop while the diagnostics are being collected.
2. When the diagnostics are uploaded, Docker Desktop prints a diagnostic ID. Copy this ID.
3. [Use your diagnostics ID to get help](#use-your-diagnostics-id-to-get-help), using the ID copied in step 2.

### Diagnose from the terminal

In some cases, it's useful to run the diagnostics yourself, for instance, if
Docker Desktop cannot start.

> [!NOTE]
>
> Gathering diagnostics may take several minutes. Wait for the process to complete before closing the terminal.

{{< tabs group="os" >}}
{{< tab name="Windows" >}}

1. Locate the `com.docker.diagnose` tool:

   ```console
   $ C:\Program Files\Docker\Docker\resources\com.docker.diagnose.exe
   ```

2. Create and upload the diagnostics ID. In PowerShell, run:

   ```console
   $ & "C:\Program Files\Docker\Docker\resources\com.docker.diagnose.exe" gather -upload
   ```

{{< /tab >}}
{{< tab name="Mac" >}}

1. Locate the `com.docker.diagnose` tool:

   ```console
   $ /Applications/Docker.app/Contents/MacOS/com.docker.diagnose
   ```

2. Create and upload the diagnostics ID. Run:

   ```console
   $ /Applications/Docker.app/Contents/MacOS/com.docker.diagnose gather -upload
   ```

{{< /tab >}}
{{< tab name="Linux" >}}

1. Locate the `com.docker.diagnose` tool:

   ```console
   $ /opt/docker-desktop/bin/com.docker.diagnose
   ```

2. Create and upload the diagnostics ID. Run:

   ```console
   $ /opt/docker-desktop/bin/com.docker.diagnose gather -upload
   ```

{{< /tab >}}
{{< /tabs >}}

After the diagnostics have finished, the terminal displays your diagnostics ID and the path to the diagnostics file. The diagnostics ID is composed of your user ID and a timestamp. For example `BE9AFAAF-F68B-41D0-9D12-84760E6B8740/20190905152051`.

> [!TIP]
>
> You can also use the [`docker desktop diagnose` command](/manuals/desktop/features/desktop-cli.md) to diagnose Docker Desktop and upload the diagnostics ID.

### View the diagnostic file

To view the contents of the diagnostic file:

{{< tabs group="os" >}}
{{< tab name="Windows" >}}

1. Unzip the file. In PowerShell, copy and paste the path to the diagnostics file into the following command and then run it. It should be similar to the following example:

   ```powershell
   $ Expand-Archive -LiteralPath "C:\Users\testUser\AppData\Local\Temp\5DE9978A-3848-429E-8776-950FC869186F\20230607101602.zip" -DestinationPath "C:\Users\testuser\AppData\Local\Temp\5DE9978A-3848-429E-8776-950FC869186F\20230607101602"
   ```

2. Open the file in your preferred text editor. Run:

   ```powershell
   $ code <path-to-file>
   ```

{{< /tab >}}
{{< tab name="Mac" >}}

Run:

```console
$ open /tmp/<your-diagnostics-ID>.zip
```

{{< /tab >}}
{{< tab name="Linux" >}}

Run:

```console
$ unzip –l /tmp/<your-diagnostics-ID>.zip
```

{{< /tab >}}
{{< /tabs >}}

## Use your diagnostics ID to get help

If you have a paid Docker subscription, select **Contact support**. This opens the Docker Desktop support form. Fill in the information required and add your diagnostic ID to the **Diagnostics ID field**. Then, select **Submit ticket** to request Docker Desktop support.

> [!NOTE]
>
> You must be signed in to Docker Desktop to access the support form. For information on what's covered as part of Docker Desktop support, see [Support](/manuals/support/_index.md).

If you don't have a paid Docker subscription, select **Report a Bug** from the app, or open a new [Docker Desktop issue on GitHub](https://github.com/docker/desktop-feedback). Complete the information required and ensure you add your diagnostic ID.

### Self-diagnose tool

> [!IMPORTANT]
>
> This tool has been deprecated.
