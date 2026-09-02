# Testing

## Functional tests

| Test | Setup | Expected result |
|---|---|---|
| Start tagged stopped instance | Tagged instance is stopped | Start Lambda submits a start request |
| Stop tagged running instance | Tagged instance is running | Stop Lambda submits a stop request |
| No matching instances | Remove/alter the tag | Lambda returns success with an empty list |
| Multiple matching instances | Tag two or more instances | All matching instances in the expected state are processed |
| Already correct state | Start Lambda with no stopped matches, or Stop Lambda with no running matches | No unnecessary API action |

## Permission tests

Temporarily remove one required EC2 permission from the Lambda role and invoke the function. The function should fail and CloudWatch should contain an AWS authorization error. Restore the permission after the test.

A common example is removing `ec2:DescribeInstances`; the Lambda then cannot discover the tagged instances.

## Scheduler test

Do not wait for the daily schedule during development. Create a temporary schedule a few minutes ahead, invoke the correct Lambda, and verify:

1. Scheduler execution occurs.
2. Lambda invocation succeeds.
3. CloudWatch contains the execution log.
4. EC2 transitions to the expected state.

Delete the temporary schedule after validation.

## Evidence to capture

For a portfolio project, useful evidence includes:

- EC2 instance with the automation tag.
- Successful Lambda execution result.
- CloudWatch log entry.
- EventBridge Scheduler configuration showing the time zone and schedule.
- Final architecture diagram.
