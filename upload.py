import boto3

s3 = boto3.resource('s3')
s3.Object('campaign-finance-tracker', 'Candidate-18.txt').put(Body=open('./Candidate18.txt', 'rb'))