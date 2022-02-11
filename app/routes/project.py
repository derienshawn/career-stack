from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.models.project import Project
from app.config.db import client
from app.schemas.project import projectEntity, projectsEntity
from app.schemas.project_detail import projectDetailEntity
from app.helpers.project_helper import create_project_detail
from bson.objectid import ObjectId
import uuid
import json

project = APIRouter()

@project.post("/project")
async def create_project(project: Project):
    project_id = str(uuid.uuid1())
    project.project_id = project_id
    db = client["careerstack"]
    collection = db["projects"]
    collection.insert_one(dict(project))
    project_info_to_create_details = projectEntity(collection.find_one({'project_id': project_id}))
    project_details = create_project_detail(project_info_to_create_details)
    collection = db["project_details"]
    project_details_formatted = json.loads(project_details.body)
    collection.insert_one(project_details_formatted)
    return JSONResponse(content=str(project_details.body, 'UTF-8'))

@project.get("/projects")
async def get_all_projects():
    db = client["careerstack"]
    collection = db["projects"]
    return projectsEntity(collection.find())

@project.delete("/project/{id}")
async def delete_project(id):
    db = client["careerstack"]
    collection = db["projects"]
    project_to_delete = projectEntity(collection.find_one({'_id': ObjectId(id)}))
    project_to_delete["_id"]
    collection = db["project_details"]
    projectDetailEntity(collection.find_one({'project_id': project_to_delete["project_id"]}))
    projectDetailEntity(collection.find_one_and_delete({'project_id': project_to_delete["project_id"]}))
    collection = db["projects"]
    return projectEntity(collection.find_one_and_delete({"_id":ObjectId(id)}))

@project.get("/project-detail/{id}")
async def get_project_details(id):
    db = client["careerstack"]
    collection = db["projects"]
    project = projectEntity(collection.find_one({'_id': ObjectId(id)}))
    test_project = create_project_detail(project)
    return test_project
