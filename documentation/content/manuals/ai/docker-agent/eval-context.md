---
title: Understand agent evals and their results
description: What saved-conversation comparisons measure and how to interpret their scores.
---

## What are evals

An eval is a saved conversation you can replay. When you run evals, Docker Agent
replays the user messages and compares the new responses against the original
saved conversation. High scores mean the agent behaved similarly; low scores
mean behavior changed.

What you do with that information depends on why you saved the conversation.
You might save successful conversations to catch regressions, or save failure
cases to document known issues and track whether they improve.

## Common workflows

How you use evals depends on what you're trying to accomplish:

Regression testing: Save conversations where your agent performs well. When you
make changes later (upgrade models, update prompts, refactor code), run the
evals. High scores mean behavior stayed consistent, which is usually what you
want. Low scores mean something changed - examine the new behavior to see if
it's still correct.

Tracking improvements: Save conversations where your agent struggles or fails.
As you make improvements, run these evals to see how behavior evolves. Low
scores indicate the agent now behaves differently, which might mean you fixed
the issue. You'll need to manually verify the new behavior is actually better.

Documenting edge cases: Save interesting or unusual conversations regardless of
quality. Use them to understand how your agent handles edge cases and whether
that behavior changes over time.

Evals measure whether behavior changed. You determine if that change is good or
bad.

## Understanding results

For each eval, Docker Agent shows:

- **First message** - The initial user message from the saved conversation
- **Eval file** - The UUID of the eval file being run
- **Tool trajectory score** - How similarly the agent used tools (0-1 scale,
  higher is better)
- **[ROUGE-1](https://en.wikipedia.org/wiki/ROUGE_(metric)) score** - Text
  similarity between responses (0-1 scale, higher is better)
- **Cost** - The cost for this eval run
- **Output tokens** - Number of tokens generated

Higher scores mean the agent behaved more similarly to the original recorded
conversation. A score of 1.0 means identical behavior.

### What the scores mean

**Tool trajectory score** measures whether the agent called the same tools in
the same order as the original conversation. Lower scores might indicate the
agent found a different approach to solve the problem, which isn't necessarily
wrong but worth investigating.

**Rouge-1 score** measures how similar the response text is to the original.
This is a heuristic measure - different wording might still be correct, so use
this as a signal rather than absolute truth.

### Interpreting your results

Scores close to 1.0 mean your changes maintained consistent behavior - the
agent is using the same approach and producing similar responses. This is
generally good; your changes didn't break existing functionality.

Lower scores mean behavior changed compared to the saved conversation. This
could be a regression where the agent now performs worse, or it could be an
improvement where the agent found a better approach.

When scores drop, examine the actual behavior to determine if it's better or
worse. The eval files are stored as JSON in your evals directory - open the
file to see the original conversation. Then test your modified agent with the
same input to compare responses. If the new response is better, save a new
conversation to replace the eval. If it's worse, you found a regression.

The scores guide you to what changed. Your judgment determines if the change is
good or bad.

## When to use evals

Evals help you track behavior changes over time. They're useful for catching
regressions when you upgrade models or dependencies, documenting known failure
cases you want to fix, and understanding how edge cases evolve as you iterate.

Evals aren't appropriate for determining which agent configuration works best -
they measure similarity to a saved conversation, not correctness. Use manual
testing to evaluate different configurations and decide which works better.

Save conversations worth tracking. Build a collection of important workflows,
interesting edge cases, and known issues. Run your evals when making changes to
see what shifted.

