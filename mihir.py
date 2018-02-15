import json
import datetime

def handler(event, context):
    data = {
    'output': 'Hello Mihir' + event["pathParameters"]["name"]
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}
    }
