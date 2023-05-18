import json
import boto3

def extractVolumeID(volume_arn):
    arn_parts=volume_arn.split(':')
    volume_id=arn_parts[-1].split('/')[-1]
    return volume_id

def lambda_handler(event, context):
    print(event)
    volume_arn=event['resources'][0]
    volume_id=extractVolumeID(volume_arn)
    
    client = boto3.client('ec2')
    response = client.modify_volume(
        VolumeId=volume_id,
        VolumeType='gp3',
    )
