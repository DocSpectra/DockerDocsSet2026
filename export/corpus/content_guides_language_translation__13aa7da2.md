---
title: Build a language translation app
linkTitle: Language translation
keywords: nlp, natural language processing, text summarization, python, language translation, googletrans
description: Learn how to build and run a language translation application using Python, Googletrans, and Docker.
summary: |
  This guide demonstrates how to use Docker to deploy language translation
  models for NLP tasks.
tags: [ai]
languages: [python]
aliases:
  - /guides/use-case/nlp/language-translation/
params:
  time: 20 minutes
---

## Overview

This guide walks you through building and running a language translation
application. You'll build the application using Python with Googletrans, and
then set up the environment and run the application using Docker.

The application demonstrates a simple but practical use of the Googletrans
library for language translation, showcasing basic Python and Docker concepts.
Googletrans is a free and unlimited Python library that implements the Google
Translate API. It uses the Google Translate Ajax API to make calls to such
methods as detect and translate.

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

The source code for the application is in the
`Docker-NLP/05_language_translation.py` file. Open `05_language_translation.py`
in a text or code editor to explore its contents in the following steps.

1. Import the required libraries.

   ```python
   from googletrans import Translator
   ```

   This line imports the `Translator` class from `googletrans`.
   Googletrans is a Python library that provides an interface to Google
   Translate's AJAX API.

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
         input_text = input("Enter the text for translation (type 'exit' to end): ")

         if input_text.lower() == 'exit':
            print("Exiting...")
            break
   ```

   An infinite loop is established here to continuously prompt you for text
   input, ensuring interactivity. The loop breaks when you type `exit`, allowing
   you to control the application flow effectively.

4. Create an instance of Translator.

   ```python
         translator = Translator()
   ```

   This creates an instance of the Translator class, which
   performs the translation.

5. Translate text.

   ```python
         translated_text = translator.translate(input_text, dest='fr').text
   ```

   Here, the `translator.translate` method is called with the user input. The
   `dest='fr'` argument specifies that the destination language for translation
   is French. The `.text` attribute gets the translated string. For more details
   about the available language codes, see the
   [Googletrans docs](https://py-googletrans.readthedocs.io/en/latest/).

6. Print the original and translated text.

   ```python
         print(f"Original Text: {input_text}")
         print(f"Translated Text: {translated_text}")
   ```

   These two lines print the original text entered by the user and the
   translated text.

7. Create `requirements.txt`. The sample application already contains the
   `requirements.txt` file to specify the necessary modules that the
   application imports. Open `requirements.txt` in a code or text editor to
   explore its contents.

   ```text
   ...

   # 05 language_translation
   googletrans==4.0.0-rc1
   ```

   Only `googletrans` is required for the language translation application.

## Explore the application environment

See the [Docker-NLP Dockerfile walkthrough](nlp-container-environment.md).

The `RUN python -m spacy download en_core_web_sm` step is not needed for this app, but is included for compatibility with other NLP applications that might use this Dockerfile.

## Run the application

To run the application using Docker:

1. [Build the `basic-nlp` image](nlp-sample-workflow.md#build-the-image).

2. Run the image as a container.

   In a terminal, run the following command.

   ```console
   $ docker run -it basic-nlp 05_language_translation.py
   ```

   See [interactive container options](nlp-sample-workflow.md#interactive-container-options) for `docker run`, `-it`, and the image name.

   - `05_language_translation.py`: This is the script you want to run inside the
     Docker container. It gets passed to the `entrypoint.sh` script, which runs
     it when the container starts.

   For more details, see the [docker run CLI reference](/reference/cli/docker/container/run/).

   See the [Windows line-ending caveat](nlp-sample-workflow.md#windows-line-endings).

   You will see the following in your console after the container starts.

   ```console
   Enter the text for translation (type 'exit' to end):
   ```

3. Test the application.

   Enter some text to get the text summarization.

   ```console
   Enter the text for translation (type 'exit' to end): Hello, how are you doing?
   Original Text: Hello, how are you doing?
   Translated Text: Bonjour comment allez-vous?
   ```

## Summary

In this guide, you learned how to build and run a language translation
application. You learned how to build the application using Python with
Googletrans, and then set up the environment and run the application using
Docker.

Related information:

- [Docker CLI reference](/reference/cli/docker/)
- [Dockerfile reference](/reference/dockerfile/)
- [Googletrans](https://github.com/ssut/py-googletrans)
- [Python documentation](https://docs.python.org/3/)

## Next steps

Explore more [natural language processing guides](./_index.md).
