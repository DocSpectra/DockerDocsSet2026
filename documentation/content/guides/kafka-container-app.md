---
title: "Connect Kafka to containers and native apps"
description: "Connect Kafka to containers and native apps"
---

## Setup and context

[Set up the sample project](kafka-project.md).

[Kafka versions and image choices](kafka-images.md).

[Kafka listeners and advertised listeners](kafka-listeners.md).

[Networking in Compose](/manuals/compose/how-tos/networking.md).

## Connecting to Kafka from both containers and native apps

Now that you have an application connecting to Kafka through its exposed port, it’s time to explore what changes are needed to connect to Kafka from another container. To do so, you will now run the application out of a container instead of natively.

But before you do that, it’s important to understand how Kafka listeners work and how those listeners help clients connect.

### Understanding Kafka listeners

[Kafka listeners and advertised listeners](kafka-listeners.md).

### Defining the listeners

To help this make sense, let’s look at how Kafka needs to be configured to support two connection opportunities:

1. Host connections (those coming through the host’s mapped port) - these will need to connect using localhost
2. Docker connections (those coming from inside the Docker networks) - these can not connect using localhost, but the network alias (or DNS address) of the Kafka service

Since there are two different methods clients need to connect, two different listeners are required - `HOST` and `DOCKER`. The `HOST` listener will tell clients to connect using localhost:9092, while the `DOCKER` listener will inform clients to connect using `kafka:9093`. Notice this means Kafka is listening on both ports 9092 and 9093. But, only the host listener needs to be exposed to the host.

![Diagram showing the DOCKER and HOST listeners and how they are exposed to the host and Docker networks](images/kafka-1.webp)

In order to set this up, the `compose.yaml` for Kafka needs some additional configuration. Once you start overriding some of the defaults, you also need to specify a few other options in order for KRaft mode to work.

```yaml
services:
  kafka:
    image: apache/kafka-native
    ports:
      - "9092:9092"
    environment:
      # Configure listeners for both docker and host communication
      KAFKA_LISTENERS: CONTROLLER://localhost:9091,HOST://0.0.0.0:9092,DOCKER://0.0.0.0:9093
      KAFKA_ADVERTISED_LISTENERS: HOST://localhost:9092,DOCKER://kafka:9093
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: CONTROLLER:PLAINTEXT,DOCKER:PLAINTEXT,HOST:PLAINTEXT

      # Settings required for KRaft mode
      KAFKA_NODE_ID: 1
      KAFKA_PROCESS_ROLES: broker,controller
      KAFKA_CONTROLLER_LISTENER_NAMES: CONTROLLER
      KAFKA_CONTROLLER_QUORUM_VOTERS: 1@localhost:9091

      # Listener to use for broker-to-broker communication
      KAFKA_INTER_BROKER_LISTENER_NAME: DOCKER

      # Required for a single node cluster
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
```

Give it a try using the steps below.

1. If you have the Node app running from the previous step, go ahead and stop it by pressing `ctrl+c` in the terminal.

2. If you have the Kafka cluster running from the previous section, go ahead and stop that container using the following command:

   ```console
   $ docker rm -f kafka
   ```

3. Start the Compose stack by running the following command at the root of the cloned project directory:

   ```console
   $ docker compose up
   ```

   After a moment, the application will be up and running.

4. In the stack is another service that can be used to publish messages. Open it by going to [http://localhost:3000](http://localhost:3000). As you type in a message and submit the form, you should see the log message of the message being received by the app.

   This helps demonstrate how a containerized approach makes it easy to add additional services to help test and troubleshoot your application.
