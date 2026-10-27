---
title: Share website files with an httpd container
keywords: concepts, images, container, docker desktop
description: This concept page will teach you the various storage options available in Docker and their common usage.
---

## Before you begin

[Sharing local files with containers](/get-started/docker-concepts/running-containers/sharing-local-files.md).

- [Mount syntax and permission caveats](/get-started/docker-concepts/running-containers/sharing-local-files.md#sharing-files-between-a-host-and-container)

## Try it out

In this hands-on guide, you’ll practice how to create and use a bind mount to share files between a host and a container.

### Run a container

1. [Download and install](/get-started/get-docker/) Docker Desktop.

2. Start a container using the [httpd](https://hub.docker.com/_/httpd) image with the following command:

   ```console
   $ docker run -d -p 8080:80 --name my_site httpd:2.4
   ```

   This will start the `httpd` service in the background, and publish the webpage to port `8080` on the host.

3. Open the browser and access [http://localhost:8080](http://localhost:8080) or use the curl command to verify if it's working fine or not.

    ```console
    $ curl localhost:8080
    ```


### Use a bind mount

Using a bind mount, you can map the configuration file on your host computer to a specific location within the container. In this example, you’ll see how to change the look and feel of the webpage by using bind mount:

1. Delete the existing container by using the Docker Desktop Dashboard:

   ![A screenshot of Docker Desktop Dashboard showing how to delete the httpd container](/get-started/docker-concepts/running-containers/images/delete-httpd-container.webp?border=true)


2. Create a new directory called `public_html` on your host system.

    ```console
    $ mkdir public_html
    ```

3. Navigate into the newly created directory `public_html` and create a file called `index.html` with the following content. This is a basic HTML document that creates a simple webpage that welcomes you with a friendly whale.

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <title> My Website with a Whale & Docker!</title>
    </head>
    <body>
    <h1>Whalecome!!</h1>
    <p>Look! There's a friendly whale greeting you!</p>
    <pre id="docker-art">
       ##         .
      ## ## ##        ==
     ## ## ## ## ##    ===
     /"""""""""""""""""\___/ ===
   {                       /  ===-
   \______ O           __/
    \    \         __/
     \____\_______/

    Hello from Docker!
    </pre>
    </body>
    </html>
    ```

4. It's time to run the container. The `--mount` and `-v` examples produce the same result. You can't run them both unless you remove the `my_site` container after running the first one.

   {{< tabs >}}
   {{< tab name="`-v`" >}}

   ```console
   $ docker run -d --name my_site -p 8080:80 -v .:/usr/local/apache2/htdocs/ httpd:2.4
   ```

   {{< /tab >}}
   {{< tab name="`--mount`" >}}

   ```console
   $ docker run -d --name my_site -p 8080:80 --mount type=bind,source=./,target=/usr/local/apache2/htdocs/ httpd:2.4
   ```

   {{< /tab >}}
   {{< /tabs >}}


   > [!TIP]  
   > When using the `-v` or `--mount` flag in Windows PowerShell, you need to provide the absolute path to your directory instead of just `./`. This is because PowerShell handles relative paths differently from bash (commonly used in Mac and Linux environments).    



   With everything now up and running, you should be able to access the site via [http://localhost:8080](http://localhost:8080) and find a new webpage that welcomes you with a friendly whale.


### Access the file on the Docker Desktop Dashboard

1. You can view the mounted files inside a container by selecting the container's **Files** tab and then selecting a file inside the `/usr/local/apache2/htdocs/` directory. Then, select **Open file editor**.


   ![A screenshot of Docker Desktop Dashboard showing the mounted files inside the a container](/get-started/docker-concepts/running-containers/images/mounted-files.webp?border=true)

2. Delete the file on the host and verify the file is also deleted in the container. You will find that the files no longer exist under **Files** in the Docker Desktop Dashboard.


   ![A screenshot of Docker Desktop Dashboard showing the deleted files inside the a container](/get-started/docker-concepts/running-containers/images/deleted-files.webp?border=true)


3. Recreate the HTML file on the host system and see that file re-appears under the **Files** tab under **Containers** on the Docker Desktop Dashboard. By now, you will be able to access the site too.



### Stop your container

The container continues to run until you stop it.

1. Go to the **Containers** view in the Docker Desktop Dashboard.

2. Locate the container you'd like to stop.

3. Select the **Stop** action in the Actions column.

## Next steps

Now that you have learned about sharing local files with containers, it’s time to learn about multi-container applications.

{{< button text="Multi-container applications" url="/get-started/docker-concepts/running-containers/multi-container-applications" >}}
