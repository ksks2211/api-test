import boto3
from .config import get_api_key
import os
from botocore.exceptions import ClientError

AWS_ACCESS_KEY=get_api_key('AWS_ACCESS_KEY')
AWS_SECRET_KEY=get_api_key('AWS_SECRET_KEY')
AWS_BUCKET_NAME=get_api_key('AWS_BUCKET_NAME')

s3_client = boto3.client('s3',aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)

def upload(filename:str,key:str, bucket=AWS_BUCKET_NAME):
    s3_client.upload_file(filename, bucket, key)

def download(filename:str,key:str, bucket=AWS_BUCKET_NAME):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    s3_client.download_file(bucket, key, filename)

def delete(key:str, bucket=AWS_BUCKET_NAME):
    s3_client.delete_object(Bucket=bucket, Key=key)

def exists(key:str, bucket=AWS_BUCKET_NAME):    
    try:
        s3_client.head_object(Bucket=bucket, Key=key)
        return True
    except ClientError as e :
        if e.response['Error']['Code'] == '404':
            print(f"The object '{key}' does not exist in '{bucket}'.")
            return False
        else:             
            print('Error or Not Forbidden')
            return False