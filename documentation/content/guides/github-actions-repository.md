---
title: Prepare a GitHub repository for Docker publishing
description: Docker Hub credentials and Git source setup for application workflows.
---

## Credentials stored as repository secrets

1. Create a Personal Access Token (PAT) from [Docker Hub](https://hub.docker.com)
   1. Go to your **Docker Hub account → Account Settings → Security**.
   2. Generate a new Access Token with **Read/Write** permissions.
   3. Use the token name from your application guide.
   4. Copy and save the token — you’ll need it in Step 4.

2. Create a repository in [Docker Hub](https://hub.docker.com/repositories/)
   1. Go to your **Docker Hub account → Create a repository**.
   2. Use the repository name from your application guide.
   3. Once created, copy and save the repository name — you’ll need it in Step 4.

3. Create a new [GitHub repository](https://github.com/new) for your project

4. Add Docker Hub credentials as GitHub repository secrets

   In your newly created GitHub repository:
   
   1. Navigate to:
   **Settings → Secrets and variables → Actions → New repository secret**.

   2. Add the following secrets:

   | Name              | Value                          |
   |-------------------|--------------------------------|
   | `DOCKER_USERNAME` | Your Docker Hub username       |
   | `DOCKERHUB_TOKEN` | Your Docker Hub access token (created in Step 1)   |
   | `DOCKERHUB_PROJECT_NAME` | Your Docker Project Name (created in Step 2)   |

   These secrets let GitHub Actions to authenticate securely with Docker Hub during automated workflows.

5. Connect Your Local Project to GitHub

   Link your local project to the GitHub repository you just created by running the following command from your project root:

   ```console
      $ git remote set-url origin https://github.com/{your-username}/{your-repository-name}.git
   ```

   >[!IMPORTANT]
   >Replace `{your-username}` and `{your-repository-name}` with your actual GitHub username and repository name.

   To confirm that your local project is correctly connected to the remote GitHub repository, run:

   ```console
   $ git remote -v
   ```

   You should see output similar to:

   ```console
   origin  https://github.com/{your-username}/{your-repository-name}.git (fetch)
   origin  https://github.com/{your-username}/{your-repository-name}.git (push)
   ```

   This confirms that your local repository is properly linked and ready to push your source code to GitHub.

6. Push Your Source Code to GitHub

   Follow these steps to commit and push your local project to your GitHub repository:

   1. Stage all files for commit.

      ```console
      $ git add -A
      ```
      This command stages all changes — including new, modified, and deleted files — preparing them for commit.


   2. Commit your changes.

      Use the commit command from your application guide.
      This command creates a commit that snapshots the staged changes with a descriptive message.  

   3. Push the code to the `main` branch.

      ```console
      $ git push -u origin main
      ```
      This command pushes your local commits to the `main` branch of the remote GitHub repository and sets the upstream branch.

Once completed, your code will be available on GitHub, and any GitHub Actions workflow you’ve configured will run automatically.

> [!NOTE]  
> Learn more about the Git commands used in this step:
> - [Git add](https://git-scm.com/docs/git-add) – Stage changes (new, modified, deleted) for commit  
> - [Git commit](https://git-scm.com/docs/git-commit) – Save a snapshot of your staged changes  
> - [Git push](https://git-scm.com/docs/git-push) – Upload local commits to your GitHub repository  
> - [Git remote](https://git-scm.com/docs/git-remote) – View and manage remote repository URLs

## Username variable and token secret

Create a GitHub repository, configure the Docker Hub credentials, and push your source code.

1. [Create a new repository](https://github.com/new) on GitHub.

2. Open the repository **Settings**, and go to **Secrets and variables** >
   **Actions**.

3. Create a new **Repository variable** named `DOCKER_USERNAME` and your Docker ID as a value.

4. Create a new [Personal Access Token (PAT)](/manuals/security/access-tokens.md#create-an-access-token) for Docker Hub. You can name this token `docker-tutorial`. Make sure access permissions include Read and Write.

5. Add the PAT as a **Repository secret** in your GitHub repository, with the name
   `DOCKERHUB_TOKEN`.

6. In your local repository on your machine, run the following command to change
   the origin to the repository you just created. Make sure you change
   `your-username` to your GitHub username and `your-repository` to the name of
   the repository you created.

   ```console
   $ git remote set-url origin https://github.com/your-username/your-repository.git
   ```

7. Follow [Push source code](#push-source-code), using the commit command from your application guide.

## Push source code

Run the following commands to stage, commit, and push your local repository to GitHub. Use the commit command from your application guide in place of the example commit below.

```console
$ git add -A
$ git commit -m "my commit"
$ git push -u origin main
```
