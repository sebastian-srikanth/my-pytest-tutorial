"""Sample class"""
import boto3
import botocore
import requests

class SampleClass:
    """
    This is a Test class
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def _f(cls):
        """
        Some function _f
        Returns:
            int: always 3
        """
        return 3

    @classmethod
    def aws_s3_list_buckets(cls):
        """
        Connect to AWS S3 bucket to list all buckets
        Returns:
            dict: list of s3 buckets
        """
        try:
            client = boto3.client("s3")
            print("My connection to AWS S3 is Success")
            print("Returning s3 buckets list")
            return client.list_buckets()
        except botocore.exceptions.ClientError as client_err:
            raise f"Exception has been raised due to = {client_err}"

    @classmethod
    def get_url(cls, url):
        """ fetch the url """
        source_code = requests.get(url).json()
        return source_code
