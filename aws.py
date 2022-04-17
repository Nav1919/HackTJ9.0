import logging
import boto3
from botocore.exceptions import ClientError
import os
import time
import json


session = boto3.Session(
    aws_access_key_id="AKIA5J5BP7DRQ22KTEEV",
    aws_secret_access_key="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",
)
s3 = session.resource("s3")

#for bucket in s3.buckets.all():
 #   print(bucket.name)
#print(os.listdir("./"))
#print("hello")

def upload_file(file_name, bucket, object_name):
    
    session = boto3.Session(
        aws_access_key_id="AKIA5J5BP7DRQ22KTEEV",
        aws_secret_access_key="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",
    )
    s3 = session.resource("s3")
    if object_name is None:
        object_name = os.path.basename(file_name)

#    print("runsuploadfile")
    s3_client = boto3.client(service_name='s3', region_name='us-east-2',
    aws_access_key_id='AKIA5J5BP7DRQ22KTEEV',
    aws_secret_access_key='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')    
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
      #  print("s")
        return False
    return True

def get_transcript(file_name, bucket, object_name):
   # print("runstranscript")
    
    session = boto3.Session(
        aws_access_key_id="AKIA5J5BP7DRQ22KTEEV",
        aws_secret_access_key="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",
    )
    s3 = session.resource("s3")

    s3_client = boto3.client(service_name='s3', region_name='us-east-2',
    aws_access_key_id='AKIA5J5BP7DRQ22KTEEV',
    aws_secret_access_key='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')   
    flag = True
    #while (flag):
        #time.sleep(300)
    try:
        (s3.Bucket('transcriptednews').download_file(file_name, object_name))
    except:
        time.sleep(5)
       # print("catch")

        get_transcript(file_name, bucket, object_name)
    # Opening JSON file
        #print("getsjson")

    f = open(file_name)
    
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    print(data['results']['transcripts'][0]['transcript'])
    return data['results']['transcripts'][0]['transcript']



    #for key in s3_client.list_objects(Bucket='transcriptednews')['Contents']:
     #   print(key['Key'])
#(s3.Bucket('transcriptednews').download_file("PXL_20220416_230256384.TS.mp4-4b5dfa93-20dc-4bf3-8e44-7de1d8ef2861.json", "PXL_20220416_230256384.TS.mp4-4b5dfa93-20dc-4bf3-8e44-7de1d8ef2861.json"))
upload_file("news.mp4", "classifynewsvideo", "news.mp4")
get_transcript("news.json", "transcriptednews", "news.json")

