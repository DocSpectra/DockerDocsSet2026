---
title: "Traefik sample application and routing layout"
description: "Traefik sample application and routing layout"
---

Now that you’ve experienced Traefik, it’s time to try using it in a development environment. In this example, you will use a sample application that has a split frontend and backend. This app stack has the following configuration:

1. All requests to /api to go to the API service
2. All other requests to localhost go to the frontend client
3. Since the app uses MySQL, db.localhost should provide phpMyAdmin to make it easy to access the database during development

![Architecture diagram showing Traefik routing requests to other containers based on the path of the request](./images/traefik-in-development.webp)

The application can be accessed on GitHub at [dockersamples/easy-http-routing-with-traefik](https://github.com/dockersamples/easy-http-routing-with-traefik).
