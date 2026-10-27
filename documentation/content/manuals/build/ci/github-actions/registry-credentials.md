---
title: Configure Docker Hub credentials for GitHub Actions
---

## Configure your GitHub repository

To push the image you build to Docker Hub, you must authenticate with your Docker credentials (username and access
token) as part of the GitHub Actions workflow.

For instructions on how to create a Docker access token, see
[Create and manage access tokens](/manuals/security/access-tokens.md).

Once you have your Docker credentials ready, add the credentials to your GitHub
repository so you can use them in GitHub Actions:

1. Open your repository's **Settings**.
2. Under **Security**, go to **Secrets and variables > Actions**.
3. Under **Secrets**, create a new repository secret with the name used by the workflow's `secrets` expression,
   containing your Docker access token.
4. Next, under **Variables**, create a repository variable with the name used by the workflow's `vars` expression
   containing your Docker Hub username.
