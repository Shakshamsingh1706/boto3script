import boto3
lambda_client = boto3.client('lambda')
response = lambda_client.create_function(
    FunctionName='my-function',
    Runtime='python3.8',
    Role='arn:aws:iam::123456789012:role/lambda-role',
    Handler='lambda_function.handler',
    Code={'ZipFile': open('lambda_function.zip', 'rb').read()}
)
print(response['FunctionArn'])
