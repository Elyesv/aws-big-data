import boto3
from decimal import Decimal
from boto3.session import Session
from boto3.dynamodb.conditions import (
    Key, Attr
)
import requests
from io import BytesIO
from urllib.parse import urlparse
import os

PROFILE_NAME = "default"
BUCKET_NAME = 'kfc-buckets'

class S3Uploader:
    def __init__(self):
        self.bucket_name = BUCKET_NAME
        self._session = Session(profile_name=PROFILE_NAME)
        self.resource = self._session.resource('s3')
        self.bucket = self.resource.Bucket(BUCKET_NAME)

        if self.check_bucket_exists():
            print(f"Bucket {self.bucket_name} already exists")
        else:
            print(f"Bucket {self.bucket_name} does not exist")
            self.create_bucket()

    def check_bucket_exists(self):
        s3_client = self._session.client('s3')
        try:
            s3_client.head_bucket(Bucket=self.bucket_name)
            return True
        except s3_client.exceptions.NoSuchBucket:
            return False

    def create_bucket(self):
        s3_client = self._session.client('s3')
        s3_client.create_bucket(Bucket=self.bucket_name)

    def upload_image_from_url(self, image_url):
        parsed_url = urlparse(image_url)
        file_name = os.path.basename(parsed_url.path)

        response = requests.get(image_url)
        if response.status_code == 200:
            image_stream = BytesIO(response.content)
            image_stream.seek(0)

            self.bucket.upload_fileobj(image_stream, file_name, ExtraArgs={'ContentType': 'image/png'})
            print(f"Image uploaded successfully to {self.bucket_name}/{file_name}")
        else:
            print("Failed to download image from url")


def main():
    uploader = S3Uploader()
    uploader.upload_image_from_url(
        'https://images.unsplash.com/photo-1566024164372-0281f1133aa6?q=80&w=3464&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D')


if __name__ == '__main__':
    main()
