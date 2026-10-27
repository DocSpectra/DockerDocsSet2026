---
title: Evals
description: Test your agents with saved conversations
keywords: [docker agent, evaluations, testing, evals]
weight: 80
---

Evaluations (evals) help you track how your agent's behavior changes over time.
When you save a conversation as an eval, you can replay it later to see if the
agent responds differently. Evals measure consistency, not correctness - they
tell you if behavior changed, not whether it's right or wrong.

## Evals and workflows

See [what evals measure and when to use them](eval-context.md).

## What are evals

See [what evals are](eval-context.md#what-are-evals).

## Common workflows

See [common workflows](eval-context.md#common-workflows).

## Creating an eval

Save a conversation from an interactive session:

```console
$ docker agent run ./agent.yaml
```

Have a conversation with your agent, then save it as an eval:

```console
> /eval test-case-name
Eval saved to evals/test-case-name.json
```

The conversation is saved to the `evals/` directory in your current working
directory. You can organize eval files in subdirectories if needed.

## Running evals

Run all evals in the default directory:

```console
$ docker agent eval ./agent.yaml
```

Use a custom eval directory:

```console
$ docker agent eval ./agent.yaml ./my-evals
```

Run evals against an agent from a registry:

```console
$ docker agent eval agentcatalog/myagent
```

Example output:

```console
$ docker agent eval ./agent.yaml
--- 0
First message: tell me something interesting about kil
Eval file: c7e556c5-dae5-4898-a38c-73cc8e0e6abe
Tool trajectory score: 1.000000
Rouge-1 score: 0.447368
Cost: 0.00
Output tokens: 177
```

## Understanding results

See [result fields, scores, and interpretation](eval-context.md#understanding-results).

## When to use evals

See [when to use evals](eval-context.md#when-to-use-evals).

## What's next

- Check the [CLI reference](reference/cli.md#eval) for all `docker agent eval`
  options
- Learn [best practices](best-practices.md) for building effective agents
- Review [example configurations](https://github.com/docker/docker-agent/tree/main/examples)
  for different agent types
