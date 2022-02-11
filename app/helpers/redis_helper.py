import redis
import os
from fastapi import Request


# Redis config to run Locally
# redis = redis.Redis(host= 'localhost',port= '6379')

#Redis config to run staging on Heroku
redis_url = os.environ.get('REDIS_URL', 'redis://localhost:6379')
redis = redis.from_url(redis_url)


def get_token():
    try:
        token = redis.get('token')
        token_as_str = str(token, 'UTF-8')
    except:
        print(">>>>>>>>> COULD NOT RETREIVE TOKEN <<<<<<<<<<<<")
    return token_as_str


def set_token(request: Request):
    try:
        params = dict(request.query_params)
        token_from_params = params['token']
        token = redis.set('token', token_from_params)
    except:
        print(">>>>>>>>> TOKEN NOT SET <<<<<<<<<<<<<")
    return token_from_params
