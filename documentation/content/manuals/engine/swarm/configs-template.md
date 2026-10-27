---
title: Use a templated config
---

## Prerequisites and caveats

See [Docker config lifecycle and platform support](configs-context.md), including example scope and Windows differences.

## Steps

To create a configuration in which the content will be generated using a
template engine, use the `--template-driver` parameter and specify the engine
name as its argument. The template will be rendered when container is created.

1.  Save the following into a new file `index.html.tmpl`.

    ```html
    <html lang="en">
      <head><title>Hello Docker</title></head>
      <body>
        <p>Hello {{ env "HELLO" }}! I'm service {{ .Service.Name }}.</p>
      </body>
    </html>
    ```

2.  Save the `index.html.tmpl` file as a swarm config named `homepage`. Provide
    parameter `--template-driver` and specify `golang` as template engine.

    ```console
    $ docker config create --template-driver golang homepage index.html.tmpl
    ```

3.  Create a service that runs Nginx and has access to the environment variable
    HELLO and to the config.

    ```console
    $ docker service create \
         --name hello-template \
         --env HELLO="Docker" \
         --config source=homepage,target=/usr/share/nginx/html/index.html \
         --publish published=3000,target=80 \
         nginx:alpine
    ```

4.  Verify that the service is operational: you can reach the Nginx server, and
    that the correct output is being served.

    ```console
    $ curl http://0.0.0.0:3000

    <html lang="en">
      <head><title>Hello Docker</title></head>
      <body>
        <p>Hello Docker! I'm service hello-template.</p>
      </body>
    </html>
    ```
