import boto3

ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    new_instance = ec2.create_instances(ImageId='ami-16d4eb01', MinCount=1,
                                        MaxCount=1, InstanceType='t2.nano')
   
    return {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": "I've created a new instance on your AWS account."
        },
        "shouldEndSession": False
    }
}
