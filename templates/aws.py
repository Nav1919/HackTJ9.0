import logging
import boto3
from botocore.exceptions import ClientError
import os
import time
import json

s3 = boto3.resource("s3")


for bucket in s3.buckets.all():
    print(bucket.name)
    

def upload_file(file_name, bucket, object_name):
    
    if object_name is None:
        object_name = os.path.basename(file_name)

    
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def get_transcript(file_name, bucket, object_name):

    s3_client = boto3.client('s3')
    flag = True
    #while (flag):
        #time.sleep(300)
    try:
        (s3.Bucket('transcriptednews').download_file(file_name, object_name))
    except:
        time.sleep(5)
        get_transcript(file_name, bucket, object_name)
    # Opening JSON file
    f = open(file_name)
    
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    print(data['results']['transcripts'][0]['transcript'])



    #for key in s3_client.list_objects(Bucket='transcriptednews')['Contents']:
     #   print(key['Key'])
#(s3.Bucket('transcriptednews').download_file("PXL_20220416_230256384.TS.mp4-4b5dfa93-20dc-4bf3-8e44-7de1d8ef2861.json", "PXL_20220416_230256384.TS.mp4-4b5dfa93-20dc-4bf3-8e44-7de1d8ef2861.json"))
upload_file("smalllermp4.mp4", "classifynewsvideo", "smalllermp4.mp4")
get_transcript("smalllermp4.json", "transcriptednews", "smalllermp4.json")
