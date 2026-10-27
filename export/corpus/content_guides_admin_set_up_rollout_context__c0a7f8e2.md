---
title: Docker rollout features, stakeholders, and integrations
---

## Features covered

This guide covers the following Docker features:

- [Organizations](/manuals/admin/organization/_index.md): The core structure
  for managing your Docker environment, grouping users, teams, and image
  repositories. Your organization was created with your subscription and is
  managed by one or more owners. Users signed into the organization are
  assigned seats based on the purchased subscription.
- [Enforce sign-in](/manuals/enterprise/security/enforce-sign-in/_index.md):
  By default, Docker Desktop doesn't require sign-in. You can configure
  settings to enforce this and ensure your developers sign in to your
  Docker organization.
- [SSO](/manuals/enterprise/security/single-sign-on/_index.md): Without SSO,
  user management in a Docker organization is manual. Setting
  up an SSO connection between your identity provider and Docker ensures
  compliance with your security policy and automates user provisioning. Adding
  SCIM further automates user provisioning and de-provisioning.
- General and security settings: Configuring key settings ensures smooth
  onboarding and usage of Docker products within your environment. You can also
  enable security features based on your company's specific security needs.

## Who needs to be involved

- Docker organization owner: Must be involved in the process and is required
  for several key steps
- DNS team: Needed during the SSO setup to verify the company domain
- MDM team: Responsible for distributing Docker-specific configuration files to
  developer machines
- Identity Provider team: Required for configuring the identity provider and
  establishing the SSO connection during setup
- Development lead: A development lead with knowledge of Docker configurations
  to help establish a baseline for developer settings
- IT team: An IT representative familiar with company desktop policies to
  assist with aligning Docker configuration to those policies
- Infosec: A security team member with knowledge of company development
  security policies to help configure security features
- Docker testers: A small group of developers to test the new settings and
  configurations before full deployment

## Tools integration

This guide covers integration with:

- Okta
- Entra ID SAML 2.0
- Azure Connect (OIDC)
- MDM solutions like Intune
