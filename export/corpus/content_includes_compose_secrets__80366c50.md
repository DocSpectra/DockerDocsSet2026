Docker Compose provides a way for you to use secrets without having to use environment variables to store information. If you’re injecting passwords and API keys as environment variables, you risk unintentional information exposure. Services can only access secrets when explicitly granted by a `secrets` attribute within the `services` top-level element.

See [secret sources](/reference/compose-file/secrets.md#choose-a-source), [service access and file-source limitations](/reference/compose-file/services.md#secrets), and [build access](/reference/compose-file/build.md#secrets).
