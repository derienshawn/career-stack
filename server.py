from fastapi import FastAPI, Request
from app.routes.user import user
from app.routes.project import project
from app.routes.user_dashboard import dashboard
from app.routes.project_creator_detail import project_creator_detail
from app.routes.applicant_detail import applicant_detail
from app.routes.event import event
from app.helpers import login_radius
import redis
import os

# Redis config to run Locally
# redis = redis.Redis(host= 'localhost',port= '6379')

#Redis config to run staging on Heroku
redis_url = os.environ.get('REDIS_URL', 'redis://localhost:6379')
redis = redis.from_url(redis_url)

app = FastAPI()
app.include_router(project, tags=["Project"])
app.include_router(project_creator_detail, tags=["Project Creator Details"])
app.include_router(applicant_detail, tags=["Applicant Details"])
app.include_router(event, tags=["Events"])
app.include_router(dashboard, tags=["User Dashboard"])


@app.get("/register")
def register():
   return login_radius.register()

@app.get("/register-redirect")
def login(request: Request):
    return login_radius.login_radius_redirect(request)

@app.get("/logout")
def logout():
    return login_radius.logout()

@app.get("/user-profile", summary="Get User profile of the currently logged in user.")
def get_current_logged_in_user_profile():
    return login_radius.get_current_logged_in_user_profile()

@app.get("/user-profile/{uid}", summary="Get User Profile by Uid")
def get_user_profile_by_id(uid):
    return login_radius.get_user_profile_by_user_id(uid)

@app.delete("/user-profile/", summary="Delete User account by email.", description="Send email as string request parameter.")
def delete_user_account_by_email(email):
    return login_radius.delete_user_by_email(email)

@app.post("user-profile/{uid}", summary="Update User profile by Uid.", description="Send updated User values as requests params.")
def update_user_profile_by_uid(uid):
    return login_radius.update_user_by_uid(uid)
