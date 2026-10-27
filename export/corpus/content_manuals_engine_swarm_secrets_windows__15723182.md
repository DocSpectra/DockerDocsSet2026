---
title: Use a secret with IIS on Windows
---

## Prerequisites and caveats

See [Docker secret lifecycle and platform support](secrets-context.md), including example scope and Windows differences.

## Steps

This is a very simple example which shows how to use secrets with a Microsoft
IIS service running on Docker for Windows running Windows containers on
Microsoft Windows 10. It is a naive example that stores the webpage in a secret.

This example assumes that you have PowerShell installed.

1.  Save the following into a new file `index.html`.

    ```html
    <html lang="en">
      <head><title>Hello Docker</title></head>
      <body>
        <p>Hello Docker! You have deployed a HTML page.</p>
      </body>
    </html>
    ```

2.  If you have not already done so, initialize or join the swarm.

    ```console
    > docker swarm init
    ```

3.  Save the `index.html` file as a swarm secret named `homepage`.

    ```console
    > docker secret create homepage index.html
    ```

4.  Create an IIS service and grant it access to the `homepage` secret.

    ```console
    > docker service create `
        --name my-iis `
        --publish published=8000,target=8000 `
        --secret src=homepage,target="\inetpub\wwwroot\index.html" `
        microsoft/iis:nanoserver
    ```

    > [!NOTE]
    >
    > There is technically no reason to use secrets for this
    > example; [configs](configs.md) are a better fit. This example is
    > for illustration only.

5.  Access the IIS service at `http://localhost:8000/`. It should serve
    the HTML content from the first step.

6.  Remove the service and the secret.

    ```console
    > docker service rm my-iis
    > docker secret rm homepage
    > docker image remove secret-test
    ```
