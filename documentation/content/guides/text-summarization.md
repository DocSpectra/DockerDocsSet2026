---
title: Build a text summarization app
linkTitle: Text summarization
keywords: nlp, natural language processing, text summarization, python, bert extractive summarizer
description: Learn how to build and run a text summarization application using Python, Bert Extractive Summarizer, and Docker.
summary: |
  This guide shows how to containerize text summarization models with Docker.
tags: [ai]
languages: [python]
aliases:
  - /guides/use-case/nlp/text-summarization/
params:
  time: 20 minutes
---

## Overview

In this guide, you'll learn how to build and run a text summarization
application. You'll build the application using Python with the Bert Extractive
Summarizer, and then set up the environment and run the application using
Docker.

The sample text summarization application uses the Bert Extractive Summarizer.
This tool utilizes the HuggingFace Pytorch transformers library to run
extractive summarizations. This works by first embedding the sentences, then
running a clustering algorithm, finding the sentences that are closest to the
cluster's centroids.

## Prerequisites

- You have installed the latest version of [Docker Desktop](/get-started/get-docker.md). Docker adds new features regularly and some parts of this guide may work only with the latest version of Docker Desktop.
- Review the [Git client prerequisite](prerequisites.md#git-client).

## Get the sample application

1. Open a terminal, and clone the sample application's repository using the
   following command.

   ```console
   $ git clone https://github.com/harsh4870/Docker-NLP.git
   ```

2. [Verify the sample files](nlp-sample-workflow.md#verify-the-sample-files).

## Explore the application code

The source code for the text summarization application is in the `Docker-NLP/04_text_summarization.py` file. Open `04_text_summarization.py` in a text or code editor to explore its contents in the following steps.

1. Import the required libraries.

   ```python
   from summarizer import Summarizer
   ```

   This line of code imports the `Summarizer` class from the `summarizer`
   package, essential for your text summarization application. The summarizer
   module implements the Bert Extractive Summarizer, leveraging the HuggingFace
   Pytorch transformers library, renowned in the NLP (Natural Language
   Processing) domain. This library offers access to pre-trained models like
   BERT, which revolutionized language understanding tasks, including text
   summarization.

   The BERT model, or Bidirectional Encoder Representations from Transformers,
   excels in understanding context in language, using a mechanism known as
   "attention" to determine the significance of words in a sentence. For
   summarization, the model embeds sentences and then uses a clustering
   algorithm to identify key sentences, those closest to the centroids of these
   clusters, effectively capturing the main ideas of the text.

2. Specify the main execution block.

   ```python
   if __name__ == "__main__":
   ```

   This Python idiom ensures that the following code block runs only if this
   script is the main program. It provides flexibility, allowing the script to
   function both as a standalone program and as an imported module.

3. Create an infinite loop for continuous input.

   ```python
      while True:
         input_text = input("Enter the text for summarization (type 'exit' to end): ")

         if input_text.lower() == 'exit':
            print("Exiting...")
            break
   ```

   An infinite loop continuously prompts you for text
   input, ensuring interactivity. The loop breaks when you type `exit`, allowing
   you to control the application flow effectively.

4. Create an instance of Summarizer.

   ```python
         bert_model = Summarizer()
   ```

   Here, you create an instance of the Summarizer class named `bert_model`. This
   instance is now ready to perform the summarization task using the BERT model,
   simplifying the complex processes of embedding sentences and clustering into
   an accessible interface.

5. Generate and print a summary.

   ```python
   summary = bert_model(input_text)
   print(summary)
   ```

   Your input text is processed by the bert_model instance, which then returns a
   summarized version. This demonstrates the power of Python's high-level
   libraries in enabling complex operations with minimal code.

6. Create `requirements.txt`. The sample application already contains the
   `requirements.txt` file to specify the necessary modules that the
   application imports. Open `requirements.txt` in a code or text editor to
   explore its contents.

   ```text
   ...

   # 04 text_summarization
   bert-extractive-summarizer==0.10.1

   ...

   torch==2.1.2
   ```

   The `bert-extractive-summarizer` and `torch` modules are required for the
   text summarization application. The summarizer module generates a summary of
   the input text. This requires PyTorch because the underlying BERT model,
   which is used for generating the summary, is implemented in PyTorch.

## Explore the application environment

See the [Docker-NLP Dockerfile walkthrough](nlp-container-environment.md).

The `RUN python -m spacy download en_core_web_sm` step is not needed for this app, but is included for compatibility with other NLP applications that might use this Dockerfile.

## Run the application

To run the application using Docker:

1. [Build the `basic-nlp` image](nlp-sample-workflow.md#build-the-image).

2. Run the image as a container.

   In a terminal, run the following command.

   ```console
   $ docker run -it basic-nlp 04_text_summarization.py
   ```

   See [interactive container options](nlp-sample-workflow.md#interactive-container-options) for `docker run`, `-it`, and the image name.

   - `04_text_summarization.py`: This is the script you want to run inside the
     Docker container. It gets passed to the `entrypoint.sh` script, which runs
     it when the container starts.

   For more details, see the [docker run CLI reference](/reference/cli/docker/container/run/).

   See the [Windows line-ending caveat](nlp-sample-workflow.md#windows-line-endings).

   You will see the following in your console after the container starts.

   ```console
   Enter the text for summarization (type 'exit' to end):
   ```

3. Test the application.

   Enter some text to get the text summarization.

   ```console
   Enter the text for summarization (type 'exit' to end): Artificial intelligence (AI) is a branch of computer science that aims to create machines capable of intelligent behavior. These machines are designed to mimic human cognitive functions such as learning, problem-solving, and decision-making. AI technologies can be classified into two main types: narrow or weak AI, which is designed for a particular task, and general or strong AI, which possesses the ability to understand, learn, and apply knowledge across various domains. One of the most popular approaches in AI is machine learning, where algorithms are trained on large datasets to recognize patterns and make predictions.

   Artificial intelligence (AI) is a branch of computer science that aims to create machines capable of intelligent behavior. These machines are designed to mimic human cognitive functions such as learning, problem-solving, and decision-making.
   ```

## Summary

In this guide, you learned how to build and run a text summarization
application. You learned how to build the application using Python with Bert
Extractive Summarizer, and then set up the environment and run the application
using Docker.

Related information:

- [Docker CLI reference](/reference/cli/docker/)
- [Dockerfile reference](/reference/dockerfile/)
- [Bert Extractive Summarizer](https://github.com/dmmiller612/bert-extractive-summarizer)
- [PyTorch](https://pytorch.org/)
- [Python documentation](https://docs.python.org/3/)

## Next steps

Explore more [natural language processing guides](./_index.md).
