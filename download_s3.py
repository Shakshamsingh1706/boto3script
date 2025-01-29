s3_client = boto3.client('s3')
s3_client.download_file('bucket_name', 'remote_file.txt', 'local_file.txt')
