---
title: Build a sentiment analysis app
linkTitle: Sentiment analysis
keywords: nlp, natural language processing, sentiment analysis, python, nltk
description: Learn how to build and run a sentiment analysis application using Python, NLTK, and Docker.
summary: |
  This guide demonstrates how to containerize sentiment analysis models using
  Docker.
tags: [ai]
languages: [python]
aliases:
  - /guides/use-case/nlp/sentiment-analysis/
params:
  time: 20 minutes
---

## Overview

In this guide, you learn how to build and run a sentiment analysis application.
You'll build the application using Python with the Natural Language Toolkit
(NLTK), and then set up the environment and run the application using Docker.

The application analyzes user input text for sentiment using NLTK's
SentimentIntensityAnalyzer and outputs whether the sentiment is positive,
negative, or neutral.

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

The source code for the sentiment analysis application is in the `Docker-NLP/01_sentiment_analysis.py` file. Open `01_sentiment_analysis.py` in a text or code editor to explore its contents in the following steps.

1. Import the required libraries.

   ```python
   import nltk
   from nltk.sentiment import SentimentIntensityAnalyzer
   import ssl
   ```

   - `nltk`: This is the Natural Language Toolkit library used for working with
     human language data in Python.
   - `SentimentIntensityAnalyzer`: This is a specific tool from NLTK used for
     determining the sentiment of a piece of text.
   - `ssl`: This module provides access to Transport Layer Security (encryption)
     functions used for secure web connections.

2. Handle SSL certificate verification.

   ```python
   try:
       _create_unverified_https_context = ssl._create_unverified_context
   except AttributeError:
       pass
   else:
       ssl._create_default_https_context = _create_unverified_https_context
   ```

   This block is a workaround for certain environments where downloading data through NLTK might fail due to SSL certificate verification issues. It's telling Python to ignore SSL certificate verification for HTTPS requests.

3. Download NLTK resources.

   ```python
   nltk.download('vader_lexicon')
   nltk.download('punkt')
   ```

   - `vader_lexicon`: This is a lexicon used by the `SentimentIntensityAnalyzer`
     for sentiment analysis.
   - `punkt`: This is used by NLTK for tokenizing sentences. It's necessary for
     the `SentimentIntensityAnalyzer` to function correctly.

4. Create a sentiment analysis function.

   ```python
   def perform_semantic_analysis(text):
       sid = SentimentIntensityAnalyzer()
       sentiment_score = sid.polarity_scores(text)

       if sentiment_score['compound'] >= 0.05:
           return "Positive"
       elif sentiment_score['compound'] <= -0.05:
           return "Negative"
       else:
           return "Neutral"
   ```

   - `SentimentIntensityAnalyzer()` creates an instance of the
     analyzer.
   - `polarity_scores(text)` generates a sentiment score for the input text.

   The function returns **Positive**, **Negative**, or **Neutral** based on the
   compound score.

5. Create the main loop.

   ```python
   if __name__ == "__main__":
       while True:
           input_text = input("Enter the text for semantic analysis (type 'exit' to end): ")

           if input_text.lower() == 'exit':
               print("Exiting...")
               break

           result = perform_semantic_analysis(input_text)
           print(f"Sentiment: {result}")
   ```

   This part of the script runs an infinite loop to accept user input for
   analysis. If the user types `exit`, the program terminates. Otherwise, it
   prints out the sentiment of the provided text.

6. Create `requirements.txt`.

   The sample application already contains the
   `requirements.txt` file to specify the necessary packages that the
   application imports. Open `requirements.txt` in a code or text editor to
   explore its contents.

   ```text
   # 01 sentiment_analysis
   nltk==3.6.5

   ...
   ```

   Only the `nltk` package is required for the sentiment analysis application.

## Explore the application environment

See the [Docker-NLP Dockerfile walkthrough](nlp-container-environment.md).

The `RUN python -m spacy download en_core_web_sm` step is not needed for this app, but is included for compatibility with other NLP applications that might use this Dockerfile.

## Run the application

To run the application using Docker:

1. [Build the `basic-nlp` image](nlp-sample-workflow.md#build-the-image).

2. Run the image as a container.

   In a terminal, run the following command.

   ```console
   $ docker run -it basic-nlp 01_sentiment_analysis.py
   ```

   See [interactive container options](nlp-sample-workflow.md#interactive-container-options) for `docker run`, `-it`, and the image name.

   - `01_sentiment_analysis.py`: This is the script you want to run inside the
     Docker container. It gets passed to the `entrypoint.sh` script, which runs
     it when the container starts.

   For more details, see the [docker run CLI reference](/reference/cli/docker/container/run/).

   See the [Windows line-ending caveat](nlp-sample-workflow.md#windows-line-endings).

   You will see the following in your console after the container starts.

   ```console
   Enter the text for semantic analysis (type 'exit' to end):
   ```

3. Test the application.

   Enter a comment to get the sentiment analysis.

   ```console
   Enter the text for semantic analysis (type 'exit' to end): I love containers!
   Sentiment: Positive
   Enter the text for semantic analysis (type 'exit' to end): I'm still learning about containers.
   Sentiment: Neutral
   ```

## Summary

In this guide, you learned how to build and run a sentiment analysis
application. You learned how to build the application using Python with NLTK,
and then set up the environment and run the application using Docker.

Related information:

- [Docker CLI reference](/reference/cli/docker/)
- [Dockerfile reference](/reference/dockerfile/)
- [Natural Language Toolkit](https://www.nltk.org/)
- [Python documentation](https://docs.python.org/3/)

## Next steps

Explore more [natural language processing guides](./_index.md).
