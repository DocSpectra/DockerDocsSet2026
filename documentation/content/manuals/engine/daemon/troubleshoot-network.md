---
title: Troubleshoot daemon networking
---

For configuration-file locations and startup options, see
[Docker daemon configuration](configuration.md#configure-the-docker-daemon).

## Networking {#networking}

### IP forwarding problems {#ip-forwarding-problems}

If you manually configure your network using `systemd-network` with systemd
version 219 or later, Docker containers may not be able to access your network.
Beginning with systemd version 220, the forwarding setting for a given network
(`net.ipv4.conf.<interface>.forwarding`) defaults to off. This setting prevents
IP forwarding. It also conflicts with Docker's behavior of enabling the
`net.ipv4.conf.all.forwarding` setting within containers.

To work around this on RHEL, CentOS, or Fedora, edit the `<interface>.network`
file in `/usr/lib/systemd/network/` on your Docker host, for example,
`/usr/lib/systemd/network/80-container-host0.network`.

Add the following block within the `[Network]` section.

```systemd
[Network]
...
IPForward=kernel
# OR
IPForward=true
```

This configuration allows IP forwarding from the container as expected.

### DNS resolver issues {#dns-resolver-issues}

```console
DNS resolver found in resolv.conf and containers can't use it
```

Linux desktop environments often have a network manager program running, that
uses `dnsmasq` to cache DNS requests by adding them to `/etc/resolv.conf`. The
`dnsmasq` instance runs on a loopback address such as `127.0.0.1` or
`127.0.1.1`. It speeds up DNS look-ups and provides DHCP services. Such a
configuration doesn't work within a Docker container. The Docker container uses
its own network namespace, and resolves loopback addresses such as `127.0.0.1`
to itself, and it's unlikely to be running a DNS server on its own loopback
address.

If Docker detects that no DNS server referenced in `/etc/resolv.conf` is a fully
functional DNS server, the following warning occurs:

```text
WARNING: Local (127.0.0.1) DNS resolver found in resolv.conf and containers
can't use it. Using default external servers : [8.8.8.8 8.8.4.4]
```

If you see this warning, first check to see if you use `dnsmasq`:

```console
$ ps aux | grep dnsmasq
```

If your container needs to resolve hosts which are internal to your network, the
public nameservers aren't adequate. You have two choices:

- Specify DNS servers for Docker to use.
- Turn off `dnsmasq`.

  Turning off `dnsmasq` adds the IP addresses of actual DNS nameservers to
  `/etc/resolv.conf`, and you lose the benefits of `dnsmasq`.

You only need to use one of these methods.

### Specify DNS servers for Docker {#specify-dns-servers-for-docker}

The default location of the configuration file is `/etc/docker/daemon.json`. You
can change the location of the configuration file using the `--config-file`
daemon flag. The following instruction assumes that the location of the
configuration file is `/etc/docker/daemon.json`.

1. Create or edit the Docker daemon configuration file, which defaults to
   `/etc/docker/daemon.json` file, which controls the Docker daemon
   configuration.

   ```console
   $ sudo nano /etc/docker/daemon.json
   ```

2. Add a `dns` key with one or more DNS server IP addresses as values.

   ```json
   {
     "dns": ["8.8.8.8", "8.8.4.4"]
   }
   ```

   If the file has existing contents, you only need to add or edit the `dns`
   line. If your internal DNS server can't resolve public IP addresses, include
   at least one DNS server that can. Doing so allows you to connect to Docker
   Hub, and your containers to resolve internet domain names.

   Save and close the file.

3. Restart the Docker daemon.

   ```console
   $ sudo service docker restart
   ```

4. Verify that Docker can resolve external IP addresses by trying to pull an
   image:

   ```console
   $ docker pull hello-world
   ```

5. If necessary, verify that Docker containers can resolve an internal hostname
   by pinging it.

   ```console
   $ docker run --rm -it alpine ping -c4 <my_internal_host>

   PING google.com (192.168.1.2): 56 data bytes
   64 bytes from 192.168.1.2: seq=0 ttl=41 time=7.597 ms
   64 bytes from 192.168.1.2: seq=1 ttl=41 time=7.635 ms
   64 bytes from 192.168.1.2: seq=2 ttl=41 time=7.660 ms
   64 bytes from 192.168.1.2: seq=3 ttl=41 time=7.677 ms
   ```

### Turn off `dnsmasq` {#turn-off-dnsmasq}

{{< tabs >}}
{{< tab name="Ubuntu" >}}

If you prefer not to change the Docker daemon's configuration to use a specific
IP address, follow these instructions to turn off `dnsmasq` in NetworkManager.

1. Edit the `/etc/NetworkManager/NetworkManager.conf` file.

2. Comment out the `dns=dnsmasq` line by adding a `#` character to the beginning
   of the line.

   ```text
   # dns=dnsmasq
   ```

   Save and close the file.

3. Restart both NetworkManager and Docker. As an alternative, you can reboot
   your system.

   ```console
   $ sudo systemctl restart network-manager
   $ sudo systemctl restart docker
   ```

{{< /tab >}}
{{< tab name="RHEL, CentOS, or Fedora" >}}

To turn off `dnsmasq` on RHEL, CentOS, or Fedora:

1. Turn off the `dnsmasq` service:

   ```console
   $ sudo systemctl stop dnsmasq
   $ sudo systemctl disable dnsmasq
   ```

2. Configure the DNS servers manually using the
   [Red Hat documentation](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/configuring_and_managing_networking/configuring-the-order-of-dns-servers_configuring-and-managing-networking).

{{< /tab >}}
{{< /tabs >}}

### Docker networks disappearing {#docker-networks-disappearing}

If a Docker network, such as the `docker0` bridge or a custom network, randomly
disappears or otherwise appears to be working incorrectly, it could be because
another service is interfering with or modifying Docker interfaces. Tools that
manage networking interfaces on the host are known to sometimes also
inappropriately modify Docker interfaces.

Refer to the following sections for instructions on how to configure your
network manager to set Docker interfaces as un-managed, depending on the
network management tools that exist on the host:

- If `netscript` is installed, consider [uninstalling it](#uninstall-netscript)
- Configure the network manager to [treat Docker interfaces as un-managed](#un-manage-docker-interfaces)
- If you're using Netplan, you may need to [apply a custom Netplan configuration](#prevent-netplan-from-overriding-network-configuration)

#### Uninstall `netscript` {#uninstall-netscript}

If `netscript` is installed on your system, you can likely fix this issue by
uninstalling it. For example, on a Debian-based system:

```console
$ sudo apt-get remove netscript-2.4
```

#### Un-manage Docker interfaces {#un-manage-docker-interfaces}

In some cases, the network manager will attempt to manage Docker interfaces by
default. You can try to explicitly flag Docker networks as un-managed by
editing your system's network configuration settings.

{{< tabs >}}
{{< tab name="NetworkManager" >}}

If you're using `NetworkManager`, edit your system network configuration under
`/etc/network/interfaces`

1. Create a file at `/etc/network/interfaces.d/20-docker0` with the following
   contents:

   ```text
   iface docker0 inet manual
   ```

   Note that this example configuration only "un-manages" the default `docker0`
   bridge, not custom networks.

2. Restart `NetworkManager` for the configuration change to take effect.

   ```console
   $ systemctl restart NetworkManager
   ```

3. Verify that the `docker0` interface has the `unmanaged` state.

   ```console
   $ nmcli device
   ```

{{< /tab >}}
{{< tab name="systemd-networkd" >}}

If you're running Docker on a system using `systemd-networkd` as a networking
daemon, configure the Docker interfaces as un-managed by creating configuration
files under `/etc/systemd/network`:

1. Create `/etc/systemd/network/docker.network` with the following contents:

   ```ini
   # Ensure that the Docker interfaces are un-managed

   [Match]
   Name=docker0 br-* veth*

   [Link]
   Unmanaged=yes

   ```

2. Reload the configuration.

   ```console
   $ sudo systemctl restart systemd-networkd
   ```

3. Restart the Docker daemon.

   ```console
   $ sudo systemctl restart docker
   ```

4. Verify that the Docker interfaces have the `unmanaged` state.

   ```console
   $ networkctl
   ```

{{< /tab >}}
{{< /tabs >}}

### Prevent Netplan from overriding network configuration {#prevent-netplan-from-overriding-network-configuration}

On systems that use [Netplan](https://netplan.io/) through
[`cloud-init`](https://cloudinit.readthedocs.io/en/latest/index.html), you may
need to apply a custom configuration to prevent `netplan` from overriding the
network manager configuration:

1. Follow the steps in [Un-manage Docker interfaces](#un-manage-docker-interfaces)
   for creating the network manager configuration.
2. Create a `netplan` configuration file under `/etc/netplan/50-cloud-init.yml`.

   The following example configuration file is a starting point.
   Adjust it to match the interfaces you want to un-manage.
   Incorrect configuration can lead to network connectivity issues.

   ```yaml {title="/etc/netplan/50-cloud-init.yml"}
   network:
     ethernets:
       all:
         dhcp4: true
         dhcp6: true
         match:
           # edit this filter to match whatever makes sense for your system
           name: en*
     renderer: networkd
     version: 2
   ```

3. Apply the new Netplan configuration.

   ```console
   $ sudo netplan apply
   ```

4. Restart the Docker daemon:

   ```console
   $ sudo systemctl restart docker
   ```

5. Verify that the Docker interfaces have the `unmanaged` state.

   ```console
   $ networkctl
   ```

