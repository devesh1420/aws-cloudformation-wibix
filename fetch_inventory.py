import boto3
import argparse

def get_stack_resources(stack_name):
    cf = boto3.client('cloudformation')
    try:
        resources = cf.describe_stack_resources(StackName=stack_name)
        return resources['StackResources']
    except Exception as e:
        print(f"Error fetching stack resources: {e}")
        return []

def list_ec2_instances():
    ec2 = boto3.client('ec2')
    instances = ec2.describe_instances()
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            print(f"EC2 Instance ID: {instance['InstanceId']} | State: {instance['State']['Name']}")

def list_s3_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        print(f"S3 Bucket: {bucket['Name']}")

def main():
    parser = argparse.ArgumentParser(description="Fetch AWS Inventory via CloudFormation Stack")
    parser.add_argument('--stack-name', required=True, help='CloudFormation Stack Name')

    args = parser.parse_args()
    print(f"Fetching resources from stack: {args.stack_name}")

    resources = get_stack_resources(args.stack_name)
    for res in resources:
        print(f"Resource: {res['ResourceType']} | Logical ID: {res['LogicalResourceId']}")

    print("\nFetching EC2 instances:")
    list_ec2_instances()

    print("\nFetching S3 buckets:")
    list_s3_buckets()

if __name__ == '__main__':
    main()
