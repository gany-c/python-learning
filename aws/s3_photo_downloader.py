import boto3
import os

def download_files_from_s3(bucket_arn, local_directory):
    # Extract the bucket name from the ARN
    bucket_name = bucket_arn.split(':::')[-1]

    # Create a new S3 client
    s3 = boto3.client('s3')

    # List all objects in the bucket
    objects = s3.list_objects_v2(Bucket=bucket_name)

    # Check if there are any objects in the bucket
    if 'Contents' in objects:
        # Iterate through each object in the bucket
        for obj in objects['Contents']:
            key = obj['Key']
            # Check if the object is a .jpg file
            if key.endswith('.jpg'):
                # Generate local file path for the downloaded file
                local_file_path = os.path.join(local_directory, key)
                # Download the file from S3
                s3.download_file(bucket_name, key, local_file_path)
                print(f'Downloaded {key} to {local_file_path}')

# Specify your S3 bucket ARN
bucket_arn = 'arn:aws:s3:::gany-photos'

# Specify the local directory where you want to save the downloaded files
local_directory = '/Users/ganapathychidambaram/s3-photos/'

# Call the function to download .jpg files from the S3 bucket
download_files_from_s3(bucket_arn, local_directory)
