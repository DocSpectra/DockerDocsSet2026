---
title: Compose byte values and durations
description: Reference syntax for byte values and durations in Compose files.
---

## Specifying byte values

Values express a byte value as a string in `{amount}{byte unit}` format:
The supported units are `b` (bytes), `k` or `kb` (kilo bytes), `m` or `mb` (mega bytes) and `g` or `gb` (giga bytes).

```text
    2b
    1024kb
    2048k
    300m
    1gb
```

## Specifying durations

Values express a duration as a string in the form of `{value}{unit}`.
The supported units are `us` (microseconds), `ms` (milliseconds), `s` (seconds), `m` (minutes) and `h` (hours).
Values can combine multiple values without separator.

```text
  10ms
  40s
  1m30s
  1h5m30s20ms
```
