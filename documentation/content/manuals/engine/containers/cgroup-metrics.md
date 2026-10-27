---
title: Read cgroup memory, CPU, and block I/O metrics
---

Before reading metrics, see [control group versions and container cgroup locations](cgroups.md).

## Metrics from cgroups: memory, CPU, block I/O {#metrics-from-cgroups-memory-cpu-block-io}

> [!NOTE]
>
> This section isn't yet updated for cgroup v2.
> For further information about cgroup v2, refer to [the kernel documentation](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html).

For each subsystem (memory, CPU, and block I/O), one or
more pseudo-files exist and contain statistics.

### Memory metrics: `memory.stat` {#memory-metrics-memorystat}

Memory metrics are found in the `memory` cgroup. The memory
control group adds a little overhead, because it does very fine-grained
accounting of the memory usage on your host. Therefore, many distributions
chose to not enable it by default. Generally, to enable it, all you have
to do is to add some kernel command-line parameters:
`cgroup_enable=memory swapaccount=1`.

The metrics are in the pseudo-file `memory.stat`.
Here is what it looks like:

    cache 11492564992
    rss 1930993664
    mapped_file 306728960
    pgpgin 406632648
    pgpgout 403355412
    swap 0
    pgfault 728281223
    pgmajfault 1724
    inactive_anon 46608384
    active_anon 1884520448
    inactive_file 7003344896
    active_file 4489052160
    unevictable 32768
    hierarchical_memory_limit 9223372036854775807
    hierarchical_memsw_limit 9223372036854775807
    total_cache 11492564992
    total_rss 1930993664
    total_mapped_file 306728960
    total_pgpgin 406632648
    total_pgpgout 403355412
    total_swap 0
    total_pgfault 728281223
    total_pgmajfault 1724
    total_inactive_anon 46608384
    total_active_anon 1884520448
    total_inactive_file 7003344896
    total_active_file 4489052160
    total_unevictable 32768

The first half (without the `total_` prefix) contains statistics relevant
to the processes within the cgroup, excluding sub-cgroups. The second half
(with the `total_` prefix) includes sub-cgroups as well.

Some metrics are "gauges", or values that can increase or decrease. For instance,
`swap` is the amount of swap space used by the members of the cgroup.
Some others are "counters", or values that can only go up, because
they represent occurrences of a specific event. For instance, `pgfault`
indicates the number of page faults since the creation of the cgroup.

`cache`
: The amount of memory used by the processes of this control group that can be
associated precisely with a block on a block device. When you read from and
write to files on disk, this amount increases. This is the case if you use
"conventional" I/O (`open`, `read`, `write` syscalls) as well as mapped files
(with `mmap`). It also accounts for the memory used by `tmpfs` mounts, though
the reasons are unclear.

`rss`
: The amount of memory that doesn't correspond to anything on disk: stacks,
heaps, and anonymous memory maps.

`mapped_file`
: Indicates the amount of memory mapped by the processes in the control group.
It doesn't give you information about how much memory is used; it rather
tells you how it's used.

`pgfault`, `pgmajfault`
: Indicate the number of times that a process of the cgroup triggered a "page
fault" and a "major fault", respectively. A page fault happens when a process
accesses a virtual memory page that is not currently mapped to a physical
memory frame. This is a normal part of memory management. For example, a page
fault occurs when the process reads from a memory zone that has been swapped
out, or that corresponds to a memory-mapped file: in that case, the kernel
loads the page from disk and lets the CPU complete the memory access. It also
happens when the process writes to a copy-on-write memory zone: the kernel
duplicates the memory page and resumes the write operation on the process's
own copy of the page. "Major" faults happen when the kernel needs to read
data from disk. When it duplicates an existing page, or allocates an empty
page, it's a regular (or "minor") fault.

`swap`
: The amount of swap currently used by the processes in this cgroup.

`active_anon`, `inactive_anon`
: The amount of anonymous memory that has been identified has respectively
_active_ and _inactive_ by the kernel. "Anonymous" memory is the memory that is
_not_ linked to disk pages. In other words, that's the equivalent of the rss
counter described above. In fact, the very definition of the rss counter is
`active_anon` + `inactive_anon` - `tmpfs` (where tmpfs is the amount of
memory used up by `tmpfs` filesystems mounted by this control group). Now,
what's the difference between "active" and "inactive"? Pages are initially
"active"; and at regular intervals, the kernel sweeps over the memory, and tags
some pages as "inactive". Whenever they're accessed again, they're
immediately re-tagged "active". When the kernel is almost out of memory, and
time comes to swap out to disk, the kernel swaps "inactive" pages.

`active_file`, `inactive_file`
: Cache memory, with _active_ and _inactive_ similar to the _anon_ memory
above. The exact formula is `cache` = `active_file` + `inactive_file` +
`tmpfs`. The exact rules used by the kernel to move memory pages between
active and inactive sets are different from the ones used for anonymous memory,
but the general principle is the same. When the kernel needs to reclaim memory,
it's cheaper to reclaim a clean (=non modified) page from this pool, since it
can be reclaimed immediately (while anonymous pages and dirty/modified pages
need to be written to disk first).

`unevictable`
: The amount of memory that cannot be reclaimed; generally, it accounts for
memory that has been "locked" with `mlock`. It's often used by crypto
frameworks to make sure that secret keys and other sensitive material never
gets swapped out to disk.

`memory_limit`, `memsw_limit`
: These aren't really metrics, but a reminder of the limits applied to this
cgroup. The first one indicates the maximum amount of physical memory that can
be used by the processes of this control group; the second one indicates the
maximum amount of RAM+swap.

Accounting for memory in the page cache is very complex. If two
processes in different control groups both read the same file
(ultimately relying on the same blocks on disk), the corresponding
memory charge is split between the control groups. It's nice, but
it also means that when a cgroup is terminated, it could increase the
memory usage of another cgroup, because they're not splitting the cost
anymore for those memory pages.

### CPU metrics: `cpuacct.stat` {#cpu-metrics-cpuacctstat}

Now that we've covered memory metrics, everything else is
simple in comparison. CPU metrics are in the
`cpuacct` controller.

For each container, a pseudo-file `cpuacct.stat` contains the CPU usage
accumulated by the processes of the container, broken down into `user` and
`system` time. The distinction is:

- `user` time is the amount of time a process has direct control of the CPU,
  executing process code.
- `system` time is the time the kernel is executing system calls on behalf of
  the process.

Those times are expressed in ticks of 1/100th of a second, also called "user
jiffies". There are `USER_HZ` _"jiffies"_ per second, and on x86 systems,
`USER_HZ` is 100. Historically, this mapped exactly to the number of scheduler
"ticks" per second, but higher frequency scheduling and
[tickless kernels](https://lwn.net/Articles/549580/) have made the number of
ticks irrelevant.

### Block I/O metrics {#block-io-metrics}

Block I/O is accounted in the `blkio` controller.
Different metrics are scattered across different files. While you can
find in-depth details in the [blkio-controller](https://www.kernel.org/doc/Documentation/cgroup-v1/blkio-controller.txt)
file in the kernel documentation, here is a short list of the most
relevant ones:

`blkio.sectors`
: Contains the number of 512-bytes sectors read and written by the processes
member of the cgroup, device by device. Reads and writes are merged in a single
counter.

`blkio.io_service_bytes`
: Indicates the number of bytes read and written by the cgroup. It has 4
counters per device, because for each device, it differentiates between
synchronous vs. asynchronous I/O, and reads vs. writes.

`blkio.io_serviced`
: The number of I/O operations performed, regardless of their size. It also has
4 counters per device.

`blkio.io_queued`
: Indicates the number of I/O operations currently queued for this cgroup. In
other words, if the cgroup isn't doing any I/O, this is zero. The opposite is
not true. In other words, if there is no I/O queued, it doesn't mean that the
cgroup is idle (I/O-wise). It could be doing purely synchronous reads on an
otherwise quiescent device, which can therefore handle them immediately,
without queuing. Also, while it's helpful to figure out which cgroup is
putting stress on the I/O subsystem, keep in mind that it's a relative
quantity. Even if a process group doesn't perform more I/O, its queue size can
increase just because the device load increases because of other devices.

