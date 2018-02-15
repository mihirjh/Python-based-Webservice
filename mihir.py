import json
import datetime

def handler(event, context):
    data = {
    'output': 'Hello Mihir' + event["pathParameters"]["name"]
    'timestamp': datetime.datetime.utcnow().isoformat()
    'Life': 'Welcome to the new world Neo'
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}
    }
