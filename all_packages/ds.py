import os

from bson.objectid import ObjectId
import logging
from dotenv import load_dotenv
import numpy
from pymongo import MongoClient, UpdateOne
import sentry_sdk
from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration
import sklearn
import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from DS!')
    }
