import boto3
import argparse

ec2 = boto3.resource('ec2')
ec2_client = boto3.client('ec2')

def lambda_handler(event, context):
    existing_instance = ec2.Instance(id='i-0e6a7023f20d1bc63')
    res = existing_instance.start()
   
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


def get_instances():
    response = ec2_client.describe_instances()
    import pdb; pdb.set_trace()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', default=None)
    args = parser.parse_args()
    get_instances()
    


if __name__ == '__main__':
    main()
