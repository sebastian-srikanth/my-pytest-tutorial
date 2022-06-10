import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))
from project.sample_code import sample_class
from  unittest.mock import patch
import pytest
import botocore

# Test f method 
def test_f():
    result = sample_class.f()
    assert result == 3

# Test constructor
def test_sample_class_constructor():
    sample_class("Factspan", "11")

# Failed Test Case
@pytest.mark.xfail()
def test_fail_case():
    sample_class("Factspan")

# Failed Test Case for aws_s3_list_buckets method
@pytest.mark.xfail()
def test_fail_aws_s3_list_buckets():
    sample_class.aws_s3_list_buckets('test_argument')

# Mock response
@patch("boto3.Session.client")
def test_aws_s3_list_buckets(mock_s3_client):
    s3_client = mock_s3_client("s3")
    mock_result = {
        "Owner": {
            "DisplayName": "Factspan",
            "ID": "1234"
        },
        "Buckets": 
        [
            {
            "CreationDate": "2021-08-30 15:30:30",
            "Name": "FactspanBucket"
            }
        ]
    }
    s3_client.list_buckets.return_value  = mock_result
    result = sample_class.aws_s3_list_buckets()
    assert result == mock_result

# Test url
@patch("requests.get")
def test_get_url(mock_get_url):
    expected = {"result": "True"}
    mock_get_url.return_value.json.return_value = expected
    result = sample_class.get_url( 'dummy_url' )
    assert result == expected

# Test right exceptions
def test_exceptions_aws_s3_list_buckets():
    with pytest.raises(botocore.exceptions.ClientError):
        sample_class.aws_s3_list_buckets()
