import logging
import os
from typing import Any

import boto3
from botocore.exceptions import BotoCoreError, ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ec2 = boto3.client("ec2")
TAG_KEY = os.environ.get("TAG_KEY", "cost optimization")
TAG_VALUE = os.environ.get("TAG_VALUE", "auto start/stop")


def get_instance_ids(state: str) -> list[str]:
    """Return instance IDs matching the configured tag and EC2 state."""
    instance_ids: list[str] = []
    paginator = ec2.get_paginator("describe_instances")

    pages = paginator.paginate(
        Filters=[
            {"Name": f"tag:{TAG_KEY}", "Values": [TAG_VALUE]},
            {"Name": "instance-state-name", "Values": [state]},
        ]
    )

    for page in pages:
        for reservation in page.get("Reservations", []):
            for instance in reservation.get("Instances", []):
                instance_ids.append(instance["InstanceId"])

    return instance_ids


def lambda_handler(event: dict[str, Any], context: Any) -> dict[str, Any]:
    """Stop tagged running EC2 instances."""
    logger.info("Stopping EC2 automation. tag=%s value=%s", TAG_KEY, TAG_VALUE)

    try:
        instance_ids = get_instance_ids("running")
        logger.info("Found %d running matching instance(s): %s", len(instance_ids), instance_ids)

        if not instance_ids:
            return {
                "statusCode": 200,
                "action": "stop",
                "stopped_instances": [],
                "message": "No matching running instances found.",
            }

        response = ec2.stop_instances(InstanceIds=instance_ids)
        stopped = [item["InstanceId"] for item in response.get("StoppingInstances", [])]
        logger.info("Stop request submitted for: %s", stopped)

        return {
            "statusCode": 200,
            "action": "stop",
            "stopped_instances": stopped,
        }

    except (ClientError, BotoCoreError) as exc:
        logger.exception("AWS API error while stopping EC2 instances")
        raise exc
    except Exception as exc:
        logger.exception("Unexpected error while stopping EC2 instances")
        raise exc
