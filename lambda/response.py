import json
import boto3
import time

# do not forget to increase timeout to 2 mins

def lambda_handler(event, context):
    
    payload = json.loads(event['Records'][0]['Sns']['Message'])
    
    print(f"Processed message {payload}")
    
    connectionId = payload['connectionId']
    request = payload['message']
    domainName = payload['domainName']
    stage = payload['stage']

    time.sleep(20)
    response = "send back message here"

    apigatewaymanagementapi = boto3.client(
        'apigatewaymanagementapi', 
        endpoint_url = "https://" + domainName + "/" + stage
    )

    apigatewaymanagementapi.post_to_connection(
        Data=response,
        ConnectionId=connectionId
    )

    return {}