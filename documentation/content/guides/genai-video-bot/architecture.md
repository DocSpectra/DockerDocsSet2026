---
title: Video bot architecture and technologies
description: Services and technologies used by the video transcription and chat sample.
---

## Explore the application architecture

The following image shows the application's high-level service architecture, which includes:

- yt-whisper: A local service, ran by Docker Compose, that interacts with the
  remote OpenAI and Pinecone services.
- dockerbot: A local service, ran by Docker Compose, that interacts with the
  remote OpenAI and Pinecone services.
- OpenAI: A remote third-party service.
- Pinecone: A remote third-party service.

![Application architecture diagram](images/architecture.webp)

## Explore the technologies used and their role

### Docker and Docker Compose

The application uses Docker to run the application in containers, providing a
consistent and isolated environment for running it. This means the application
will operate as intended within its Docker containers, regardless of the
underlying system differences. To learn more about Docker, see the [Getting started overview](/get-started/introduction/_index.md).

Docker Compose is a tool for defining and running multi-container applications.
Compose makes it easy to run this application with a single command, `docker
compose up`. For more details, see the [Compose overview](/manuals/compose/_index.md).

### OpenAI API

The OpenAI API provides an LLM service that's known for its cutting-edge AI and
machine learning technologies. In this application, OpenAI's technology is used
to generate transcriptions from audio (using the Whisper model) and to create
embeddings for text data, as well as to generate responses to user queries
(using GPT and chat completions). For more details, see
[openai.com](https://openai.com/product).

### Whisper

Whisper is an automatic speech recognition system developed by OpenAI, designed
to transcribe spoken language into text. In this application, Whisper is used to
transcribe the audio from YouTube videos into text, enabling further processing
and analysis of the video content. For more details, see [Introducing Whisper](https://openai.com/research/whisper).

### Embeddings

Embeddings are numerical representations of text or other data types, which
capture their meaning in a way that can be processed by machine learning
algorithms. In this application, embeddings are used to convert video
transcriptions into a vector format that can be queried and analyzed for
relevance to user input, facilitating efficient search and response generation
in the application. For more details, see OpenAI's
[Embeddings](https://platform.openai.com/docs/guides/embeddings) documentation.

![Embedding diagram](images/embeddings.webp)

### Chat completions

Chat completion, as utilized in this application through OpenAI's API, refers to
the generation of conversational responses based on a given context or prompt.
In the application, it is used to provide intelligent, context-aware answers to
user queries by processing and integrating information from video transcriptions
and other inputs, enhancing the chatbot's interactive capabilities. For more
details, see OpenAI's
[Chat Completions API](https://platform.openai.com/docs/guides/text-generation) documentation.

### Pinecone

Pinecone is a vector database service optimized for similarity search, used for
building and deploying large-scale vector search applications. In this
application, Pinecone is employed to store and retrieve the embeddings of video
transcriptions, enabling efficient and relevant search functionality within the
application based on user queries. For more details, see
[pincone.io](https://www.pinecone.io/).

### Retrieval-Augmented Generation

Retrieval-Augmented Generation (RAG) is a technique that combines information
retrieval with a language model to generate responses based on retrieved
documents or data. In RAG, the system retrieves relevant information (in this
case, via embeddings from video transcriptions) and then uses a language model
to generate responses based on this retrieved data. For more details, see
OpenAI's cookbook for
[Retrieval Augmented Generative Question Answering with Pinecone](https://cookbook.openai.com/examples/vector_databases/pinecone/gen_qa).

## RAG context

See [RAG, embeddings, and graph databases](../rag-concepts.md).
