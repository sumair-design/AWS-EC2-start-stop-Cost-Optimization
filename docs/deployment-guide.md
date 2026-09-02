# Deployment Guide

## Prerequisites

- AWS account with permission to create IAM roles, Lambda functions, EventBridge Scheduler schedules, and EC2 resources for the lab.
- An EC2 instance in the same AWS Region as the Lambda functions.
- The EC2 instance tagged with:

```text
Key:   cost optimization
Value: auto start/stop
```

The tag key and value can be changed through Lambda environment variables.

## 1. Create the Lambda execution role

Create an IAM role trusted by Lambda using `iam/lambda-trust-policy.json`.

Attach permissions equivalent to `iam/ec2-start-stop-policy.json`.

For a production implementation, consider restricting `ec2:StartInstances` and `ec2:StopInstances` to the intended instance ARNs and keep `ec2:DescribeInstances` separate because it does not support the same resource-level restriction.

## 2. Create the Start Lambda

Create a Python Lambda function named, for example:

```text
EC2-AutoStart
```

Runtime: Python 3.x.

Paste the contents of `lambda/start_ec2/lambda_function.py` and attach the execution role.

Optional environment variables:

```text
TAG_KEY=cost optimization
TAG_VALUE=auto start/stop
```

## 3. Create the Stop Lambda

Create another Python Lambda function, for example:

```text
EC2-AutoStop
```

Use `lambda/stop_ec2/lambda_function.py` and the same IAM execution-role pattern.

## 4. Create EventBridge Scheduler schedules

Create two recurring EventBridge Scheduler schedules.

### Start

```text
Schedule: 0 13 ? * SUN-THU *
Time zone: Asia/Kolkata
Target: EC2-AutoStart
```

### Stop

```text
Schedule: 0 14 ? * SUN-THU *
Time zone: Asia/Kolkata
Target: EC2-AutoStop
```

Allow Scheduler to invoke the target Lambda using its execution role.

## 5. Validate

1. Confirm the EC2 tag exactly matches the Lambda environment variables.
2. Invoke each Lambda manually with `{}` before relying on the schedule.
3. Check the EC2 state after execution.
4. Review `/aws/lambda/<function-name>` in CloudWatch Logs.
5. Confirm both Scheduler schedules are enabled.

## Important

The example schedule is intentionally short for the lab. A real business-hours schedule would normally keep instances running for a longer useful work window. Do not assume the one-hour lab schedule represents a realistic production workload.
