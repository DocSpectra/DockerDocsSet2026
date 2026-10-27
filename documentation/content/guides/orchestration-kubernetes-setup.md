---
title: Enable and verify Kubernetes in Docker Desktop
description: Set up Kubernetes and verify a test pod.
---

## Turn on Kubernetes

Docker Desktop sets up Kubernetes for you quickly and easily. Follow the setup and validation instructions appropriate for your operating system:

{{< tabs group="os" >}}
{{< tab name="Mac and Linux" >}}

### Mac

1.  From the Docker Dashboard, navigate to **Settings**, and select the **Kubernetes** tab.

2.  Select the checkbox labeled **Enable Kubernetes**, and select **Apply**. Docker Desktop automatically sets up Kubernetes for you. You'll know that Kubernetes has been successfully enabled when you see a green light beside 'Kubernetes _running_' in **Settings**.

3.  To confirm that Kubernetes is up and running, create a text file called `pod.yaml` with the following content:

    ```yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: demo
    spec:
      containers:
        - name: testpod
          image: alpine:latest
          command: ["ping", "8.8.8.8"]
    ```

    This describes a pod with a single container, isolating a simple ping to 8.8.8.8.

4.  In a terminal, navigate to where you created `pod.yaml` and create your pod:

    ```console
    $ kubectl apply -f pod.yaml
    ```

5.  Check that your pod is up and running:

    ```console
    $ kubectl get pods
    ```

    You should see something like:

    ```shell
    NAME      READY     STATUS    RESTARTS   AGE
    demo      1/1       Running   0          4s
    ```

6.  Check that you get the logs you'd expect for a ping process:

    ```console
    $ kubectl logs demo
    ```

    You should see the output of a healthy ping process:

    ```shell
    PING 8.8.8.8 (8.8.8.8): 56 data bytes
    64 bytes from 8.8.8.8: seq=0 ttl=37 time=21.393 ms
    64 bytes from 8.8.8.8: seq=1 ttl=37 time=15.320 ms
    64 bytes from 8.8.8.8: seq=2 ttl=37 time=11.111 ms
    ...
    ```

7.  Finally, tear down your test pod:

    ```console
    $ kubectl delete -f pod.yaml
    ```

{{< /tab >}}
{{< tab name="Windows" >}}

### Windows

1. From the Docker Dashboard, navigate to **Settings**, and select the **Kubernetes** tab.

2. Select the checkbox labeled **Enable Kubernetes**, and select **Apply**. Docker Desktop automatically sets up Kubernetes for you. You'll know that Kubernetes has been successfully enabled when you see a green light beside 'Kubernetes _running_' in the **Settings** menu.

3. To confirm that Kubernetes is up and running, create a text file called `pod.yaml` with the following content:

   ```yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: demo
   spec:
     containers:
       - name: testpod
         image: alpine:latest
         command: ["ping", "8.8.8.8"]
   ```

   This describes a pod with a single container, isolating a simple ping to 8.8.8.8.

4. In PowerShell, navigate to where you created `pod.yaml` and create your pod:

   ```console
   $ kubectl apply -f pod.yaml
   ```

5. Check that your pod is up and running:

   ```console
   $ kubectl get pods
   ```

   You should see something like:

   ```shell
   NAME      READY     STATUS    RESTARTS   AGE
   demo      1/1       Running   0          4s
   ```

6. Check that you get the logs you'd expect for a ping process:

   ```console
   $ kubectl logs demo
   ```

   You should see the output of a healthy ping process:

   ```shell
   PING 8.8.8.8 (8.8.8.8): 56 data bytes
   64 bytes from 8.8.8.8: seq=0 ttl=37 time=21.393 ms
   64 bytes from 8.8.8.8: seq=1 ttl=37 time=15.320 ms
   64 bytes from 8.8.8.8: seq=2 ttl=37 time=11.111 ms
   ...
   ```

7. Finally, tear down your test pod:

   ```console
   $ kubectl delete -f pod.yaml
   ```

{{< /tab >}}
{{< /tabs >}}
