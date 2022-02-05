from fastapi import APIRouter, FastAPI
from app.models.project import Project
from app.config.db import client
from app.schemas.project import projectEntity, projectsEntity
from bson.objectid import ObjectId

project = APIRouter()

@project.post("/project")
async def create_project(project: Project):
    db = client["careerstack"]
    collection = db["projects"]
    collection.insert_one(dict(project))
    return "Project created"

@project.get("/projects")
async def get_all_projects():
    user_list = []
    db = client["careerstack"]
    collection = db["projects"]
    return projectsEntity(collection.find())

@project.delete("/project/{id}")
async def delete_project(id):
    db = client["careerstack"]
    collection = db["projects"]
    return projectEntity(collection.find_one_and_delete({"_id":ObjectId(id)}))