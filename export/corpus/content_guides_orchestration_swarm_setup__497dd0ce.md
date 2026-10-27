---
title: Enable and verify Swarm in Docker Desktop
description: Initialize Swarm and verify a test service.
---

## Enable Docker Swarm

Docker Desktop runs primarily on Docker Engine, which has everything you need to run a Swarm built in. Follow the setup and validation instructions appropriate for your operating system:

{{< tabs group="os" >}}
{{< tab name="Mac" >}}

### Mac

1. Open a terminal, and initialize Docker Swarm mode:

   ```console
   $ docker swarm init
   ```

   If all goes well, you should see a message similar to the following:

   ```shell
   Swarm initialized: current node (tjjggogqpnpj2phbfbz8jd5oq) is now a manager.

   To add a worker to this swarm, run the following command:

       docker swarm join --token SWMTKN-1-3e0hh0jd5t4yjg209f4g5qpowbsczfahv2dea9a1ay2l8787cf-2h4ly330d0j917ocvzw30j5x9 192.168.65.3:2377

   To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.
   ```

2. Run a simple Docker service that uses an alpine-based filesystem, and isolates a ping to 8.8.8.8:

   ```console
   $ docker service create --name demo alpine:latest ping 8.8.8.8
   ```

3. Check that your service created one running container:

   ```console
   $ docker service ps demo
   ```

   You should see something like:

   ```shell
   ID                  NAME                IMAGE               NODE                DESIRED STATE       CURRENT STATE           ERROR               PORTS
   463j2s3y4b5o        demo.1              alpine:latest       docker-desktop      Running             Running 8 seconds ago
   ```

4. Check that you get the logs you'd expect for a ping process:

   ```console
   $ docker service logs demo
   ```

   You should see the output of a healthy ping process:

   ```shell
   demo.1.463j2s3y4b5o@docker-desktop    | PING 8.8.8.8 (8.8.8.8): 56 data bytes
   demo.1.463j2s3y4b5o@docker-desktop    | 64 bytes from 8.8.8.8: seq=0 ttl=37 time=13.005 ms
   demo.1.463j2s3y4b5o@docker-desktop    | 64 bytes from 8.8.8.8: seq=1 ttl=37 time=13.847 ms
   demo.1.463j2s3y4b5o@docker-desktop    | 64 bytes from 8.8.8.8: seq=2 ttl=37 time=41.296 ms
   ...
   ```

5. Finally, tear down your test service:

   ```console
   $ docker service rm demo
   ```

{{< /tab >}}
{{< tab name="Windows" >}}

### Windows

1. Open a PowerShell, and initialize Docker Swarm mode:

   ```console
   $ docker swarm init
   ```

   If all goes well, you should see a message similar to the following:

   ```shell
   Swarm initialized: current node (tjjggogqpnpj2phbfbz8jd5oq) is now a manager.

   To add a worker to this swarm, run the following command:

       docker swarm join --token SWMTKN-1-3e0hh0jd5t4yjg209f4g5qpowbsczfahv2dea9a1ay2l8787cf-2h4ly330d0j917ocvzw30j5x9 192.168.65.3:2377

   To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.
   ```

2. Run a simple Docker service that uses an alpine-based filesystem, and isolates a ping to 8.8.8.8:

   ```console
   $ docker service create --name demo alpine:latest ping 8.8.8.8
   ```

3. Check that your service created one running container:

   ```console
   $ docker service ps demo
   ```

   You should see something like:

   ```shell
   ID                  NAME                IMAGE               NODE                DESIRED STATE       CURRENT STATE           ERROR               PORTS
   463j2s3y4b5o        demo.1              alpine:latest       docker-desktop      Running             Running 8 seconds ago
   ```

4. Check that you get the logs you'd expect for a ping process:

   ```console
   $ docker service logs demo
   ```

   You should see the output of a healthy ping process:

   ```shell
   demo.1.463j2s3y4b5o@docker-desktop    | PING 8.8.8.8 (8.8.8.8): 56 data bytes
   demo.1.463j2s3y4b5o@docker-desktop    | 64 bytes from 8.8.8.8: seq=0 ttl=37 time=13.005 ms
   demo.1.463j2s3y4b5o@docker-desktop    | 64 bytes from 8.8.8.8: seq=1 ttl=37 time=13.847 ms
   demo.1.463j2s3y4b5o@docker-desktop    | 64 bytes from 8.8.8.8: seq=2 ttl=37 time=41.296 ms
   ...
   ```

5. Finally, tear down your test service:

   ```console
   $ docker service rm demo
   ```

{{< /tab >}}
{{< /tabs >}}
