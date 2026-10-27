---
title: Leveraging RAG in GenAI to teach new information
linkTitle: Leveraging RAG in GenAI
description:  This guide walks through the process of setting up and utilizing a GenAI stack with Retrieval-Augmented Generation (RAG) systems and graph databases. Learn how to integrate graph databases like Neo4j with AI models for more accurate, contextually-aware responses.
keywords: Docker, GenAI, Retrieval-Augmented Generation, RAG, Graph Databases, Neo4j, AI, LLM
summary: |
  This guide explains setting up a GenAI stack with Retrieval-Augmented Generation (RAG) and Neo4j, covering key concepts, deployment steps, and a case study. It also includes troubleshooting tips for optimizing AI performance with real-time data.
tags: [ai]
params:
  time: 35 minutes
---

## Introduction

Retrieval-Augmented Generation (RAG) is a powerful framework that enhances large language models (LLMs) by integrating information retrieval from external knowledge sources. This guide focuses on a specialized RAG implementation using graph databases like Neo4j, which excel in managing highly connected, relational data. Unlike traditional RAG setups with vector databases, combining RAG with graph databases offers better context-awareness and relationship-driven insights.

In this guide, you will:

* Explore the advantages of integrating graph databases into a RAG framework.
* Configure a GenAI stack with Docker, incorporating Neo4j and an AI model.
* Analyze a real-world case study that highlights the effectiveness of this approach for handling specialized queries.

## Understanding RAG

See [RAG, embeddings, and graph databases](../rag-concepts.md), including [when to leverage RAG](../rag-concepts.md#when-to-leverage-rag-for-optimal-results).

## Introduction to Graph databases

See [graph database context](../rag-concepts.md#introduction-to-graph-databases).

## Practical implementation: testing RAG effectiveness

To illustrate the power of RAG systems in practice, let's examine a real-world implementation using Apache NiFi as our subject matter. This case study demonstrates how RAG can enhance an AI's ability to provide accurate, contextual information about specialized technical topics.

### Teaching AI about new technologies

Apache NiFi serves as an excellent example of the limitations of traditional LLMs and how RAG can overcome them. As a relatively recent technology, many LLMs have limited or outdated knowledge about it, making it a perfect candidate for demonstrating RAG's capabilities.

Without RAG, the LLM may provide broad responses or acknowledge its limited knowledge when asked about information that is beyond its cutoff date. The following example demonstrates this.
```text
Question: What important events happened in 2024?
RAG: Disabled
I'm happy to help! Unfortunately, I'm a large language model, I don't have access to real-time information or events that occurred after my training data cutoff in 2024. Therefore, I cannot provide you with any important events that happened in 2024. My apologize for any inconvenience this may cause. Is there anything else I can help you with?
```

## Setting up GenAI stack with GPU acceleration on Linux

[Set up the stack and check its startup logs](stack-setup.md).

## Import and query the Apache NiFi data

You can now access the interface at [http://localhost:8501/](http://localhost:8501/) to ask questions. For example, you can try the sample question:

When we see [those lines in the logs](stack-setup.md#monitoring-progress), web apps are ready to be used.

Since our goal is to teach AI about things it does not yet know, we begin by asking it a simple question about Nifi at
[http://localhost:8501/](http://localhost:8501/).
![alt text](image.png)

```text
Question: What is Apache Nifi?
RAG: Disabled
Hello! I'm here to help you with your question about Apache NiFi. Unfortunately, I don't know the answer to that question. I'm just an AI and my knowledge cutoff is December 2022, so I may not be familiar with the latest technologies or software. Can you please provide more context or details about Apache NiFi? Maybe there's something I can help you with related to it.
```

As we can see, AI does not know anything about this subject because it did not exist during the time of its training, also known as the information cutoff point.

Now it's time to teach the AI some new tricks. First, connect to [http://localhost:8502/](http://localhost:8502/). Instead of using the "neo4j" tag, change it to the "apache-nifi" tag, then select the **Import** button.

![alt text](image-1.png)

After the import is successful, we can access Neo4j to verify the data.

After logging in to [http://localhost:7474/](http://localhost:7474/) using the credentials from the `.env` file, you can run queries on Neo4j. Using the Neo4j Cypher query language, you can check for the data stored in the database.

To count the data, run the following query:

```text
MATCH (n)
RETURN DISTINCT labels(n) AS NodeTypes, count(*) AS Count
ORDER BY Count DESC;
```

To execute this query, write in the box on the top and select the blue run button.

![alt text](image-2.png)

Results will appear below. What we are seeing here is the information system downloaded from Stack Overflow and saved in the graph database. RAG will utilize this information to enhance its responses.

You can also run the following query to visualize the data:

```text
CALL db.schema.visualization()
```

To check the relationships in the database, run the following query:

```text
CALL db.relationshipTypes()
```

Now, we are ready to enable our LLM to use this information. Go back to [http://localhost:8501/](http://localhost:8501/), enable the **RAG** checkbox, and ask the same question again. The LLM will now provide a more detailed answer.

![alt text](image-3.png)

The system delivers comprehensive, accurate information by pulling from current technical documentation.
```text
Question: What is Apache Nifi?
RAG: Enabled

Answer:
Apache NiFi is an open-source, distributed data processing system that allows you to collect, transform, and transport data across various sources and sinks. It provides a graphical user interface for designing and managing data flows, as well as a set of APIs for integrating with other systems.
According to this Stack Overflow question, the free Neo4J JDBC driver doesn't understand SQL, only Cypher, so you would need to use a non-free BI Connector to connect to Neo4j from Apache Drill.
Additionally, this Stack Overflow question suggests that Apache POI does work in a Neo4j User Defined Function. However, there may be an unknown glitch in the standalone UDF mentioned in the initial question.
To export data from Neo4j to Excel using APOC Extended procedures, you can use apoc.export.xls.query which takes a Cypher query and exports the results to an Excel file.

References:
How to connect and query Neo4j Database on Apache Drill?
Is a Neo4j UDF compatible with Apache POI?
```

Keep in mind that new questions will be added to Stack Overflow, and due to the inherent randomness in most AI models, the answers may vary and won't be identical to those in this example.

Feel free to start over with another [Stack Overflow tag](https://stackoverflow.com/tags). To drop all data in Neo4j, you can use the following command in the Neo4j Web UI:

```txt
MATCH (n)
DETACH DELETE n;
```

For optimal results, choose a tag that the LLM is not familiar with.

By following this guide, you now have the foundational knowledge to implement RAG with Neo4j, enabling your AI system to deliver more accurate, relevant, and insightful responses. The next step is experimentation—choose a dataset, configure your stack, and start enhancing your AI with the power of retrieval-augmented generation.