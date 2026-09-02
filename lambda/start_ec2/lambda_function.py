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
    """Start tagged stopped EC2 instances."""
    logger.info("Starting EC2 automation. tag=%s value=%s", TAG_KEY, TAG_VALUE)

    try:
        instance_ids = get_instance_ids("stopped")
        logger.info("Found %d stopped matching instance(s): %s", len(instance_ids), instance_ids)

        if not instance_ids:
            return {
                "statusCode": 200,
                "action": "start",
                "started_instances": [],
                "message": "No matching stopped instances found.",
            }

        response = ec2.start_instances(InstanceIds=instance_ids)
        started = [item["InstanceId"] for item in response.get("StartingInstances", [])]
        logger.info("Start request submitted for: %s", started)

        return {
            "statusCode": 200,
            "action": "start",
            "started_instances": started,
        }

    except (ClientError, BotoCoreError) as exc:
        logger.exception("AWS API error while starting EC2 instances")
        raise exc
    except Exception as exc:
        logger.exception("Unexpected error while starting EC2 instances")
        raise exc
