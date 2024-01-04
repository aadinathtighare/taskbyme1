import json

import boto3
 
s3 = boto3.client('s3')
 
def lambda_handler(event, context):

    bucket = 'virginia.bucket-destination'
 
    transactionToUpload = {}

    transactionToUpload['transcationId'] = '1'

    transactionToUpload['type'] = 'PURCHASE'

    transactionToUpload['amount'] = '80000'

    transactionToUpload['customerId'] = 'kotiCUST-1000'
 
    fileName = 'ADINATHCUST-1' + '.json'
 
    uploadByteStream = bytes(json.dumps(transactionToUpload).encode('UTF-8'))

    s3.put_object(Bucket=bucket, Key=fileName, Body=uploadByteStream)

    print('Put Complete')
