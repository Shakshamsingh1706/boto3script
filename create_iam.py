import boto3
iam_client = boto3.client('iam')
response = iam_client.create_user(UserName='my-user')
print(response['User']['Arn'])
