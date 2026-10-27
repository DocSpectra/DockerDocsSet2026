---
title: Image and registry access control scope
---

## Shared prerequisites

Before configuring Registry Access Management or Image Access Management, you must:

- [Enforce sign-in](/manuals/enterprise/security/enforce-sign-in/_index.md). Registry Access Management and Image Access Management only take effect when users are signed in to Docker Desktop with organization credentials.
- Use [personal access tokens (PATs)](/manuals/security/access-tokens.md) for authentication (Organization access tokens aren't supported)
- Have a Docker Business subscription


## Registry controls

Registry Access Management (RAM) lets administrators control which container registries developers can access through Docker Desktop. This DNS-level filtering ensures developers only pull and push images from approved registries, improving supply chain security.

RAM works with all registry types including cloud services, on-premises registries, and registry mirrors. You can allow any hostname or domain, but must include redirect domains (like `s3.amazonaws.com` for some registries) in your allowlist.

### Supported registries

Registry Access Management works with any container registry, including:

- Docker Hub (allowed by default)
- Cloud registries: Amazon ECR, Google Artifact Registry, Azure Container Registry
- Git-based registries: GitHub Container Registry, GitLab Container Registry
- On-premises solutions: Nexus, Artifactory, Harbor
- Registry mirrors: Including Docker Hub mirrors

### Registry limits and platform constraints

Registry Access Management has these limits and platform-specific behaviors:

- Maximum allowlist size: 100 registries or domains per organization
- DNS-based filtering: Restrictions work at the hostname level, not IP addresses
- Redirect domains required: Must include all domains a registry redirects to (CDN endpoints, storage services)
- Windows containers: Windows image operations aren't restricted by default. Turn on **Use proxy for Windows Docker daemon** in Docker Desktop settings to apply restrictions
- WSL 2 requirements: Requires Linux kernel 5.4 or later, restrictions apply to all WSL 2 distributions

### Build and deployment restrictions

These scenarios are not restricted by Registry Access Management:

- Docker buildx with Kubernetes driver
- Docker buildx with custom Docker-container driver
- Some Docker Debug and Kubernetes image pulls (even if Docker Hub is blocked)
- Images previously cached by registry mirrors may still be blocked if the source registry is restricted

### Security bypass considerations

Users can potentially bypass Registry Access Management through:

- Local proxies or DNS manipulation
- Signing out of Docker Desktop (unless sign-in is enforced)
- Network-level modifications outside Docker Desktop's control

To maximize security effectiveness:

- [Enforce sign-in](/manuals/enterprise/security/enforce-sign-in/_index.md) to prevent bypass through sign-out
- Implement additional network-level controls for complete protection
- Use Registry Access Management as part of a broader security strategy

### Registry allowlist best practices

- Include all registry domains: Some registries redirect to multiple
domains. For AWS ECR, include:

    ```text
    your-account.dkr.ecr.us-west-2.amazonaws.com
    amazonaws.com
    s3.amazonaws.com
    ```

- Practice regular allowlist maintenance:
    - Remove unused registries periodically
    - Add newly approved registries as needed
    - Update domain names that may have changed
    - Monitor registry usage through Docker Desktop analytics
- Test configuration changes:
    - Verify registry access after making allowlist updates
    - Check that all necessary redirect domains are included
    - Ensure development workflows aren't disrupted
    - Combine with [Enhanced Container Isolation](/manuals/enterprise/security/hardened-desktop/enhanced-container-isolation/_index.md) for comprehensive protection
    
## Image controls

Image Access Management lets administrators control which types of images developers can pull from Docker Hub. This prevents developers from accidentally using untrusted community images that could pose security risks to your organization.

With Image Access Management, you can restrict access to:

- Docker Official Images: Curated images maintained by Docker
- Docker Verified Publisher Images: Images from trusted commercial publishers
- Organization images: Your organization's private repositories
- Community images: Public images from individual developers

You can also use a repository allowlist to approve specific repositories that bypass all other access controls.

### Who should use Image Access Management?

Image Access Management helps prevent supply chain attacks by ensuring developers only use trusted container images. For example, a developer building a new application might accidentally use a malicious community image as a component. Image Access Management prevents this by restricting access to only approved image types.

Common security scenarios include:

- Prevent use of unmaintained or malicious community images
- Ensure developers use only vetted, official base images
- Control access to commercial third-party images
- Maintain consistent security standards across development teams

Use the repository allowlist when you need to:

- Grant access to specific vetted community images
- Allow essential third-party tools that don't fall under official categories
- Provide exceptions to general image access policies for specific business requirements

### Best practices

- Start with the most restrictive policy and gradually expand based on legitimate business needs:
   1. Start with Docker Official Images and Organization images
   2. If needed, add Docker Verified Publisher Images for commercial tools
   3. Carefully evaluate community images only for specific, vetted use cases
   4. Use the repository allowlist sparingly. Only add repositories that have been thoroughly vetted and approved through your organization's security review process
- Monitor usage patterns: Review which images developers are attempting to pull, identify legitimate requests for additional image types, regularly audit approved image categories for continued relevance, and use Docker Desktop analytics to monitor usage patterns.
- Regularly review the repository allow list: Periodically audit the repositories in your allowlist to ensure they remain necessary and trustworthy, and remove any that are no longer needed or maintained.

### Scope and bypass considerations

- Image Access Management only controls access to Docker Hub images. Images from other registries aren't affected by these policies. Use Registry Access Management to control access to other registries.
- Users can potentially bypass Image Access Management by signing out of Docker Desktop (unless sign-in is enforced), using images from other registries that aren't restricted, or using registry mirrors or proxies. Enforce sign-in and combine with Registry Access Management for comprehensive control.
- Image restrictions apply to Dockerfile `FROM` instructions, Docker Compose services using restricted images will fail, multi-stage builds may be affected if intermediate images are restricted, and CI/CD pipelines using diverse image types may be impacted.

### Layer security controls

- Layer security controls: Image Access Management works best with Registry Access Management to control which registries developers can access, [Enhanced Container Isolation](enhanced-container-isolation/_index.md) to secure containers at runtime, and [Settings Management](settings-management/policy-model.md) to control Docker Desktop configuration.
