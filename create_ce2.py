import boto3
ec2_client = boto3.client('ec2')
response = ec2_client.run_instances(
    ImageId='ami-0abcdef1234567890',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1
)
print(response['Instances'][0]['InstanceId'])
