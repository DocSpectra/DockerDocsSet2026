With the `depends_on` attribute, you can control the order of service startup and shutdown. It is useful if services are closely coupled, and the startup sequence impacts the application's functionality.

See [dependency syntax and startup guarantees](/reference/compose-file/services.md#depends_on) and [healthcheck configuration](/reference/compose-file/services.md#healthcheck).
