import boto3
import os

# Set the AWS credentials for MinIO
os.environ['AWS_ACCESS_KEY_ID'] = 'minioadmin'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'minioadmin'

# Initialize a boto3 client to interact with MinIO
s3_client = boto3.client('s3', endpoint_url="http://minio-service:9000")

# Specify the bucket and object key
bucket_name = 'models'
object_key = 'models/model-training-job-lmpx4.pkl'

# File to upload (replace with your local file path)
local_file_path = 'models/model-training-job-lmpx4.pkl'

try:
    # Upload the file to MinIO
    s3_client.upload_file(local_file_path, bucket_name, object_key)
    print(f"File uploaded to s3://{bucket_name}/{object_key}")
except Exception as e:
    print(f"Error uploading file: {e}")
