---
title: Prepare and build the Docker-NLP sample
description: Verify the Docker-NLP sample files and build its container image.
---

## Verify the sample files

You should see the following files in your `Docker-NLP` directory.

```text
01_sentiment_analysis.py
02_name_entity_recognition.py
03_text_classification.py
04_text_summarization.py
05_language_translation.py
entrypoint.sh
requirements.txt
Dockerfile
README.md
```

## Build the image

In a terminal, run the following command inside the directory of where the `Dockerfile` is located.

```console
$ docker build -t basic-nlp .
```

The following is a break down of the command:

- `docker build`: This is the primary command used to build a Docker image
  from a Dockerfile and a context. The context is typically a set of files at
  a specified location, often the directory containing the Dockerfile.
- `-t basic-nlp`: This is an option for tagging the image. The `-t` flag
  stands for tag. It assigns a name to the image, which in this case is
  `basic-nlp`. Tags are a convenient way to reference images later,
  especially when pushing them to a registry or running containers.
- `.`: This is the last part of the command and specifies the build context.
  The period (`.`) denotes the current directory. Docker will look for a
  Dockerfile in this directory. The build context (the current directory, in
  this case) is sent to the Docker daemon to enable the build. It includes
  all the files and subdirectories in the specified directory.

For more details, see the [docker build CLI reference](/reference/cli/docker/buildx/build/).

Docker outputs several logs to your console as it builds the image. You'll
see it download and install the dependencies. Depending on your network
connection, this may take several minutes. Docker does have a caching
feature, so subsequent builds can be faster. The console will
return to the prompt when it's complete.

## Interactive container options

Options for the task-specific run command:

- `docker run`: This is the primary command used to run a new container from
  a Docker image.
- `-it`: This is a combination of two options:
  - `-i` or `--interactive`: This keeps the standard input (STDIN) open even
    if not attached. It lets the container remain running in the
    foreground and be interactive.
  - `-t` or `--tty`: This allocates a pseudo-TTY, essentially simulating a
    terminal, like a command prompt or a shell. It's what lets you
    interact with the application inside the container.
- `basic-nlp`: This specifies the name of the Docker image to use for
  creating the container. In this case, it's the image named `basic-nlp` that
  you created with the `docker build` command.

## Windows line endings

> [!NOTE]
>
> For Windows users, you may get an error when running the container. Verify
> that the line endings in the `entrypoint.sh` are `LF` (`\n`) and not `CRLF` (`\r\n`),
> then rebuild the image. For more details, see [Avoid unexpected syntax errors, use Unix style line endings for files in containers](/manuals/desktop/troubleshoot-and-support/troubleshoot/windows-line-endings.md).

