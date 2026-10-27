---
title: Build a Maven application for Tomcat
---

## Shared context and procedure

- [Multi-stage build context](/get-started/docker-concepts/building-images/multi-stage-builds.md)
- [Multi-stage build procedure](/manuals/build/building/multi-stage.md)

## Maven/Tomcat example

When building Java-based applications, you need a JDK to compile the source code to Java bytecode. However,
that JDK isn't needed in production. Also, you might be using tools like Maven or Gradle to help build the app.
Those also aren't needed in your final image. Multi-stage builds help.

```dockerfile
# syntax=docker/dockerfile:1
FROM maven AS build
WORKDIR /app
COPY . .
RUN mvn package

FROM tomcat
COPY --from=build /app/target/file.war /usr/local/tomcat/webapps 
```

In this example, you use one stage (called `build`) to perform the actual Java build using Maven. In the second
stage (starting at `FROM tomcat`), you copy in files from the `build` stage. The final image is only the last stage
being created, which can be overridden using the `--target` flag.
