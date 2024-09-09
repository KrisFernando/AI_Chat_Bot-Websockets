import json
import boto3
import os



# dont forget to add SNS_ARN to Environment Variables

def lambda_handler(event, context):
    connectionId = event["requestContext"]["connectionId"]
    request = json.loads(event["body"])["message"]
    domainName = event["requestContext"]["domainName"]
    stage = event["requestContext"]["stage"]
    response = request + "response"
    
    apigatewaymanagementapi = boto3.client(
        'apigatewaymanagementapi', 
        endpoint_url = "https://" + domainName + "/" + stage
    )

    apigatewaymanagementapi.post_to_connection(
        Data=response,
        ConnectionId=connectionId
    )

    return {}