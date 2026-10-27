---
title: Gordon prompts and working directory
description: Prompt guidance and working directory context for Gordon.
---

## Writing effective prompts

Be specific:
- Include relevant context: "my postgres container" not "the database"
- State your goal: "make my build faster" not "optimize"
- Include error messages when debugging

Gordon works best when you describe what you want to achieve rather than how to
do it.

### Working directory context

When using `docker ai` in the CLI, Gordon uses your current working directory
as the default context for file operations. Change to your project directory
before starting Gordon to ensure it has access to the right files:

```console
$ cd ~/my-project
$ docker ai "review my Dockerfile"
```

You can also override the working directory with the `-C` flag.
