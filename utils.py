import os
import sys
import boto3
sys.path.insert(0, "/home/jovyan/.local/lib/python3.9/site-packages")

os.environ['AWS_ACCESS_KEY_ID'] = ""
os.environ['AWS_SECRET_ACCESS_KEY'] = ""
os.environ['AWS_SESSION_TOKEN'] = ""


def upload_folder_to_s3(local_folder_path, s3_bucket_name, s3_folder_path):
    s3 = boto3.client('s3')

    for root, dirs, files in os.walk(local_folder_path):
        for file in files:
            local_file_path = os.path.join(root, file)
            s3_file_path = os.path.join(s3_folder_path, os.path.relpath(
                local_file_path, local_folder_path))

            # Upload the file to S3
            s3.upload_file(local_file_path, s3_bucket_name, s3_file_path)

            print(
                f'Uploaded {local_file_path} to {s3_bucket_name}/{s3_file_path}')
