import json
import boto3


def lambda_handler(event, context):
    
    S3_BUCKET_NAME = ''
    KEY = 'fee_summary_report.json'
    s3_client = boto3.client('s3')
    response = s3_client.get_object(Bucket='feesummarybucketmmmm', Key=KEY)
    data = response['Body'].read()
    print(response)
    print(data)
    fee_summary_report = json.loads(data)
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': fee_summary_report
    }
