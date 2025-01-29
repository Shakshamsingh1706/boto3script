import boto3
iam_client = boto3.client('iam')
iam_client.attach_user_policy(
    UserName='my-user',
    PolicyArn='arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess'
)
