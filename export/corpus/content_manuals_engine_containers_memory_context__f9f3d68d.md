---
title: Understand the risks of running out of memory
---

## Understand the risks of running out of memory {#understand-the-risks-of-running-out-of-memory}

It's important not to allow a running container to consume too much of the
host machine's memory. On Linux hosts, if the kernel detects that there isn't
enough memory to perform important system functions, it throws an `OOME`, or
`Out Of Memory Exception`, and starts killing processes to free up
memory. Any process is subject to killing, including Docker and other important
applications. This can effectively bring the entire system down if the wrong
process is killed.

Docker attempts to mitigate these risks by adjusting the OOM priority on the
Docker daemon so that it's less likely to be killed than other processes
on the system. The OOM priority on containers isn't adjusted. This makes it more
likely for an individual container to be killed than for the Docker daemon
or other system processes to be killed. You shouldn't try to circumvent
these safeguards by manually setting `--oom-score-adj` to an extreme negative
number on the daemon or a container, or by setting `--oom-kill-disable` on a
container.

For more information about the Linux kernel's OOM management, see
[Out of Memory Management](https://www.kernel.org/doc/gorman/html/understand/understand016.html).

You can mitigate the risk of system instability due to OOME by:

- Perform tests to understand the memory requirements of your application
  before placing it into production.
- Ensure that your application runs only on hosts with adequate resources.
- Limit the amount of memory your container can use.
- Be mindful when configuring swap on your Docker hosts. Swap is slower than
  memory but can provide a buffer against running out of system memory.
- Consider converting your container to a
  [service](/manuals/engine/swarm/services.md), and using service-level constraints
  and node labels to ensure that the application runs only on hosts with enough
  memory

