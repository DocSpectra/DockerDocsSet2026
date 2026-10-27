The `healthcheck` attribute declares a check that's run to determine whether or not the service containers are "healthy". It works in the same way, and has the same default values, as the HEALTHCHECK Dockerfile instruction
set by the service's Docker image. Your Compose file can override the values set in the Dockerfile. 

See [healthcheck commands, durations, and disabling checks](/reference/compose-file/services.md#healthcheck), and [dependency health conditions](/reference/compose-file/services.md#depends_on).
