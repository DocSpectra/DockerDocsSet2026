---
title: "Connect a native Node.js app to Kafka"
description: "Connect a native Node.js app to Kafka"
---

## Setup and context

[Start Kafka](kafka-start.md).

[Set up the sample project](kafka-project.md).

[Port publishing](/get-started/docker-concepts/running-containers/publishing-ports.md).

## Connecting to Kafka from a non-containerized app

Now that you’ve shown you can connect to the Kafka instance from a command line, it’s time to connect to the cluster from an application. In this example, you will use a simple Node project that uses the [KafkaJS](https://github.com/tulios/kafkajs) library.

Since the cluster is running locally and is exposed at port 9092, the app can connect to the cluster at localhost:9092 (since it’s running natively and not in a container right now). Once connected, this sample app will log messages it consumes from the `demo` topic. Additionally, when it runs in development mode, it will also create the topic if it isn’t found.

1. If you don’t have the Kafka cluster running from the previous step, run the following command to start a Kafka instance:

   ```console
   $ docker run -d --name=kafka -p 9092:9092 apache/kafka
   ```

2. [Set up the Kafka Node.js sample project](kafka-project.md).

3. Start the application using `yarn dev`. This will set the `NODE_ENV` environment variable to `development` and use `nodemon` to watch for file changes.

   ```console
   $ yarn dev
   ```

4. With the application now running, it will log received messages to the console. In a new terminal, publish a few messages using the following command:

   ```console
   $ docker exec -ti kafka /opt/kafka/bin/kafka-console-producer.sh --bootstrap-server :9092 --topic demo
   ```

   And then send a message to the cluster:

   ```plaintext
   Test message
   ```

   Remember to press `ctrl+c` when you’re done to stop producing messages.
