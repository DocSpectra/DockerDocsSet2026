---
title: What is Docker Compose?
weight: 40
keywords: concepts, build, images, container, docker desktop
aliases:
 - /guides/walkthroughs/multi-container-apps/
 - /guides/docker-concepts/the-basics/what-is-docker-compose/
---

{{< youtube-embed xhcUIK4fGtY >}}

## Explanation

If you've been following the guides so far, you've been working with single container applications. But, now you're wanting to do something more complicated - run databases, message queues, caches, or a variety of other services. Do you install everything in a single container? Run multiple containers? If you run multiple, how do you connect them all together?

One best practice for containers is that each container should do one thing and do it well. While there are exceptions to this rule, avoid the tendency to have one container do multiple things.

You can use multiple `docker run` commands to start multiple containers. But, you'll soon realize you'll need to manage networks, all of the flags needed to connect containers to those networks, and more. And when you're done, cleanup is a little more complicated.

With Docker Compose, you can define all of your containers and their configurations in a single YAML file. If you include this file in your code repository, anyone that clones your repository can get up and running with a single command.

It's important to understand that Compose is a declarative tool - you simply define it and go. You don't always need to recreate everything from scratch. If you make a change, run `docker compose up` again and Compose will reconcile the changes in your file and apply them intelligently.

> **Dockerfile versus Compose file**
>
> A Dockerfile provides instructions to build a container image while a Compose file defines your running containers. Quite often, a Compose file references a Dockerfile to build an image to use for a particular service.

## Share a version-controlled application stack

[Docker Compose](/manuals/compose/_index.md) is a tool that helps you define and
share multi-container applications. With Compose, you can create a YAML file to define the services
and with a single command, you can spin everything up or tear it all down.

The big advantage of using Compose is you can define your application stack in a file, keep it at the root of
your project repository (it's now version controlled), and easily enable someone else to contribute to your project.
Someone would only need to clone your repository and start the app using Compose. In fact, you might see quite a few projects
on GitHub/GitLab doing exactly this now.

## Additional resources

This page was a brief introduction to Compose. In the following resources, you can dive deeper into Compose and how to write Compose files.


* [Overview of Docker Compose](/compose/)
* [Overview of Docker Compose CLI](/reference/cli/docker/compose/)
* [How Compose works](/compose/intro/compose-application-model/)
