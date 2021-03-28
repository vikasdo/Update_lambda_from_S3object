import boto3
import sys,io,os
from zipfile import ZipFile
def main():
    # if (len(sys.argv)>6):
    #     print ('Error: Required 5 arguments.')
    #     # Checks for 6 because the script path is in position 0. So len is 6
    #     # for 5 arguments.
    #     sys.exit(1)
    print(sys.argv)
    bucket_name=sys.argv[1]
    aws_key=sys.argv[2]
    aws_access_key=sys.argv[3]
    aws_access_secret=sys.argv[4]
    local_path=sys.argv[5]

    session = boto3.Session(
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_access_secret,
        region_name='us-east-2'
    )
    client = session.client('s3')

    response = client.upload_file(
        Filename=local_path,
        Bucket=bucket_name,
        Key=aws_key
    )
    print ('Done uploading')
    client = session.client('lambda')
  
    def files_to_zip(path):
        for root, dirs, files in os.walk(path):
            for f in files:
                full_path = os.path.join(root, f)
                archive_name = full_path[len(path) + len(os.sep):]
                yield full_path, archive_name
    def make_zip_file_bytes(path):
        print(os.path.exists(path))
        buf = io.BytesIO()
        with ZipFile(buf, 'w') as z:
            for full_path, archive_name in files_to_zip(path=path):
                z.write(full_path, archive_name)
        return buf.getvalue()
    response = client.update_function_code(
    FunctionName='increment-operation',
    S3Bucket=bucket_name,
    S3Key=aws_key,  
    )
    response = client.update_function_code(
    FunctionName='decrement-operation',
    S3Bucket=bucket_name,
    S3Key=aws_key,  
    )
     response = client.update_function_code(
    FunctionName='square-operation',
    S3Bucket=bucket_name,
    S3Key=aws_key,  
    )
    print ('Done updated lambda d')


main()