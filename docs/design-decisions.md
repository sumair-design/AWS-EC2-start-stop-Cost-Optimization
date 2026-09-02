# Design Decisions

## 1. Why Lambda?

The workload is event-driven and short-lived. Lambda removes the need to keep a management server running solely to execute scheduled EC2 API calls.

## 2. Why EventBridge Scheduler?

Scheduling belongs outside the application code. EventBridge Scheduler can invoke the correct Lambda at the required time and supports explicit time-zone configuration.

## 3. Why tag-based discovery?

Hard-coding instance IDs creates maintenance overhead and makes the automation brittle. A tag defines the desired management scope instead:

```text
cost optimization = auto start/stop
```

Adding another eligible instance therefore requires a tag change, not a source-code change.

## 4. Why two Lambda functions?

Separate start and stop handlers make the EventBridge targets explicit and reduce conditional logic. Each schedule has one clear responsibility.

A single handler with an `action` event is also possible, but the two-function model is easier to understand for this portfolio implementation.

## 5. Why IAM resource conditions?

The policy allows only the EC2 APIs required by the application. Start/stop operations are further constrained by the expected resource tag, reducing the chance of accidentally changing unrelated instances.

## 6. Why CloudWatch Logs?

Scheduled automation must be diagnosable without an interactive session. Lambda's execution logs provide a simple audit trail for discovery and action results.

## 7. Why environment variables?

Tag configuration is operational configuration, not application logic. Environment variables allow the same Lambda package to be reused with different tagging conventions without editing code.

## 8. Production considerations

The lab intentionally stays small. A production version should evaluate retry/backoff behavior, protected-instance exclusions, alerting, multi-account deployment, centralized logging, change management, and infrastructure-as-code.
