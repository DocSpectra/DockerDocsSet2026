---
title: Build a static React image with Nginx
---

## Shared context and procedure

- [Multi-stage build context](/get-started/docker-concepts/building-images/multi-stage-builds.md)
- [Multi-stage build procedure](/manuals/build/building/multi-stage.md)

## Scope

> [!Tips]
> This React example is for illustration purposes. The getting-started todo app is a `Node.js` backend application, not a React frontend.

## React example

When building React applications, you need a Node environment to compile the JS code (typically JSX), SASS stylesheets,
and more into static HTML, JS, and CSS. If you aren't doing server-side rendering, you don't even need a Node environment
for your production build. You can ship the static resources in a static nginx container.

```dockerfile
# syntax=docker/dockerfile:1
FROM node:24-alpine AS build
WORKDIR /app
COPY package* ./
RUN npm install
COPY public ./public
COPY src ./src
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html
```

In the previous Dockerfile example, it uses the `node:24-alpine` image to perform the build (maximizing layer caching) and then copies the output
into an nginx container.
