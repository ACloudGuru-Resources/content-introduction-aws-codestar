import json
import datetime
import boto3
import os
import uuid

client = boto3.client('dynamodb')
table = os.getenv('DYNAMODB_TABLE')

def handler(event, context):
    unique_id = str(uuid.uuid1())
    if table is not None:
        response = client.put_item (
            TableName=table,
            Item={
                'Id': {
                    "S": unique_id
                }
            }
        )
    data = {
        'output': 'Hello World',
        'unique_id': unique_id,
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}