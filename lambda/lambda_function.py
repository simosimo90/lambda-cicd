import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Ciao a tutti dal mio CICD githubactions workflow!')
    }