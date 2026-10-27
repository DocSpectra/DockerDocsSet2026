---
title: Create and check a Docker GitHub Actions workflow
description: Workflow editor steps, publication checks, and branch protection.
---

## Create the workflow file

1. Go to your repository on GitHub and select the **Actions** tab in the top menu.

2. Select **Set up a workflow yourself** when prompted.

    This opens an inline editor to create a new workflow file. By default, it will be saved to:
   `.github/workflows/main.yml`

   
3. Add the workflow configuration from your application guide to the new file.


## Run and verify tagged images

Follow [Verify repository publication](#verify-repository-publication) to commit and push your workflow file, monitor the run, and check Docker Hub.

In the **Actions** tab, click into the workflow run to follow each step: **build**, **test**, and (if successful) **push**.

After a successful workflow run, check the image in your [Docker Hub repositories](https://hub.docker.com/repositories):

- Repository name: `${your-repository-name}`
- Tags include:
  - `latest` – represents the most recent successful build; ideal for quick testing or deployment.
  - `<short-sha>` – a unique identifier based on the commit hash, useful for version tracking, rollbacks, and traceability.

> [!TIP] Protect your main branch
> To maintain code quality and prevent accidental direct pushes, enable branch protection rules:
>  - Navigate to your **GitHub repo → Settings → Branches**.
>  - Under Branch protection rules, click **Add rule**.
>  - Specify `main` as the branch name.
>  - Enable options like:
>     - *Require a pull request before merging*.
>     - *Require status checks to pass before merging*.
>
>  This ensures that only tested and reviewed code is merged into `main` branch.

## Verify repository publication

Save the workflow file and run the job.

1. Select **Commit changes...** and push the changes to the `main` branch.

   After pushing the commit, the workflow starts automatically.

2. Go to the **Actions** tab. It displays the workflow.

   Selecting the workflow shows you the breakdown of all the steps.

3. When the workflow is complete, go to your
   [repositories on Docker Hub](https://hub.docker.com/repositories).

   If you see the new repository in that list, it means the GitHub Actions
   successfully pushed the image to Docker Hub.
