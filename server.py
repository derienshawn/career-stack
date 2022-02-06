from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, JSONResponse
from app.routes.user import user
from app.routes.project import project
from LoginRadius import LoginRadius as LR
import redis
import requests
import os

# Redis config to run Locally
# redis = redis.Redis(host= 'localhost',port= '6379')

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
redis = redis.from_url(redis_url)
print("**********************",redis_url)
LR.API_KEY = "5a253b16-8b8e-49da-8bd6-5fcf6ad5a968"
LR.API_SECRET = "5a253b16-8b8e-49da-8bd6-5fcf6ad5a968"

app = FastAPI()
loginradius = LR()
app.include_router(user, tags=["user"])
app.include_router(project, tags=["project"])
session = requests.Session()
staging_url = "https://career-stack.hub.loginradius.com/auth.aspx?action=register&return_url=https://career-stack.herokuapp.com/login"
local_url = "https://career-stack.hub.loginradius.com/auth.aspx?action=register&return_url=http://127.0.0.1:8000/login"

@app.get("/register")
def register():

    # URL for local testing -- uncomment when running locally
    # return RedirectResponse(local_url)

    # URL for staging testing -- uncomment when running on Heroku staging
    return RedirectResponse(staging_url)


@app.get("/login")
def login(request: Request):
    params = dict(request.query_params)
    token_from_params = params['token']
    redis.set('token', token_from_params)
    res = loginradius.authentication.get_profile_by_access_token(token_from_params)

    if token_from_params is None:
        # redirect the user to our LoginRadius login URL if no access token is provided
        return RedirectResponse(staging_url)

    return JSONResponse(content=res, headers={'token': token_from_params})

@app.get("/logout")
def logout():
    token_as_bytes = redis.get('token')
    token_as_str = str(token_as_bytes, 'UTF-8')

    if token_as_str is None:
        return "No token found"

    # invalidate the access token with LoginRadius API
    loginradius.authentication.auth_in_validate_access_token(token_as_str)
    session.headers.clear()
    return RedirectResponse(staging_url)

@app.get("/user-profile")
def get_user(id: str):
    res = loginradius.authentication.get_profile_by_access_token(id)
    return JSONResponse(content=res)
