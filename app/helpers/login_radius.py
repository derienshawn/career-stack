from fastapi import Request
from fastapi.responses import RedirectResponse, JSONResponse
from LoginRadius import LoginRadius as LR
import redis
import os

# Redis config to run Locally
# redis = redis.Redis(host= 'localhost',port= '6379')

#Redis config to run staging on Heroku
redis_url = os.environ.get('REDIS_URL', 'redis://localhost:6379')
redis = redis.from_url(redis_url)

LR.API_KEY = "5a253b16-8b8e-49da-8bd6-5fcf6ad5a968"
LR.API_SECRET = "5a253b16-8b8e-49da-8bd6-5fcf6ad5a968"

loginradius = LR()


register_local_url = "https://career-stack.hub.loginradius.com/auth.aspx?action=register&return_url=http://127.0.0.1:8000/register-redirect"
register_staging_url = "https://career-stack.hub.loginradius.com/auth.aspx?action=register&return_url=https://career-stack.herokuapp.com/register-redirect"


def register():
    # URL for local testing -- uncomment when running locally
    # return RedirectResponse(register_local_url)

    # URL for staging testing -- uncomment when running on Heroku staging
    return RedirectResponse(register_staging_url)


def login_radius_redirect(request: Request):
    params = dict(request.query_params)
    token_from_params = params['token']
    redis.set('token', token_from_params)
    res = loginradius.authentication.get_profile_by_access_token(token_from_params)

    if token_from_params is None:
        # redirect the user to our LoginRadius login URL if no access token is provided
        return RedirectResponse(register_staging_url)
        # return RedirectResponse(register_local_url)

    return JSONResponse(content=res)

def logout():
    token_as_bytes = redis.get('token')
    token_as_str = str(token_as_bytes, 'UTF-8')

    if token_as_str is None:
        return "No token found"

    # invalidate the access token with LoginRadius API
    loginradius.authentication.auth_in_validate_access_token(token_as_str)
    return RedirectResponse(register_staging_url)

def get_user(id: str):
    res = loginradius.authentication.get_profile_by_access_token(id)
    return JSONResponse(content=res)
