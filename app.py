import os
import logging
import json

from flask import (Flask, request, session)
from flask_lambda import FlaskLambda
from flask_cors import CORS

from config.environment import DevelopmentConfig

app = FlaskLambda(__name__)
app.config.from_object(DevelopmentConfig)
CORS(app)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

logger.info('## ENVIRONMENT VARIABLES')
logger.info(os.environ)

@app.route('/')
def index(): #pylint: disable=unused-variable
  logger.info('## GET /')
  logger.info(request)

  data = {
    "status": "Demo Flask APP"
  }

  return (
    json.dumps(data, indent=2, sort_keys=True),
    200,
    {'Content-Type': 'application/json'}
  )

if __name__ == "__main__":
  app.debug = os.environ['DEBUG_APP'] or False
  app.run()