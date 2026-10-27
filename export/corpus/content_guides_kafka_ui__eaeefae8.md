---
title: "Visualize a Kafka cluster with Kafbat UI"
description: "Visualize a Kafka cluster with Kafbat UI"
---

## Setup and context

[Kafka for containers and native apps](kafka-container-app.md).

[Kafka listeners and advertised listeners](kafka-listeners.md).

[Networking in Compose](/manuals/compose/how-tos/networking.md).

## Adding cluster visualization

Once you start using containers in your development environment, you start to realize the ease of adding additional services that are solely focused on helping development, such as visualizers and other supporting services. Since you have Kafka running, it might be helpful to visualize what’s going on in the Kafka cluster. To do so, you can run the [Kafbat UI web application](https://github.com/kafbat/kafka-ui).

To add it to your own project (it’s already in the demo application), you only need to add the following configuration to your Compose file:

```yaml
services:
  kafka-ui:
    image: kafbat/kafka-ui:main
    ports:
      - 8080:8080
    environment:
      DYNAMIC_CONFIG_ENABLED: "true"
      KAFKA_CLUSTERS_0_NAME: local
      KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS: kafka:9093
    depends_on:
      - kafka
```

Then, once the Compose stack starts, you can open your browser to [http://localhost:8080](http://localhost:8080) and navigate around to view additional details about the cluster, check on consumers, publish test messages, and more.
