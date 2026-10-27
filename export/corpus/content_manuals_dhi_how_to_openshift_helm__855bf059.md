---
title: Deploy DHI Helm charts on OpenShift
description: Inspect chart values and apply OpenShift security context overrides.
---

Before you begin, review [OpenShift security constraints](../core-concepts/openshift.md) and [DHI registry authentication](authenticate.md).

Follow [image pull setup](openshift-pull.md), and see the [Helm chart installation procedure](helm.md) for shared steps.

## Deploy DHI Helm charts on OpenShift

DHI provides pre-configured Helm charts for popular applications. When deploying
these charts on OpenShift, you may need to adjust security context settings.

### Inspect chart values first

Before installing, check what security context values the chart exposes:

```console
helm registry login dhi.io

helm show values oci://dhi.io/<chart-name> --version <version> | grep -A 20 securityContext
```

The available value paths vary by chart, so always check `values.yaml` before
setting overrides.

### Install with OpenShift overrides

The following example shows a typical installation pattern. Adjust the `--set`
paths based on what `helm show values` returns for your specific chart:

```console
helm install my-release oci://dhi.io/<chart-name> \
    --version <version> \
    --set "imagePullSecrets[0].name=dhi-pull-secret" \
    -f openshift-values.yaml
```

Create an `openshift-values.yaml` with security context overrides appropriate
for your chart:

```yaml
# Example — adjust keys based on `helm show values` output
podSecurityContext:
  runAsNonRoot: true
  seccompProfile:
    type: RuntimeDefault

securityContext:
  allowPrivilegeEscalation: false
  capabilities:
    drop:
      - ALL
```

> [!NOTE]
> 
> DHI Helm chart value paths are not standardized across charts. For example,
> one chart may use `image.imagePullSecrets`, while another uses
> `global.imagePullSecrets`. Always consult the specific chart’s documentation
> or `values.yaml`.
