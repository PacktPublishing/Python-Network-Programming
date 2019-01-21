import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_instances()
for item in response['Reservations']:
    for eachinstance in item['Instances']:
        print (eachinstance['InstanceId'],eachinstance['PrivateIpAddress'])
