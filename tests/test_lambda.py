from unittest.mock import MagicMock, patch

import pytest


@pytest.fixture
def start_module():
    with patch("boto3.client") as client:
        mock_ec2 = MagicMock()
        client.return_value = mock_ec2
        import importlib
        module = importlib.import_module("lambda.start_ec2.lambda_function")
        module.ec2 = mock_ec2
        yield module, mock_ec2


def test_start_lambda_starts_matching_instances(start_module):
    module, ec2 = start_module
    ec2.get_paginator.return_value.paginate.return_value = [
        {"Reservations": [{"Instances": [{"InstanceId": "i-example123"}]}]}
    ]
    ec2.start_instances.return_value = {
        "StartingInstances": [{"InstanceId": "i-example123"}]
    }

    result = module.lambda_handler({}, None)

    ec2.start_instances.assert_called_once_with(InstanceIds=["i-example123"])
    assert result["statusCode"] == 200
    assert result["started_instances"] == ["i-example123"]


def test_start_lambda_does_nothing_when_no_matches(start_module):
    module, ec2 = start_module
    ec2.get_paginator.return_value.paginate.return_value = [{"Reservations": []}]

    result = module.lambda_handler({}, None)

    ec2.start_instances.assert_not_called()
    assert result["started_instances"] == []
