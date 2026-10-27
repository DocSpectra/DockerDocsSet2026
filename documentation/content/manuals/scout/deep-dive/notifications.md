---
title: Docker Scout notification settings
---

The [Notification settings](https://scout.docker.com/settings/notifications)
page is where you can change the preferences for receiving notifications from
Docker Scout. Notification settings are personal, and changing notification
settings only affects your personal account, not the entire organization.

The purpose of notifications in Docker Scout is to raise awareness about
upstream changes that affect you. Docker Scout will notify you about when a new
vulnerability is disclosed in a security advisory, and it affects one or more
of your images. You will not receive notifications about changes to
vulnerability exposure or policy compliance as a result of pushing a new image.

> [!NOTE]
>
> Notifications are only triggered for the _last pushed_ image tags for each
> repository. "Last pushed" refers to the image tag that was most recently
> pushed to the registry and analyzed by Docker Scout. If the last pushed image
> is not affected by a newly disclosed CVE, then no notification will be
> triggered.

The available notification settings are:

- **Repository scope**

  Here you can select whether you want to enable notifications for all
  repositories, or only for specific repositories. These settings apply to the
  currently selected organization, and can be changed for each organization you
  are a member of.
  - **All repositories**: select this option to receive notifications for all
    repositories that you have access to.
  - **Specific repositories**: select this option to receive notifications for
    specific repositories. You can then enter the names of repositories you
    want to receive notifications for.

- **Delivery preferences**

  These settings control how you receive notifications from Docker Scout. They
  apply to all organizations that you're a member of.
  - **Notification pop-ups**: select this check-box to receive notification
    pop-up messages in the Docker Scout Dashboard.
  - **OS notifications**: select this check-box to receive OS-level notifications
    from your browser if you have the Docker Scout Dashboard open in a browser
    tab.

  To enable OS notifications, Docker Scout needs permissions to send
  notifications using the browser API.

From this page, you can also go to the settings for Team collaboration
integrations, such as the Slack
integration.

You can also configure your notification settings in Docker Desktop by going
to **Settings** > **Notifications**.
