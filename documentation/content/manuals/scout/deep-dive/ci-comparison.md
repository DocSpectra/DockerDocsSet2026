---
title: Image comparison and policy evaluation in CI
---

Adding Policy Evaluation to your continuous integration pipelines helps you
detect and prevent cases where code changes would cause policy compliance to
become worse compared to your baseline.

The recommended strategy for Policy Evaluation in a CI setting involves
evaluating a local image and comparing the results to a baseline. If the policy
compliance for the local image is worse than the specified baseline, the CI run
fails with an error. If policy compliance is better or unchanged, the CI run
succeeds.

This comparison is relative, meaning that it's only concerned with whether your
CI image is better or worse than your baseline. It's not an absolute check to
pass or fail all policies. By measuring relative to a baseline that you define,
you can quickly see if a change has a positive or negative impact on policy
compliance.

## How it works

When you do Policy Evaluation in CI, you run a local policy evaluation on the
image you build in your CI pipeline. To run a local evaluation, the image that
you evaluate must exist in the image store where your CI workflow is being run.
Either build or pull the image, and then run the evaluation.

To run policy evaluation and trigger failure if compliance for your local image
is worse than your comparison baseline, you need to specify the image version
to use as a baseline. You can hard-code a specific image reference, but a
better solution is to use [environments](../integrations/environment/_index.md)
to automatically infer the image version from an environment. The policy evaluation example uses environments to compare
the CI image with
the image in the `production` environment.

## GitHub Actions example requirements

This example doesn't assume that you're using Docker Hub as your container
registry. As a result, this workflow uses the `docker/login-action` twice:

- Once for authenticating to your container registry.
- Once more for authenticating to Docker to pull the analysis results of your
  `production` image.

If you use Docker Hub as your container registry, you only need to authenticate
once.

> [!NOTE]
>
> Due to a limitation in the Docker Engine, loading multi-platform images or
> images with attestations to the image store isn't supported.
>
> For the policy evaluation to work, you must load the image to the local image
> store of the runner. Ensure that you're building a single-platform image
> without attestations, and that you're loading the build results. Otherwise,
> the policy evaluation fails.

Also note the `pull-requests: write` permission for the job. The Docker Scout
GitHub Action adds a pull request comment with the evaluation results by
default, which requires this permission. For details, see
[Pull Request Comments](https://github.com/docker/scout-action#pull-request-comments).

### Local analysis and evaluation

> [!NOTE]
>
> This CI workflow runs a local analysis and evaluation of your image. To
> evaluate the image locally, you must ensure that the image is loaded to the
> local image store of your runner.
>
> This comparison doesn't work if you push the image to a registry, or if you
> build an image that can't be loaded to the runner's local image store. For
> example, multi-platform images or images with SBOM or provenance attestation
> can't be loaded to the local image store.
