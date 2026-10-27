---
title: Back up and recover a Swarm
---

## Context and caveats

Read [Plan managers and maintain quorum](manager-quorum.md) and [Raft consensus](raft.md).

## Back up the swarm

Docker manager nodes store the swarm state and manager logs in the
`/var/lib/docker/swarm/` directory. This data includes the keys used to encrypt
the Raft logs. Without these keys, you cannot restore the swarm.

You can back up the swarm using any manager. Use the following procedure.

1.  If the swarm has auto-lock enabled, you need the unlock key
    to restore the swarm from backup. Retrieve the unlock key if necessary and
    store it in a safe location. If you are unsure, read
    [Lock your swarm to protect its encryption key](swarm_manager_locking.md).

2.  Stop Docker on the manager before backing up the data, so that no data is
    being changed during the backup. It is possible to take a backup while the
    manager is running (a "hot" backup), but this is not recommended and your
    results are less predictable when restoring. While the manager is down,
    other nodes continue generating swarm data that is not part of this backup.

    > [!NOTE]
    > 
    > Be sure to maintain the quorum of swarm managers. During the
    > time that a manager is shut down, your swarm is more vulnerable to
    > losing the quorum if further nodes are lost. The number of managers you
    > run is a trade-off. If you regularly take down managers to do backups,
    > consider running a five manager swarm, so that you can lose an additional
    > manager while the backup is running, without disrupting your services.

3.  Back up the entire `/var/lib/docker/swarm` directory.

4.  Restart the manager.

To restore, see [Restore from a backup](#restore-from-a-backup). 

## Recover from disaster

### Restore from a backup

After backing up the swarm as described in
[Back up the swarm](#back-up-the-swarm), use the following procedure to
restore the data to a new swarm.

1.  Shut down Docker on the target host machine for the restored swarm.

2.  Remove the contents of the `/var/lib/docker/swarm` directory on the new
    swarm.

3.  Restore the `/var/lib/docker/swarm` directory with the contents of the
    backup.

    > [!NOTE]
    > 
    > The new node uses the same encryption key for on-disk
    > storage as the old one. It is not possible to change the on-disk storage
    > encryption keys at this time.
    >
    > In the case of a swarm with auto-lock enabled, the unlock key is also the
    > same as on the old swarm, and the unlock key is needed to restore the
    > swarm.

4.  Start Docker on the new node. Unlock the swarm if necessary. Re-initialize
    the swarm using the following command, so that this node does not attempt
    to connect to nodes that were part of the old swarm, and presumably no
    longer exist.

    ```console
    $ docker swarm init --force-new-cluster
    ```

5.  Verify that the state of the swarm is as expected. This may include
    application-specific tests or simply checking the output of
    `docker service ls` to be sure that all expected services are present.

6.  If you use auto-lock,
    [rotate the unlock key](swarm_manager_locking.md#rotate-the-unlock-key).

7.  Add manager and worker nodes to bring your new swarm up to operating
    capacity.

8.  Reinstate your previous backup regimen on the new swarm.

### Recover from losing the quorum

Swarm is resilient to failures and can recover from any number
of temporary node failures (machine reboots or crash with restart) or other
transient errors. However, a swarm cannot automatically recover if it loses a
quorum. Tasks on existing worker nodes continue to run, but administrative
tasks are not possible, including scaling or updating services and joining or
removing nodes from the swarm. The best way to recover is to bring the missing
manager nodes back online. If that is not possible, continue reading for some
options for recovering your swarm.

In a swarm of `N` managers, a quorum (a majority) of manager nodes must always
be available. For example, in a swarm with five managers, a minimum of three must be
operational and in communication with each other. In other words, the swarm can
tolerate up to `(N-1)/2` permanent failures beyond which requests involving
swarm management cannot be processed. These types of failures include data
corruption or hardware failures.

If you lose the quorum of managers, you cannot administer the swarm. If you have
lost the quorum and you attempt to perform any management operation on the swarm,
an error occurs:

```text
Error response from daemon: rpc error: code = 4 desc = context deadline exceeded
```

The best way to recover from losing the quorum is to bring the failed nodes back
online. If you can't do that, the only way to recover from this state is to use
the `--force-new-cluster` action from a manager node. This removes all managers
except the manager the command was run from. The quorum is achieved because
there is now only one manager. Promote nodes to be managers until you have the
desired number of managers.

From the node to recover, run:

```console
$ docker swarm init --force-new-cluster --advertise-addr node01:2377
```

When you run the `docker swarm init` command with the `--force-new-cluster`
flag, the Docker Engine where you run the command becomes the manager node of a
single-node swarm which is capable of managing and running services. The manager
has all the previous information about services and tasks, worker nodes are
still part of the swarm, and services are still running. You need to add or
re-add  manager nodes to achieve your previous task distribution and ensure that
you have enough managers to maintain high availability and prevent losing the
quorum.
