import boto3
 
aws_access_key_id = 'accesskey'
aws_secret_access_key = 'secretaccesskey'
region_name = 'us-east-2'
 
ec2 = boto3.client('ec2',aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key,region_name=region_name)
