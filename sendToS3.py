import boto3

s3 = boto3.client('s3')

def uploadToS3(file_path, bucket, fileName):
    s3.upload_file(file_path, bucket, fileName)
    print(f"Successfully uploaded {fileName} to {bucket}.")