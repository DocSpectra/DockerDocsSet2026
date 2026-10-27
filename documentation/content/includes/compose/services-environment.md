The `environment` attribute defines environment variables set in the container. `environment` can use either an array or a
map. Any boolean values; true, false, yes, no, should be enclosed in quotes to ensure
they are not converted to True or False by the YAML parser.

See [environment syntax and precedence](/reference/compose-file/services.md#environment), [env_file](/reference/compose-file/services.md#env_file), and [interpolation](/reference/compose-file/interpolation.md).
