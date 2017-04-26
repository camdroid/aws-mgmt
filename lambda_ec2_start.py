import boto3
import argparse
from get_instances import get_instances
import pprint

ec2 = boto3.resource('ec2')
ec2_client = boto3.client('ec2')

pp = pprint.PrettyPrinter(indent=4)

name = None

def lambda_handler(event, context):
    instances = get_instances()
    if name:
        instance_id = instances[name][0]['instanceId']
    else:
        instance_id = 'i-0e6a7023f20d1bc63'
    existing_instance = ec2.Instance(id=instance_id)
    res = existing_instance.start()
    res = instances
   
    return {
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                # "text": "I've created a new instance on your AWS account. "
                "text": str(res.keys())+str(res.values())
        },
        "shouldEndSession": False
    }
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', default=None)
    args = parser.parse_args()

    global name
    name = args.name

    res = lambda_handler({}, {})
    pp.pprint(res)


if __name__ == '__main__':
    main()
