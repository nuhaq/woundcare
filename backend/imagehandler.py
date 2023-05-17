# Function desc:
    # takes image as binary file (stored in 'body') and uploads to s3 bucket

import json
import base64

import boto3
client = boto3.client('s3')

#stomaimages
#https://zeqdncr77a.execute-api.us-west-2.amazonaws.com/test/upload-image
def lambda_handler(event, context):
    ms = base64.b64decode(event['body'])
    response = client.put_object(
        Body = ms,
        Bucket = 'stomaimages',
        Key = 'test.JPG'
    )
    return {
        'statusCode': 200,
        'body': response
    }