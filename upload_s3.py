import boto3
s3_client = boto3.client('s3')
s3_client.upload_file('local_file.txt', 'bucket_name', 'remote_file.txt')
