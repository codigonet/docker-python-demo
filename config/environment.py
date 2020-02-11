import os

class Config(object):
  DEBUG = False
  TESTING = False
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID','AWSACCESSKEYID12345')
  AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY','AWSSECRETKEY12345')
  AWS_REGION = os.environ.get('AWS_REGION','us-east-1')

class DevelopmentConfig(Config):
  DEBUG = os.environ.get('DEBUG_APP',False)