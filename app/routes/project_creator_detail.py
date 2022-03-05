from fastapi import APIRouter
from app.models.project_creator_detail import ProjectCreatorDetail
from app.config.db import client
from app.schemas.project_creator_detail import projectCreatorDetailEntity, projectCreatorDetailListEntity
from bson.objectid import ObjectId
from app.helpers.integromat_helper import project_creator_webhook_ping

project_creator_detail = APIRouter()

@project_creator_detail.post("/project-creator")
async def create_project_creator_details(project_creator_details: ProjectCreatorDetail):
    db = client["careerstack"]
    collection = db["project_creator_details"]
    collection.insert_one(dict(project_creator_details))
    project_creator_webhook_ping(dict(project_creator_details))
    return "Project creator details created"

@project_creator_detail.get("/project-creator/{id}")
async def get_project_creator_details_by_id(id):
    db = client["careerstack"]
    collection = db["project_creator_details"]
    return projectCreatorDetailEntity(collection.find_one({"_id": ObjectId(id)}))

@project_creator_detail.get("/project-creator/")
async def get_all_project_creator_details():
    db = client["careerstack"]
    collection = db["project_creator_details"]
    return projectCreatorDetailListEntity(collection.find())

@project_creator_detail.delete("/project-creator/{id}")
async def delete_project_creator_detail_by_id(id):
    db = client["careerstack"]
    collection = db["project_creator_details"]
    return projectCreatorDetailEntity(collection.find_one_and_delete({"_id":ObjectId(id)}))