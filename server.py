from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, JSONResponse
from app.routes.user import user
from app.routes.project import project
from LoginRadius import LoginRadius as LR
from app.helpers import login_radius
import redis
import requests
import os

# Redis config to run Locally
# redis = redis.Redis(host= 'localhost',port= '6379')

#Redis config to run staging on Heroku
redis_url = os.environ.get('REDIS_URL', 'redis://localhost:6379')
redis = redis.from_url(redis_url)

app = FastAPI()
app.include_router(user, tags=["user"])
app.include_router(project, tags=["project"])


@app.get("/register")
def register():
   return login_radius.register()


@app.get("/register-redirect")
def login(request: Request):
    return login_radius.login_radius_redirect(request)

@app.get("/logout")
def logout():
    return login_radius.logout()

@app.get("/user-profile")
def get_user(id: str):
    return login_radius.get_user(id)
