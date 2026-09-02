# Troubleshooting

## `UnauthorizedOperation` for `DescribeInstances`

The Lambda execution role is missing `ec2:DescribeInstances`. Add it to the role policy and invoke the function again.

## `UnauthorizedOperation` for StartInstances or StopInstances

The execution role is missing the corresponding EC2 action. Check the attached policy and verify that the Lambda is using the intended execution role.

## Lambda succeeds but no instances change

Check:

- AWS Region of Lambda and EC2.
- Tag key and value, including capitalization and spaces.
- Current EC2 state.
- Lambda environment variables `TAG_KEY` and `TAG_VALUE`.

The start function only targets instances in the `stopped` state. The stop function only targets instances in the `running` state.

## Scheduler does not invoke Lambda

Check that:

- The schedule is enabled.
- The cron expression is correct.
- `Asia/Kolkata` is selected when using the lab schedule.
- The Scheduler execution role can invoke the Lambda target.
- The schedule target points to the correct function and Region.

## Where to look for logs

Open CloudWatch Logs and select:

```text
/aws/lambda/<function-name>
```

The functions log the selected tag, number of matching instances, instance IDs, and AWS API errors.
