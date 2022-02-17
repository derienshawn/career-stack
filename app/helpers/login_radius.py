from fastapi import Request
from fastapi.responses import RedirectResponse, JSONResponse
from app.helpers import redis_helper
from app.models.user import User
from LoginRadius import LoginRadius as LR


LR.API_KEY = "5a253b16-8b8e-49da-8bd6-5fcf6ad5a968"
LR.API_SECRET = "a0a208b2-181e-4303-8fad-ca993af14cf2"

loginradius = LR()


register_local_url = "https://career-stack.hub.loginradius.com/auth.aspx?action=register&return_url=http://127.0.0.1:8000/register-redirect"
register_staging_url = "https://career-stack.hub.loginradius.com/auth.aspx?action=register&return_url=https://career-stack.herokuapp.com/register-redirect"


def register():
    # URL for local testing -- uncomment when running locally
    # return RedirectResponse(register_local_url)

    # URL for staging testing -- uncomment when running on Heroku staging
    return RedirectResponse(register_staging_url)


def login_radius_redirect(request: Request):
    user_token = redis_helper.set_token(request)
    res = loginradius.authentication.get_profile_by_access_token(user_token)

    if user_token is None:
        # redirect the user to our LoginRadius login URL if no access token is provided
        # return RedirectResponse(register_staging_url)
        return RedirectResponse(register_staging_url)

    return JSONResponse(content=res)

def logout():
    token_as_str = redis_helper.get_token()

    if token_as_str is None:
        return "No token found"

    # invalidate the access token with LoginRadius API
    loginradius.authentication.auth_in_validate_access_token(token_as_str)
    return RedirectResponse(register_staging_url)

def get_current_logged_in_user_profile():
    token = redis_helper.get_token()
    res = loginradius.authentication.get_profile_by_access_token(token)
    user_id = res["ID"]
    first_name = res["FirstName"]
    last_name = res["LastName"]
    email = res["Email"][0]['Value']
    image_url = res["ImageUrl"]
    user = User(user_id = user_id, first_name = first_name, last_name = last_name, email = email, image_url = image_url)
    return JSONResponse(content=dict(user))

def get_user_profile_by_user_id(id):
    res = loginradius.account.get_account_profile_by_uid(id)
    user_id = res["ID"]
    first_name = res["FirstName"]
    last_name = res["LastName"]
    email = res["Email"][0]['Value']
    image_url = res["ImageUrl"]
    user = User(user_id = user_id, first_name = first_name, last_name = last_name, email = email, image_url = image_url)
    return JSONResponse(content=dict(user))

def delete_user_by_email(email):
    res = loginradius.account.account_delete_by_email(email)
    return JSONResponse(content=res)

def update_user_by_uid(uid):
    res = loginradius.account.update_account_by_uid(uid)
    return JSONResponse(content=res)