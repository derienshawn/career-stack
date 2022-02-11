from fastapi import APIRouter
from app.models.project_detail import ProjectDetail
from app.config.db import client
from app.schemas.project_detail import projectDetailEntity
from bson.objectid import ObjectId

project_detail = APIRouter()

@project_detail.post("/project-detail")
async def create_project_details(project_details: ProjectDetail):
    db = client["careerstack"]
    collection = db["project_details"]
    collection.insert_one(dict(project_details))
    return "Project details created"

@project_detail.get("/project-detail/{id}")
async def get_project_details_by_id():
    db = client["careerstack"]
    collection = db["project_details"]
    return projectDetailEntity(collection.find())

@project_detail.delete("/project-detail/{id}")
async def delete_project_detail_by_id(id):
    db = client["careerstack"]
    collection = db["project_details"]
    return projectDetailEntity(collection.find_one_and_delete({"_id":ObjectId(id)}))