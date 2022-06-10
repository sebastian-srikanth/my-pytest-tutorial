"""This is just a sample class
"""
from project.base_class import base_class
import boto3
import botocore
import requests
from project.base_class import base_class


class sample_class(base_class):
    """[summary]
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def f():
        """[summary]

        Returns:
            [type]: [description]
        """
        return 3

    def aws_s3_list_buckets():
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
        except botocore.exceptions.ClientError as e:
            raise e

    def get_url(url):
        """fetch the url in json format"""
        source_code = requests.get(url).json()
        return source_code
