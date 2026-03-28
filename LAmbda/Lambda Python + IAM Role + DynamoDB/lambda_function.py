import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Lab1-Events')

def lambda_handler(event, context):
    event_id = str(uuid.uuid4())

    table.put_item(
        Item={
            'event_id': event_id,
            'message': 'Hello from Lambda'
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps({
            'event_id': event_id,
            'status': 'inserted'
        })
    }
