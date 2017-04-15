import boto3
import sys
import argparse


def get_instances():
    instances = {}

    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            names = [tag['Value'] for tag in instance['Tags']
                    if tag['Key'] == 'Name']
            d = {'instanceId': instance['InstanceId'],
                 'status': instance['Monitoring']['State']}
            instances.setdefault(names[0], []).append(d)
    return instances


def get_names():
    instances = get_instances()
    return list(instances.keys())


def get_status():
    instances = get_instances()
    result = {}
    for name in instances.keys():
        result[name] = instances[name][0]['status']
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--status', action='store_true')
    args = parser.parse_args()

    if args.status:
        result = get_status()
    else:
        result = get_instances(status=args.status)
    print(result)


if __name__ == '__main__':
    main()
