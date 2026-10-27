---
title: GenAI video transcription and chat
linkTitle: Video transcription and chat
description: Explore a generative AI video analysis app that uses Docker, OpenAI, and Pinecone.
keywords: python, generative ai, genai, llm, whisper, pinecone, openai, whisper
summary: |
  Learn how to build and deploy a generative AI video analysis and
  transcription bot using Docker.
tags: [ai]
aliases:
  - /guides/use-case/genai-video-bot/
params:
  time: 20 minutes
---

## Overview

This guide presents a project on video transcription and analysis using a set of
technologies related to the
[GenAI Stack](https://www.docker.com/blog/introducing-a-new-genai-stack/).

The project showcases the following technologies:

- [Docker and Docker Compose](architecture.md#docker-and-docker-compose)
- [OpenAI](architecture.md#openai-api)
- [Whisper](architecture.md#whisper)
- [Embeddings](architecture.md#embeddings)
- [Chat completions](architecture.md#chat-completions)
- [Pinecone](architecture.md#pinecone)
- [Retrieval-Augmented Generation](architecture.md#retrieval-augmented-generation)

> **Acknowledgment**
>
> This guide is a community contribution. Docker would like to thank
> [David Cardozo](https://www.davidcardozo.com/) for his contribution
> to this guide.

## Prerequisites

- You have an [OpenAI API Key](https://platform.openai.com/api-keys).

  > [!NOTE]
  >
  > OpenAI is a third-party hosted service and [charges](https://openai.com/pricing) may apply.

- You have a [Pinecone API Key](https://app.pinecone.io/).
- You have installed the latest version of [Docker Desktop](/get-started/get-docker.md). Docker adds new features regularly and some parts of this guide may work only with the latest version of Docker Desktop.
- Review the [Git client prerequisite](../prerequisites.md#git-client).

## About the application

The application is a chatbot that can answer questions from a video. In
addition, it provides timestamps from the video that can help you find the sources used to answer your question.

## Get and run the application

1. Clone the sample application's repository. In a terminal, run the following
   command.

   ```console
   $ git clone https://github.com/Davidnet/docker-genai.git
   ```

   The project contains the following directories and files:

   ```text
   ├── docker-genai/
   │ ├── docker-bot/
   │ ├── yt-whisper/
   │ ├── .env.example
   │ ├── .gitignore
   │ ├── LICENSE
   │ ├── README.md
   │ └── docker-compose.yaml
   ```

2. Specify your API keys. In the `docker-genai` directory, create a text file
   called `.env` and specify your API keys inside. The following is the contents of the `.env.example` file that you can refer to as an example.

   ```text
   #----------------------------------------------------------------------------
   # OpenAI
   #----------------------------------------------------------------------------
   OPENAI_TOKEN=your-api-key # Replace your-api-key with your personal API key

   #----------------------------------------------------------------------------
   # Pinecone
   #----------------------------------------------------------------------------
   PINECONE_TOKEN=your-api-key # Replace your-api-key with your personal API key
   ```

3. Build and run the application. In a terminal, change directory to your
   `docker-genai` directory and run the following command.

   ```console
   $ docker compose up --build
   ```

   Docker Compose builds and runs the application based on the services defined
   in the `docker-compose.yaml` file. When the application is running, you'll
   see the logs of 2 services in the terminal.

   In the logs, you'll see the services are exposed on ports `8503` and `8504`.
   The two services are complimentary to each other.

   The `yt-whisper` service is running on port `8503`. This service feeds the
   Pinecone database with videos that you want to archive in your knowledge
   database. The following section explores this service.

## Using the yt-whisper service

The yt-whisper service is a YouTube video processing service that uses the OpenAI
Whisper model to generate transcriptions of videos and stores them in a Pinecone
database. The following steps show how to use the service.

1. Open a browser and access the yt-whisper service at [http://localhost:8503](http://localhost:8503).
2. Once the application appears, in the **Youtube URL** field specify a Youtube video URL
   and select **Submit**. The following example uses
   [https://www.youtube.com/watch?v=yaQZFhrW0fU](https://www.youtube.com/watch?v=yaQZFhrW0fU).

   ![Submitting a video in the yt-whisper service](images/yt-whisper.webp)

   The yt-whisper service downloads the audio of the video, uses Whisper to
   transcribe it into a WebVTT (`*.vtt`) format (which you can download), then
   uses the text-embedding-3-small model to create embeddings, and finally
   uploads those embeddings in to the Pinecone database.

   After processing the video, a video list appears in the web app that informs
   you which videos have been indexed in Pinecone. It also provides a button to
   download the transcript.

   ![A processed video in the yt-whisper service](images/yt-whisper-2.webp)

   You can now access the dockerbot service on port `8504` and ask questions
   about the videos.

## Using the dockerbot service

The dockerbot service is a question-answering service that leverages both the
Pinecone database and an AI model to provide responses. The following steps show
how to use the service.

> [!NOTE]
>
> You must process at least one video via the
> [yt-whisper service](#using-the-yt-whisper-service) before using
> the dockerbot service.

1. Open a browser and access the service at
   [http://localhost:8504](http://localhost:8504).

2. In the **What do you want to know about your videos?** text box, ask the
   Dockerbot a question about a video that was processed by the yt-whisper
   service. The following example asks the question, "What is a sugar cookie?".
   The answer to that question exists in the video processed in the previous
   example,
   [https://www.youtube.com/watch?v=yaQZFhrW0fU](https://www.youtube.com/watch?v=yaQZFhrW0fU).

   ![Asking a question to the Dockerbot](images/bot.webp)

   In this example, the Dockerbot answers the question and
   provides links to the video with timestamps, which may contain more
   information about the answer.

   The dockerbot service takes the question, turns it into an embedding using
   the text-embedding-3-small model, queries the Pinecone database to find
   similar embeddings, and then passes that context into the gpt-4-turbo-preview
   to generate an answer.

3. Select the first link to see what information it provides. Based on the
   previous example, select
   [https://www.youtube.com/watch?v=yaQZFhrW0fU&t=553s](https://www.youtube.com/watch?v=yaQZFhrW0fU&t=553s).

   In the example link, you can see that the section of video perfectly answers
   the question, "What is a sugar cookie?".

## Explore the application architecture

See the [application architecture and technologies](architecture.md).

## Next steps

Explore how to [create a PDF bot application](/guides/genai-pdf-bot/_index.md) using
generative AI, or view more GenAI samples in the
[GenAI Stack](https://github.com/docker/genai-stack) repository.
