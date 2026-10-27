---
title: Set up the GenAI Stack on Linux
description: GPU and CPU setup, startup, and log checks for the GenAI Stack.
---

## Setting up GenAI stack with GPU acceleration on Linux

To set up and run the GenAI stack on a Linux host, execute one of the following commands, either for GPU or CPU powered:

### GPU powered

```bash
git clone https://github.com/docker/genai-stack
docker compose --profile linux-gpu up -d
mv env.example .env
nano .env
```
In the `.env` file, make sure following lines are commented out. Set your own credentials for security

  ```txt
    NEO4J_URI=neo4j://database:7687
    NEO4J_USERNAME=neo4j
    NEO4J_PASSWORD=password
    OLLAMA_BASE_URL=http://llm-gpu:11434
  ```

### CPU powered

```bash
git clone https://github.com/docker/genai-stack
docker compose --profile linux up -d
mv env.example .env
nano .env
```
In the `.env` file, make sure following lines are commented out. Set your own credentials for security

  ```txt
    NEO4J_URI=neo4j://database:7687
    NEO4J_USERNAME=neo4j
    NEO4J_PASSWORD=password
    OLLAMA_BASE_URL=http://llm:11434
  ```

### Setting up on other platforms

For instructions on how to set up the stack on other platforms, refer to [this page](https://github.com/docker/genai-stack).

### Initial startup

The first startup may take some time because the system needs to download a large language model.

### Monitoring progress

We can monitor the download and initialization progress by viewing the logs. Run the following command to view the logs:

```bash
docker compose logs
```

Wait for specific lines in the logs indicating that the download is complete and the stack is ready. These lines typically confirm successful setup and initialization.

  ```text
    pull-model-1 exited with code 0
    database-1    | 2024-12-29 09:35:53.269+0000 INFO  Started.
    pdf_bot-1     |   You can now view your Streamlit app in your browser.
    loader-1      |   You can now view your Streamlit app in your browser.
    bot-1         |   You can now view your Streamlit app in your browser.
  ```

