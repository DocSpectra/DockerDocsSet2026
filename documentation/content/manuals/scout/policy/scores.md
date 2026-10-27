---
title: Docker Scout health scores
description: |
  Docker Scout health scores provide a supply chain assessment for Docker Hub
  images, grading them from A to F based on various security policies.
keywords: scout, health scores, evaluation, checks, grades, docker hub
---

{{< summary-bar feature_name="Docker Scout health scores" >}}

Docker Scout health scores provide a security assessment, and overall supply
chain health, of images on Docker Hub, helping you determine whether an image
meets established security best practices. The scores range from A to F, where
A represents the highest level of security and F the lowest, offering an
at-a-glance view of the security posture of your images.

Only users who are members of the organization that owns the repository, and
have at least “read” access to the repository, can view the health score. The
score is not visible to users outside the organization or members without
"read" access.

## Viewing health scores

{{< tabs >}}
{{< tab name="Docker Hub" >}}

To view the health score of an image in Docker Hub:

1. Go to Docker Hub and sign in.
2. Navigate to your organization's page.

In the list of repositories, you can see the health score of each repository
based on the latest pushed tag.

![Repository health score](../images/score-badges-repolist.png)

{{< /tab >}}
{{< tab name="Docker Desktop" >}}

To view the health score of an image in Docker Desktop:

1. Open Docker Desktop and sign in to your Docker account.
2. Navigate to the **Images** view and select the **Hub** tab.

In the list of repositories, the **Health** column displays the scores of the
different tags that have been pushed to Docker Hub.

![Repository health score](../images/score-badges-dd.png)

{{< /tab >}}
{{< /tabs >}}

The health score badge is color-coded to indicate the overall health of the
repository:

- **Green**: A score of A or B.
- **Yellow**: A score of C.
- **Orange**: A score of D.
- **Red**: A score of E or F.
- **Gray**: An `N/A` score.

The score is also displayed on the Docker Hub page for a given repository,
along with each policy that contributed to the score.

![Scout "A" health score](../images/score-a-shiny.png?w=450px)

## Scoring system

See [Health score calculation](/manuals/scout/deep-dive/health-scores.md#scoring-system).

### N/A scores

See [N/A scores](/manuals/scout/deep-dive/health-scores.md#na-scores).

### Policy weights

See [Policy weights](/manuals/scout/deep-dive/health-scores.md#policy-weights).

## Improving your health score

To improve the health score of an image, take steps to ensure that the image is
compliant with the Docker Scout recommended [policies](/manuals/scout/deep-dive/policy-evaluation.md).

1. Go to the [Docker Scout Dashboard](https://scout.docker.com/).
2. Sign in using your Docker ID.
3. Go to [Repository settings](https://scout.docker.com/settings/repos) and
   enable Docker Scout for your Docker Hub image repositories.
4. Analyze the [policy compliance](/manuals/scout/deep-dive/policy-evaluation.md) for your repositories,
   and take actions to ensure your images are policy-compliant.

Since policies are weighted differently, prioritize the policies with the
highest scores for a greater impact on your image's overall score.
