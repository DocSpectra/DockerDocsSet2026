---
title: Check kernel compatibility and swap accounting
---

## Kernel compatibility {#kernel-compatibility}

Docker can't run correctly if your kernel is older than version 3.10, or if it's
missing kernel modules. To check kernel compatibility, you can download and run
the
[`check-config.sh`](https://raw.githubusercontent.com/docker/docker/master/contrib/check-config.sh)
script.

```console
$ curl https://raw.githubusercontent.com/docker/docker/master/contrib/check-config.sh > check-config.sh

$ bash ./check-config.sh
```

The script only works on Linux.

## Kernel cgroup swap limit capabilities {#kernel-cgroup-swap-limit-capabilities}

On Ubuntu or Debian hosts, you may see messages similar to the following when
working with an image.

```text
WARNING: Your kernel does not support swap limit capabilities. Limitation discarded.
```

If you don't need these capabilities, you can ignore the warning.

You can turn on these capabilities on Ubuntu or Debian by following these
instructions. Memory and swap accounting incur an overhead of about 1% of the
total available memory and a 10% overall performance degradation, even when
Docker isn't running.

1. Log into the Ubuntu or Debian host as a user with `sudo` privileges.

2. Edit the `/etc/default/grub` file. Add or edit the `GRUB_CMDLINE_LINUX` line
   to add the following two key-value pairs:

   ```text
   GRUB_CMDLINE_LINUX="cgroup_enable=memory swapaccount=1"
   ```

   Save and close the file.

3. Update the GRUB boot loader.

   ```console
   $ sudo update-grub
   ```

   An error occurs if your GRUB configuration file has incorrect syntax. In this
   case, repeat steps 2 and 3.

   The changes take effect when you reboot the system.

