import boto3
s3_client = boto3.client('s3')
s3_client.delete_bucket(Bucket='my-bucket-name')
