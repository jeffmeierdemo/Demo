import boto3
boto3.setup_default_session(profile_name='336694646358_AdministratorAccess')  
session = boto3.Session()
S3 = boto3.client('s3')

# Function to list all objects in an S3 bucket and output their name and creation date
def list_s3_objects(bucket_name):
    paginator = S3.get_paginator('list_objects_v2')
    page_iterator = paginator.paginate(Bucket=bucket_name)
    
    for page in page_iterator:
        if 'Contents' in page:
            for obj in page['Contents']:
                print(f"Name: {obj['Key']}, Creation Date: {obj['LastModified']}, Storage class: {obj['StorageClass']}")
        else:
            print("The bucket is empty.")

bucket_name = 'athome'
list_s3_objects(bucket_name)