import json
import uuid
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UrlShortener')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    long_url = body['url']
    shortcode = str(uuid.uuid4())[:6]
    
    table.put_item(Item={
        'shortcode': shortcode,
        'url': long_url
    })
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'shortcode': shortcode,
            'short_url': f"https://your-api-url/{shortcode}"
        })
    }
