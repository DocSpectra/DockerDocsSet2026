---
title: Build a named entity recognition app
linkTitle: Named entity recognition
keywords: nlp, natural language processing, named entity recognition, python, spacy, ner
description: Learn how to build and run a named entity recognition application using Python, spaCy, and Docker.
summary: |
  This guide explains how to containerize named entity recognition (NER) models
  using Docker.
tags: [ai]
languages: [python]
aliases:
  - /guides/use-case/nlp/named-entity-recognition/
params:
  time: 20 minutes
---

## Overview

This guide walks you through building and running a named entity recognition
(NER) application. You'll build the application using Python with
spaCy, and then set up the environment and run the application using Docker.

The application processes input text to identify and print named entities, like people, organizations, or locations.

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

The source code for the name recognition application is in the `Docker-NLP/02_name_entity_recognition.py` file. Open `02_name_entity_recognition.py` in a text or code editor to explore its contents in the following steps.

1. Import the required libraries.

   ```python
   import spacy
   ```

   This line imports the `spaCy` library. `spaCy` is a popular library in Python
   used for natural language processing (NLP).

2. Load the language model.

   ```python
   nlp = spacy.load("en_core_web_sm")
   ```

   Here, the `spacy.load` function loads a language model. The `en_core_web_sm`
   model is a small English language model. You can use this model for various
   NLP tasks, including tokenization, part-of-speech tagging, and named entity
   recognition.

3. Specify the main execution block.

   ```python
   if __name__ == "__main__":
   ```

   This Python idiom ensures that the following code block runs only if this
   script is the main program. It provides flexibility, allowing the script to
   function both as a standalone program and as an imported module.

4. Create an infinite loop for continuous input.

   ```python
      while True:
   ```

   This while loop runs indefinitely until it's explicitly broken. It lets
   the user continuously enter text for entity recognition until they decide
   to exit.

5. Get user input.

   ```python
   input_text = input("Enter the text for entity recognition (type 'exit' to end): ")
   ```

   This line prompts the user to enter text. The program will then perform entity recognition on this text.

6. Define an exit condition.

   ```python
   if input_text.lower() == 'exit':
      print("Exiting...")
      break
   ```

   If the user types something, the program converts the input to lowercase and
   compares it to `exit`. If they match, the program prints **Exiting...** and
   breaks out of the while loop, effectively ending the program.

7. Perform named entity recognition.

   ```python
   doc = nlp(input_text)

   for ent in doc.ents:
      print(f"Entity: {ent.text}, Type: {ent.label_}")
   ```

   - `doc = nlp(input_text)`: Here, the nlp model processes the user-input text. This creates a Doc object which contains various NLP attributes, including identified entities.
   - `for ent in doc.ents:`: This loop iterates over the entities found in the text.
   - `print(f"Entity: {ent.text}, Type: {ent.label_}")`: For each entity, it prints the entity text and its type (like PERSON, ORG, or GPE).

8. Create `requirements.txt`.

   The sample application already contains the `requirements.txt` file to specify the necessary packages that the application imports. Open `requirements.txt` in a code or text editor to explore its contents.

   ```text
   # 02 named_entity_recognition
   spacy==3.7.2

   ...
   ```

   Only the `spacy` package is required for the named recognition application.

## Explore the application environment

See the [Docker-NLP Dockerfile walkthrough](nlp-container-environment.md).

## Run the application

To run the application using Docker:

1. [Build the `basic-nlp` image](nlp-sample-workflow.md#build-the-image).

2. Run the image as a container.

   In a terminal, run the following command.

   ```console
   $ docker run -it basic-nlp 02_name_entity_recognition.py
   ```

   See [interactive container options](nlp-sample-workflow.md#interactive-container-options) for `docker run`, `-it`, and the image name.

   - `02_name_entity_recognition.py`: This is the script you want to run inside
     the Docker container. It gets passed to the `entrypoint.sh` script, which
     runs it when the container starts.

   For more details, see the [docker run CLI reference](/reference/cli/docker/container/run/).

   See the [Windows line-ending caveat](nlp-sample-workflow.md#windows-line-endings).

   You will see the following in your console after the container starts.

   ```console
   Enter the text for entity recognition (type 'exit' to end):
   ```

3. Test the application.

   Enter some information to get the named entity recognition.

   ```console
   Enter the text for entity recognition (type 'exit' to end): Apple Inc. is planning to open a new store in San Francisco. Tim Cook is the CEO of Apple.

   Entity: Apple Inc., Type: ORG
   Entity: San Francisco, Type: GPE
   Entity: Tim Cook, Type: PERSON
   Entity: Apple, Type: ORG
   ```

## Summary

This guide demonstrated how to build and run a named entity recognition
application. You learned how to build the application using Python with spaCy,
and then set up the environment and run the application using Docker.

Related information:

- [Docker CLI reference](/reference/cli/docker/)
- [Dockerfile reference](/reference/dockerfile/)
- [spaCy](https://spacy.io/)
- [Python documentation](https://docs.python.org/3/)

## Next steps

Explore more [natural language processing guides](./_index.md).
