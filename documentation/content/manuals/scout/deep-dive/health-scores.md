---
title: Docker Scout health score calculation
---

## Scoring system

Health scores are determined by evaluating images against Docker Scout
[policies](/manuals/scout/deep-dive/policy-evaluation.md). These policies align with best practices for the
software supply chain.

If your image repositories are already enrolled with Docker Scout, the health
score is calculated automatically based on the policies that are enabled for
your organization. This also includes any custom policies that you have
configured.

If you're not using Docker Scout, the health scores show the compliance of your
images with the default policies, a set of supply chain rules recommended by
Docker as foundational standards for images. You can enable Docker Scout for
your organization and edit the policy configurations to get a more relevant
health score based on your specific policies.

### Scoring process

Each policy is assigned a points value based on its
[type](/manuals/scout/policy/types.md#policy-types). If the image is compliant
with a policy, it is awarded the points value for that policy type. The health
score of an image is calculated based on the percentage of points achieved
relative to the total possible points.

1. Policy compliance is evaluated for the image.
2. Points are awarded based on compliance with policies.
3. The points achieved percentage is calculated:

   ```text
   Percentage = (Points / Total) * 100
   ```

4. The final score is assigned based on the percentage of points achieved, as
   shown in the following table:

   | Points percentage (awarded out of total) | Score |
   | ---------------------------------------- | ----- |
   | More than 90%                            | A     |
   | 71% to 90%                               | B     |
   | 51% to 70%                               | C     |
   | 31% to 50%                               | D     |
   | 11% to 30%                               | E     |
   | Less than 10%                            | F     |

### N/A scores

Images can also be assigned an `N/A` score, which can happen when:

- The image is larger than 4GB (compressed size).
- The image architecture is not `linux/amd64` or `linux/arm64`.
- The image is too old and does not have fresh data for evaluation.

If you see an `N/A` score, consider the following:

- If the image is too large, try reducing the size of the image.
- If the image has an unsupported architecture, rebuild the image for a
  supported architecture.
- If the image is too old, push a new tag to trigger a fresh evaluation.

### Policy weights

Different policy types carry varying weights, which impact the score assigned
to an image during evaluation, as shown in the following table.

| Policy type                                                                                  | Points |
| -------------------------------------------------------------------------------------------- | ------ |
| [Severity-Based Vulnerability](/manuals/scout/policy/types.md#severity-based-vulnerability) | 20     |
| [High-Profile Vulnerabilities](/manuals/scout/policy/types.md#high-profile-vulnerabilities) | 20     |
| [Supply Chain Attestations](/manuals/scout/policy/types.md#supply-chain-attestations)       | 15     |
| [Approved Base Images](/manuals/scout/policy/types.md#approved-base-images)                 | 15     |
| [Up-to-Date Base Images](/manuals/scout/policy/types.md#up-to-date-base-images)             | 10     |
| [SonarQube Quality Gates](/manuals/scout/policy/types.md#sonarqube-quality-gates) \*        | 10     |
| [Default Non-Root User](/manuals/scout/policy/types.md#default-non-root-user)               | 5      |
| [Compliant Licenses](/manuals/scout/policy/types.md#compliant-licenses)                     | 5      |

\* _This policy is not enabled by default and must be configured by the user._

### Evaluation

Health scores are calculated for new images pushed to Docker Hub after the
feature is enabled. The health scores help you maintain high security standards
and ensure your applications are built on secure and reliable images.

### Repository scores

In addition to individual image scores (per tag or digest), each repository
receives a health score based on the latest pushed tag, providing an overall
view of the repository's security status.

### Example

For an image with a total possible score of 100 points:

- If the image only deviates from one policy, worth 5 points, its score will be
  95 out of 100. Since this score is above the 90th percentile, the image
  receives an A health score.
- If the image is non-compliant with more policies and scores 65 out of 100, it
  receives a C health score, reflecting its lower compliance.
