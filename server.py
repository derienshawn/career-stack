from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, JSONResponse, Response
from app.routes.user import user
from app.routes.project import project
from LoginRadius import LoginRadius as LR
import requests

LR.API_KEY = "5a253b16-8b8e-49da-8bd6-5fcf6ad5a968"
LR.API_SECRET = "5a253b16-8b8e-49da-8bd6-5fcf6ad5a968"

app = FastAPI()
loginradius = LR()
app.include_router(user)
app.include_router(project)
r = Response()



@app.get("/register")
def register():

    # URL for local testing -- uncomment when running locally
    # return RedirectResponse("https://career-stack.hub.loginradius.com/auth.aspx?action=register&return_url=http://127.0.0.1:8000/login")

    # URL for staging testing -- uncomment when running on Heroku staging
    return RedirectResponse("https://career-stack.hub.loginradius.com/auth.aspx?action=register&return_url=http://career-stack.herokuapp.com/login")



@app.get("/login")
def login(request: Request):
    params = dict(request.query_params)
    token = params['token']
    print("******************************************", token)
    res = loginradius.authentication.get_profile_by_access_token(token)

    #Need to store token in a cookie
    r.set_cookie(key="token", value=token)

    if token is None:
        # redirect the user to our LoginRadius login URL if no access token is provided
        return RedirectResponse("https://career-stack.hub.loginradius.com/auth.aspx?action=register&return_url=https://career-stack.herokuapp.com")

    return JSONResponse(content=res)

@app.get("/user-profile")
def get_user(id: str):
    res = loginradius.authentication.get_profile_by_access_token(id)
    return JSONResponse(content=res)