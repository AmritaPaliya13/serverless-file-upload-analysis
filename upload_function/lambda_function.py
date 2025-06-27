import json
import base64
import boto3

s3 = boto3.client('s3')
bucket_name = 'file-analyzer-amrita'  # ← Replace with your actual bucket name

def lambda_handler(event, context):
    try:
        # Parse body
        body = json.loads(event['body'])  # This will raise KeyError if 'body' missing

        filename = body['filename']
        filedata = body['filedata']

        # Base64 fix: padding
        missing_padding = len(filedata) % 4
        if missing_padding:
            filedata += '=' * (4 - missing_padding)

        decoded_file = base64.b64decode(filedata)

        # Upload to S3
        s3.put_object(Bucket=bucket_name, Key=filename, Body=decoded_file)

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'File uploaded successfully'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
