import boto3
ec2_client = boto3.client('ec2')
ec2_client.stop_instances(InstanceIds=['i-0abcdef1234567890'])
