# Project Walkthrough

Use this sequence when demonstrating the project in an interview or portfolio review.

## 1. Show the target

Open EC2 and show an instance carrying the automation tag:

```text
cost optimization = auto start/stop
```

Explain that the tag defines which resources are eligible for automation.

## 2. Show IAM

Open the Lambda execution role and explain:

- Lambda is the trusted service principal.
- `DescribeInstances` is required for discovery.
- Start/stop actions are restricted to the intended tag condition.
- CloudWatch Logs permissions provide operational visibility.

## 3. Show the Lambda functions

Explain that the start function searches for matching stopped instances and the stop function searches for matching running instances.

Point out that the instance ID is discovered at runtime rather than hard-coded.

## 4. Show EventBridge Scheduler

Show the start and stop schedules and their configured time zone. Explain that scheduling is separated from the Lambda business logic.

## 5. Demonstrate a manual execution

Invoke the Lambda manually with an empty event. The functions do not require an event payload for normal scheduled execution.

Expected behavior:

- matching instances are discovered;
- the correct EC2 API is called;
- the result is returned;
- CloudWatch receives the execution logs.

## 6. Show CloudWatch

Open the corresponding Lambda log group and show the discovery/action messages. This demonstrates that the automation is observable and failures are not silently ignored.

## 7. Explain the cost model

The project is not about claiming a made-up percentage saving. The saving depends on instance type, region, pricing model, number of instances, and hours avoided. Explain the formula and use real AWS pricing for any quantified estimate.

## 8. Discuss production improvements

A strong production discussion includes:

- retry and backoff for transient AWS errors;
- explicit protected/excluded tags;
- alerting for failed scheduled invocations;
- infrastructure-as-code;
- multi-account deployment strategy;
- centralized logging and audit controls;
- schedule exceptions for holidays or maintenance windows.
