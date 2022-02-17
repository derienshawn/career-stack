from app.models.project_creator_detail import ProjectDetail
from app.helpers import login_radius
from app.helpers import redis_helper
from fastapi.responses import JSONResponse
import json

def create_project_detail(project):
    project_creator_token = redis_helper.get_token()
    project_creator_info = login_radius.get_user(project_creator_token)
    updated_project_info = json.loads(str(project_creator_info.body, 'UTF-8'))
    project_id = project["project_id"]
    project_creator_id = updated_project_info["ID"]
    first_name = updated_project_info["FirstName"]
    last_name = updated_project_info["LastName"]
    email = updated_project_info["Email"][0]["Value"]
    project_details = ProjectDetail(project_id = project_id, project_creator_id = project_creator_id, first_name = first_name, last_name = last_name, email = email)
    project_details_as_dict = dict(project_details)
    return JSONResponse(content=project_details_as_dict)
