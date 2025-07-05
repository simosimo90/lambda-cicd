import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Ciao dalla mia Lambda function triggherata con githubactions')
    }