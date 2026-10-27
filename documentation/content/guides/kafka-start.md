---
title: "Start Kafka and exchange test messages"
description: "Start Kafka and exchange test messages"
---

## Prerequisites

[Docker Desktop](prerequisites.md#docker-desktop).

Basic knowledge of Kafka and Docker.

[Kafka versions and image choices](kafka-images.md).

[Port publishing](/get-started/docker-concepts/running-containers/publishing-ports.md).

## Launching Kafka

[Kafka versions and image choices](kafka-images.md).

### Starting Kafka

Start a basic Kafka cluster by doing the following steps. This example will launch a cluster, exposing port 9092 onto the host to let a native-running application to connect to it.

1. Start a Kafka container by running the following command:

   ```console
   $ docker run -d --name=kafka -p 9092:9092 apache/kafka
   ```

2. Once the image pulls, you’ll have a Kafka instance up and running within a second or two.

3. The apache/kafka image ships with several helpful scripts in the `/opt/kafka/bin` directory. Run the following command to verify the cluster is up and running and get its cluster ID:

   ```console
   $ docker exec -ti kafka /opt/kafka/bin/kafka-cluster.sh cluster-id --bootstrap-server :9092
   ```

   Doing so will produce output similar to the following:

   ```plaintext
   Cluster ID: 5L6g3nShT-eMCtK--X86sw
   ```

4. Create a sample topic and produce (or publish) a few messages by running the following command:

   ```console
   $ docker exec -ti kafka /opt/kafka/bin/kafka-console-producer.sh --bootstrap-server :9092 --topic demo
   ```

   After running, you can enter a message per line. For example, enter a few messages, one per line. A few examples might be:

   ```plaintext
   First message
   ```

   And

   ```plaintext
   Second message
   ```

   Press `enter` to send the last message and then press ctrl+c when you’re done. The messages will be published to Kafka.

5. Confirm the messages were published into the cluster by consuming the messages:

   ```console
   $ docker exec -ti kafka /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server :9092 --topic demo --from-beginning
   ```

   You should then see your messages in the output:

   ```plaintext
   First message
   Second message
   ```

   If you want, you can open another terminal and publish more messages and see them appear in the consumer.

   When you’re done, hit ctrl+c to stop consuming messages.

You have a locally running Kafka cluster and have validated you can connect to it.
