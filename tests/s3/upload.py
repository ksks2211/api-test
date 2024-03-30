import boto3



s3_client = boto3.client('s3')

bucket='ksks2211-image-bucket'


def upload(filename:str,key:str, bucket=bucket):
    s3_client.upload_file(filename, bucket, key)

filename = 'profile.png'
key = "images/photo.png"



upload(filename, key)
    