---
title: Socket Firewall variants for DHI Node.js images
description: Socket Firewall interception during Node.js dependency installation.
---

DHI provides `-sfw` (Socket Firewall) variants for Node.js images. Socket Firewall intercepts `npm` and `yarn` commands during the build to detect and block malicious packages before they execute install scripts.
