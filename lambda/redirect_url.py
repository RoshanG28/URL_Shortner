import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UrlShortener')

def lambda_handler(event, context):
    shortcode = event['pathParameters']['shortcode']
    
    resp = table.get_item(Key={'shortcode': shortcode})
    
    if 'Item' not in resp:
        return {'statusCode': 404, 'body': 'Not Found'}
    
    return {
        'statusCode': 301,
        'headers': {
            'Location': resp['Item']['url']
        }
    }
