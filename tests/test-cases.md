# Test Checklist

- [ ] Tagged stopped EC2 instance is started by the start Lambda.
- [ ] Tagged running EC2 instance is stopped by the stop Lambda.
- [ ] Untagged instances are ignored.
- [ ] Instances in an already-correct state are not targeted.
- [ ] Multiple tagged instances are processed.
- [ ] Missing `ec2:DescribeInstances` permission produces an authorization error.
- [ ] Missing start/stop permission produces an authorization error.
- [ ] CloudWatch receives Lambda logs.
- [ ] EventBridge Scheduler invokes the correct Lambda.
- [ ] Scheduler uses `Asia/Kolkata` for the lab schedule.
- [ ] Temporary test schedules are removed after testing.
