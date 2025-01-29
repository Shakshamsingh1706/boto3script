import boto3
s3_client = boto3.client('s3')
s3_client.put_bucket_versioning(
    Bucket='my-bucket-name',
    VersioningConfiguration={'Status': 'Enabled'}
)
