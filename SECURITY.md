# Security Policy

## Public repository rule

This repository contains a portfolio implementation and must not contain production secrets or sensitive AWS identifiers that are not necessary for demonstrating the design.

Never commit:

- AWS access keys or secret access keys
- STS session tokens
- Private keys or certificates containing private material
- Passwords or API tokens
- Unredacted account IDs or full environment-specific ARNs unless there is a deliberate reason to publish them
- Internal IP addresses, hostnames, or other confidential infrastructure details

## If a credential is exposed

Treat it as compromised immediately. Revoke or rotate it in AWS, inspect CloudTrail for unexpected use, remove the secret from the working tree, and rewrite Git history when appropriate.

Removing a secret from the latest commit is not enough if it remains in Git history.

## Reporting

For this portfolio project, open a GitHub issue for non-sensitive documentation or implementation problems. Do not post credentials, tokens, or other secrets in an issue.
