# AWS Evidence Gallery

This folder is reserved for **sanitized** AWS console evidence.

Recommended portfolio captures:

1. EC2 instance showing the automation tag.
2. Start Lambda successful test execution.
3. Stop Lambda successful test execution.
4. EventBridge Scheduler start schedule.
5. EventBridge Scheduler stop schedule.
6. CloudWatch Lambda log groups or execution logs.
7. IAM policy showing the required EC2 permissions.
8. Architecture diagram.

## Redaction checklist

Before committing a screenshot, verify that it contains no:

- AWS account ID
- Full ARN
- Access key or secret
- Session token
- Private key
- Internal IP address or hostname
- Unnecessary instance ID

Use the naming pattern:

```text
01-ec2-tag.png
02-start-lambda-success.png
03-stop-lambda-success.png
04-eventbridge-schedule.png
05-cloudwatch-logs.png
06-iam-policy.png
```

The screenshots supplied during project development were reviewed and sanitized locally. The GitHub connector used for this build can write text/code files but cannot attach arbitrary local binary images directly to the repository. Therefore, the sanitized evidence files are kept separately until they are uploaded through GitHub's normal web interface.
