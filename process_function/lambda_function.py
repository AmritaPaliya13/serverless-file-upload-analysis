import json

def lambda_handler(event, context):
    # Sample logic
    return {
        'statusCode': 200,
        'body': json.dumps('Process function executed successfully!')
    }
