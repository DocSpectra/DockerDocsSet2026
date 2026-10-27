---
title: Remediation with Docker Scout
description: Learn how Docker Scout can help you improve your software quality automatically, using remediation
keywords: scout, supply chain, security, remediation, automation
---

{{< summary-bar feature_name="Remediation with Docker Scout" >}}

Docker Scout helps you remediate supply chain or security issues by providing
recommendations based on policy evaluation results. Recommendations are
suggested actions you can take that improve policy compliance, or that add
metadata to images which enables Docker Scout to provide better evaluation
results and recommendations.

Docker Scout provides remediation advice for the default policies of the
following policy types:

- [Up-to-Date Base Images](#up-to-date-base-images-remediation)
- [Supply Chain Attestations](#supply-chain-attestations-remediation)

> [!NOTE]
> Guided remediation is not supported for custom policies.

For images that violate policy, the recommendations focus on addressing
compliance issues and fixing violations. For images where Docker Scout is
unable to determine compliance, recommendations show you how to meet the
prerequisites that ensure Docker Scout can successfully evaluate the policy.

## View recommendations

Recommendations appear on the policy details pages of the Docker Scout
Dashboard. To get to this page:

1. Go to the [Policies page](https://scout.docker.com/reports/policy) in the Docker Scout Dashboard.
2. Select a policy in the list.

The policy details page groups evaluation results into two different tabs
depending on the policy status:

- Violations
- Compliance unknown

The **Violations** tab lists images that don't comply with the selected policy.
The **Compliance unknown** tab lists images that Docker Scout is unable to
determine the compliance status for. When compliance is unknown, Docker Scout
needs more information about the image.

To view recommended actions for an image, hover over one of the images in the
list to reveal a **View fixes** button.

![Remediation for policy violations](../images/remediation.png)

Select the **View fixes** button to opens the remediation side panel containing
recommended actions for your image.

If there are more than one recommendations available, the primary
recommendation displays as the **Recommended fix**. Additional recommendations
are listed as **Quick fixes**. Quick fixes are usually actions that provide a
temporary solution.

The side panel may also contain one or more help sections related to the
available recommendations.

## Up-to-Date Base Images remediation

See [Up-to-Date Base Images remediation](/manuals/scout/deep-dive/remediation.md#up-to-date-base-images-remediation).

## Supply Chain Attestations remediation

See [Supply Chain Attestations remediation](/manuals/scout/deep-dive/remediation.md#supply-chain-attestations-remediation).
