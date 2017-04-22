import boto3
import argparse

ec2 = boto3.resource('ec2')
name = None

def lambda_handler(event, context):
    new_instance = ec2.create_instances(ImageId='ami-16d4eb01', MinCount=1,
                                        MaxCount=1, InstanceType='t2.nano')
   
    # There really has to be a better way to get the instance id.
    # I'm just too lazy to find it right now.
    instance_id = new_instance[0].__dict__['meta'].__dict__['data']['InstanceId']

    # Really shouldn't make this global, but not sure how this will work
    # when calling from Lambda
    if name:
        ec2.create_tags(Resources=[instance_id], Tags=[{'Key':'Name', 'Value':name}])

    return {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": "I've created a new instance named {} on your AWS account.".format(name)
        },
        "shouldEndSession": False
    }
}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', required=False)
    args = parser.parse_args()

    if args.name:
        name = args.name
    lambda_handler({}, {})
