---
title: Build a text recognition app
linkTitle: Text classification
keywords: nlp, natural language processing, sentiment analysis, python, nltk, scikit-learn, text classification
description: Learn how to build and run a text recognition application using Python, NLTK, scikit-learn, and Docker.
summary: |
  This guide details how to containerize text classification models using
  Docker.
tags: [ai]
languages: [python]
aliases:
  - /guides/use-case/nlp/text-classification/
params:
  time: 20 minutes
---

## Overview

In this guide, you'll learn how to create and run a text recognition
application. You'll build the application using Python with scikit-learn and the
Natural Language Toolkit (NLTK). Then you'll set up the environment and run the
application using Docker.

The application analyzes the sentiment of a user's input text using NLTK's
SentimentIntensityAnalyzer. It lets the user input text, which is then processed
to determine its sentiment, classifying it as either positive or negative. Also,
it displays the accuracy and a detailed classification report of its sentiment
analysis model based on a predefined dataset.

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

The source code for the text classification application is in the `Docker-NLP/03_text_classification.py` file. Open `03_text_classification.py` in a text or code editor to explore its contents in the following steps.

1. Import the required libraries.

   ```python
   import nltk
   from nltk.sentiment import SentimentIntensityAnalyzer
   from sklearn.metrics import accuracy_score, classification_report
   from sklearn.model_selection import train_test_split
   import ssl
   ```

   - `nltk`: A popular Python library for natural language processing (NLP).
   - `SentimentIntensityAnalyzer`: A component of `nltk` for sentiment analysis.
   - `accuracy_score`, `classification_report`: Functions from scikit-learn for
     evaluating the model.
   - `train_test_split`: Function from scikit-learn to split datasets into
     training and testing sets.
   - `ssl`: Used for handling SSL certificate issues which might occur while
     downloading data for `nltk`.

2. Handle SSL certificate verification.

   ```python
   try:
       _create_unverified_https_context = ssl._create_unverified_context
   except AttributeError:
       pass
   else:
       ssl._create_default_https_context = _create_unverified_https_context
   ```

   This block is a workaround for certain environments where downloading data
   through NLTK might fail due to SSL certificate verification issues. It's
   telling Python to ignore SSL certificate verification for HTTPS requests.

3. Download NLTK resources.

   ```python
   nltk.download('vader_lexicon')
   ```

   The `vader_lexicon` is a lexicon used by the `SentimentIntensityAnalyzer` for
   sentiment analysis.

4. Define text for testing and corresponding labels.

   ```python
   texts = [...]
   labels = [0, 1, 2, 0, 1, 2]
   ```

   This section defines a small dataset of texts and their corresponding labels (0 for positive, 1 for negative, and 2 for spam).

5. Split the test data.

   ```python
   X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)
   ```

   This part splits the dataset into training and testing sets, with 20% of data
   as the test set. As this application uses a pre-trained model, it doesn't
   train the model.

6. Set up sentiment analysis.

   ```python
   sia = SentimentIntensityAnalyzer()
   ```

   This code initializes the `SentimentIntensityAnalyzer` to analyze the
   sentiment of text.

7. Generate predictions and classifications for the test data.

   ```python
   vader_predictions = [sia.polarity_scores(text)["compound"] for text in X_test]
   threshold = 0.2
   vader_classifications = [0 if score > threshold else 1 for score in vader_predictions]
   ```

   This part generates sentiment scores for each text in the test set and classifies them as positive or negative based on a threshold.

8. Evaluate the model.

   ```python
   accuracy = accuracy_score(y_test, vader_classifications)
   report_vader = classification_report(y_test, vader_classifications, zero_division='warn')
   ```

   This part calculates the accuracy and classification report for the predictions.

9. Specify the main execution block.

   ```python
   if __name__ == "__main__":
   ```

   This Python idiom ensures that the following code block runs only if this
   script is the main program. It provides flexibility, allowing the script to
   function both as a standalone program and as an imported module.

10. Create an infinite loop for continuous input.

    ```python
       while True:
        input_text = input("Enter the text for classification (type 'exit' to end): ")

          if input_text.lower() == 'exit':
             print("Exiting...")
             break
    ```

    This while loop runs indefinitely until it's explicitly broken. It lets the
    user continuously enter text for entity recognition until they decide to
    exit.

11. Analyze the text.

    ```python
            input_text_score = sia.polarity_scores(input_text)["compound"]
            input_text_classification = 0 if input_text_score > threshold else 1
    ```

12. Print the VADER Classification Report and the sentiment analysis.

    ```python
            print(f"Accuracy: {accuracy:.2f}")
            print("\nVADER Classification Report:")
            print(report_vader)

            print(f"\nTest Text (Positive): '{input_text}'")
            print(f"Predicted Sentiment: {'Positive' if input_text_classification == 0 else 'Negative'}")
    ```

13. Create `requirements.txt`. The sample application already contains the
    `requirements.txt` file to specify the necessary packages that the
    application imports. Open `requirements.txt` in a code or text editor to
    explore its contents.

    ```text
    # 01 sentiment_analysis
    nltk==3.6.5

    ...

    # 03 text_classification
    scikit-learn==1.3.2

    ...
    ```

    Both the `nltk` and `scikit-learn` modules are required for the text
    classification application.

## Explore the application environment

See the [Docker-NLP Dockerfile walkthrough](nlp-container-environment.md).

The `RUN python -m spacy download en_core_web_sm` step is not needed for this app, but is included for compatibility with other NLP applications that might use this Dockerfile.

## Run the application

To run the application using Docker:

1. [Build the `basic-nlp` image](nlp-sample-workflow.md#build-the-image).

2. Run the image as a container.

   In a terminal, run the following command.

   ```console
   $ docker run -it basic-nlp 03_text_classification.py
   ```

   See [interactive container options](nlp-sample-workflow.md#interactive-container-options) for `docker run`, `-it`, and the image name.

   - `03_text_classification.py`: This is the script you want to run inside the
     Docker container. It gets passed to the `entrypoint.sh` script, which runs
     it when the container starts.

   For more details, see the [docker run CLI reference](/reference/cli/docker/container/run/).

   See the [Windows line-ending caveat](nlp-sample-workflow.md#windows-line-endings).

   You will see the following in your console after the container starts.

   ```console
   Enter the text for classification (type 'exit' to end):
   ```

3. Test the application.

   Enter some text to get the text classification.

   ```console
   Enter the text for classification (type 'exit' to end): I love containers!
   Accuracy: 1.00

   VADER Classification Report:
                 precision    recall  f1-score   support

              0       1.00      1.00      1.00         1
              1       1.00      1.00      1.00         1

       accuracy                           1.00         2
      macro avg       1.00      1.00      1.00         2
   weighted avg       1.00      1.00      1.00         2

   Test Text (Positive): 'I love containers!'
   Predicted Sentiment: Positive
   ```

## Summary

In this guide, you learned how to build and run a text classification
application. You learned how to build the application using Python with
scikit-learn and NLTK. Then you learned how to set up the environment and run
the application using Docker.

Related information:

- [Docker CLI reference](/reference/cli/docker/)
- [Dockerfile reference](/reference/dockerfile/)
- [Natural Language Toolkit](https://www.nltk.org/)
- [Python documentation](https://docs.python.org/3/)
- [scikit-learn](https://scikit-learn.org/)

## Next steps

Explore more [natural language processing guides](./_index.md).
