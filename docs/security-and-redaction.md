# Security & Portfolio Redaction

This repository is intended to be public.

## Never publish

- AWS account IDs
- Full IAM role ARNs
- Lambda function ARNs
- EC2 instance IDs when they are not needed as evidence
- Access keys, secret keys, session tokens, private keys, passwords, or API tokens
- Internal hostnames, private IP addresses, or other environment-specific identifiers

## Safe examples

Use placeholders in documentation:

```text
ACCOUNT_ID=<AWS_ACCOUNT_ID>
LAMBDA_ARN=arn:aws:lambda:<REGION>:<AWS_ACCOUNT_ID>:function:<FUNCTION_NAME>
INSTANCE_ID=<INSTANCE_ID>
ROLE_ARN=arn:aws:iam::<AWS_ACCOUNT_ID>:role/<ROLE_NAME>
```

## Screenshot policy

Portfolio screenshots should have account IDs and ARNs blurred or redacted before publication. The repository documentation and code intentionally use placeholders and environment variables rather than real account-specific identifiers.

If a credential is ever exposed publicly, treat it as compromised and rotate/revoke it immediately. Blurring a credential in an image is not sufficient protection if the underlying secret exists elsewhere in repository history.
