# aws-cloudformation-wibix
This proof-of-concept demonstrates how to create a read-only IAM role using AWS CloudFormation, and how to use a Python script to fetch AWS resource inventory securely without using access/secret keys.

## 📂 Files
- `read-only-role.yaml` – CloudFormation template to create a read-only IAM role.
- `fetch_inventory.py` – Python script to fetch EC2 and S3 resource details using boto3 and the CloudFormation stack name.
- `README.md` – Project documentation and usage instructions.

- ## 🚀 Instructions

### 1. Upload CloudFormation Template to S3

Upload `read-only-role.yaml` to a public S3 bucket.
https://wibix-poc.s3.amazonaws.com/read-only-role.yaml

### 2. Launch CloudFormation Stack

Use the following format to launch the stack:
https://console.aws.amazon.com/cloudformation/home?region=us-east-1/stacks/create/review?templateURL=https://wibix-poc.s3.amazonaws.com/read-only-role.yaml&stackName=ReadOnlyInventoryStack

### 3. Run Python Script

Make sure you're running this from an environment (like EC2) with sufficient IAM permissions.

#### Step-by-step:

1. Install required library:

```bash
pip install boto3

2. Run the script:
python3 fetch_inventory.py --stack-name ReadOnlyInventoryStack

What This Script Does?
-- Connects to AWS using default IAM credentials (no hardcoded secrets).
--Lists: EC2 instance IDs and their states and S3 bucket names
--Prints details of resources created by the CloudFormation stack

Requirements:
 Python 3.x
 boto3
 IAM role attached to environment with read-only permissions (no credentials file needed)

