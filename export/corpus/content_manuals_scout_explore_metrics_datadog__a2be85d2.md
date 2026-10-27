---
title: Scrape Docker Scout metrics with Datadog
---

## Prerequisites and endpoint reference

See [Docker Scout metrics endpoint](/manuals/scout/deep-dive/metrics.md) for metrics, streams, access-token requirements, scrape intervals, and token revocation.

## Datadog setup

This section describes how to scrape the metrics endpoint using Datadog.
Datadog pulls data for monitoring by running a customizable
[agent](https://docs.datadoghq.com/agent/?tab=Linux) that scrapes available
endpoints for any exposed metrics. The OpenMetrics and Prometheus checks are
included in the agent, so you don’t need to install anything else on your
containers or hosts.

This guide assumes you have a Datadog account and a Datadog API Key. Refer to
the [Datadog documentation](https://docs.datadoghq.com/agent) to get started.

### Configure the Datadog agent

To start collecting the metrics, you will need to edit the agent’s
configuration file for the OpenMetrics check. If you're running the agent as a
container, such file must be mounted at
`/etc/datadog-agent/conf.d/openmetrics.d/conf.yaml`.

The following example shows a Datadog configuration that:

- Specifies the OpenMetrics endpoint targeting the `dockerscoutpolicy` Docker organization
- A `namespace` that all collected metrics will be prefixed with
- The [`metrics`](/manuals/scout/deep-dive/metrics.md#metrics) you want the agent to scrape (`scout_*`)
- An `auth_token` section for the Datadog agent to authenticate to the Metrics
  endpoint, using a Docker PAT as a Bearer token.

```yaml
instances:
  - openmetrics_endpoint: "https://api.scout.docker.com/v1/exporter/org/dockerscoutpolicy/metrics"
    namespace: "scout-metrics-exporter"
    metrics:
      - scout_*
    auth_token:
      reader:
        type: file
        path: /var/run/secrets/scout-metrics-exporter/token
      writer:
        type: header
        name: Authorization
        value: Bearer <TOKEN>
```

> [!IMPORTANT]
>
> Do not replace the `<TOKEN>` placeholder in the previous configuration
> example. It must stay as it is. Only make sure the Docker PAT is correctly
> mounted into the Datadog agent in the specified filesystem path. Save the
> file as `conf.yaml` and restart the agent.

When creating a Datadog agent configuration of your own, make sure to edit the
`openmetrics_endpoint` property to target your organization, by replacing
`dockerscoutpolicy` with the namespace of your Docker organization.

### Datadog sample project

If you don't have a Datadog server set up, you can run a [sample project](https://github.com/dockersamples/scout-metrics-exporter)
using Docker Compose. The sample includes a Datadog agent, running as a
container, that scrapes metrics for a Docker organization enrolled in Docker
Scout. This sample project assumes that you have a Datadog account, an API key,
and a Datadog site.

1. Clone the starter template for bootstrapping a Datadog Compose service for
   scraping the Docker Scout metrics endpoint:

   ```console
   $ git clone git@github.com:dockersamples/scout-metrics-exporter.git
   $ cd scout-metrics-exporter/datadog
   ```

2. [Create a Docker access token](/manuals/security/access-tokens.md)
   and store it in a plain text file at `/datadog/token` under the template directory.

   ```plaintext {title=token}
   $ echo $DOCKER_PAT > ./token
   ```

3. In the `/datadog/compose.yaml` file, update the `DD_API_KEY` and `DD_SITE` environment variables
   with the values for your Datadog deployment.

   ```yaml {hl_lines="5-6"}
     datadog-agent:
       container_name: datadog-agent
       image: gcr.io/datadoghq/agent:7
       environment:
         - DD_API_KEY=${DD_API_KEY} # e.g. 1b6b3a42...
         - DD_SITE=${DD_SITE} # e.g. datadoghq.com
         - DD_DOGSTATSD_NON_LOCAL_TRAFFIC=true
       volumes:
         - /var/run/docker.sock:/var/run/docker.sock:ro
         - ./conf.yaml:/etc/datadog-agent/conf.d/openmetrics.d/conf.yaml:ro
         - ./token:/var/run/secrets/scout-metrics-exporter/token:ro
   ```

   The `volumes` section mounts the Docker socket from the host to the
   container. This is required to obtain an accurate hostname when running as a
   container ([more details here](https://docs.datadoghq.com/agent/troubleshooting/hostname_containers/)).

   It also mounts the agent's config file and the Docker access token.

4. Edit the `/datadog/config.yaml` file by replacing the placeholder `<ORG>` in
   the `openmetrics_endpoint` property with the namespace of the Docker
   organization that you want to collect metrics for.

   ```yaml {hl_lines=2}
   instances:
     - openmetrics_endpoint: "https://api.scout.docker.com/v1/exporter/org/<<ORG>>/metrics"
       namespace: "scout-metrics-exporter"
   # ...
   ```

5. Start the Compose services.

   ```console
   docker compose up -d
   ```

If configured properly, you should see the OpenMetrics check under Running
Checks when you run the agent’s status command whose output should look similar
to:

```text
openmetrics (4.2.0)
-------------------
  Instance ID: openmetrics:scout-prometheus-exporter:6393910f4d92f7c2 [OK]
  Configuration Source: file:/etc/datadog-agent/conf.d/openmetrics.d/conf.yaml
  Total Runs: 1
  Metric Samples: Last Run: 236, Total: 236
  Events: Last Run: 0, Total: 0
  Service Checks: Last Run: 1, Total: 1
  Average Execution Time : 2.537s
  Last Execution Date : 2024-05-08 10:41:07 UTC (1715164867000)
  Last Successful Execution Date : 2024-05-08 10:41:07 UTC (1715164867000)
```

For a comprehensive list of options, take a look at this [example config file](https://github.com/DataDog/integrations-core/blob/master/openmetrics/datadog_checks/openmetrics/data/conf.yaml.example) for the generic OpenMetrics check.

### Visualizing your data

Once the agent is configured to grab Prometheus metrics, you can use them to build comprehensive Datadog graphs, dashboards, and alerts.

Go into your [Metric summary page](https://app.datadoghq.com/metric/summary?filter=scout_prometheus_exporter)
to see the metrics collected from this example. This configuration will collect
all exposed metrics starting with `scout_` under the namespace
`scout_metrics_exporter`.

![datadog_metrics_summary](../images/datadog_metrics_summary.png)

The following screenshots show examples of a Datadog dashboard containing
graphs about vulnerability and policy compliance for a specific [stream](/manuals/scout/deep-dive/metrics.md#stream).

![datadog_dashboard_1](../images/datadog_dashboard_1.png)
![datadog_dashboard_2](../images/datadog_dashboard_2.png)

> The reason why the lines in the graphs look flat is due to the own nature of
> vulnerabilities (they don't change too often) and the short time interval
> selected in the date picker.
