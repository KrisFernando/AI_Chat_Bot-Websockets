import json
import boto3
import os

client = boto3.client('sns')

# dont forget to add SNS_ARN to Environment Variables

def lambda_handler(event, context):
    snsTopicARN = os.environ['SNS_ARN'] 
    connectionId = event["requestContext"]["connectionId"]
    request = json.loads(event["body"])["message"]
    domainName = event["requestContext"]["domainName"]
    stage = event["requestContext"]["stage"]
    msg_json = {
        "message": request,
        "connectionId": connectionId,
        "domainName": domainName,
        "stage": stage
    }
    
    #response = client.publish(TopicArn=snsTopicARN,Message=request)
    response = client.publish(
        TargetArn=snsTopicARN,
        Message=json.dumps({'default': json.dumps(msg_json)}),
        MessageStructure='json'
    )

    return {}