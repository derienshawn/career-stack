from fastapi import APIRouter
from app.models.project import Project
from app.models.project_milestone import ProjectMilestone
from app.config.db import client
from app.schemas.project import projectEntity, projectsEntity
from app.schemas.project_milestone import projectMilestoneEntity, projectMilestoneListEntity
from app.schemas.project_detail import projectDetailEntity
from app.helpers.project_helper import create_project_detail
from app.enum import project_status
from bson.objectid import ObjectId
import uuid

project = APIRouter()


@project.post("/project")
async def create_project(project: Project):
    project_id = str(uuid.uuid1())
    project.project_id = project_id
    project.project_status = str(project_status.ProjectStatus.UNPUBLISHED).replace('ProjectStatus.', '')
    db = client["careerstack"]
    collection = db["projects"]
    collection.insert_one(dict(project))
    return "Project Created"

@project.get("/projects", summary="Returns all projects.")
async def get_all_projects():
    db = client["careerstack"]
    collection = db["projects"]
    return projectsEntity(collection.find())

@project.get("/projects/{project_id}", summary="Get single project using project_id")
async def get_project_by_project_id(project_id):
    db = client["careerstack"]
    collection = db["projects"]
    return projectsEntity(collection.find({'project_id': project_id}))

@project.delete("/project/{project_id}", summary="Delete a project by project_id.")
async def delete_project(project_id):
    db = client["careerstack"]
    collection = db["projects"]
    return projectEntity(collection.find_one_and_delete({"project_id": project_id}))

@project.get("/project-detail/{id}")
async def get_project_details(id):
    db = client["careerstack"]
    collection = db["project_details"]
    project = projectDetailEntity(collection.find_one({'_id': ObjectId(id)}))
    return projectDetailEntity(project)

@project.post("/project/{id}/milestone")
async def create_project_milestone(project_milestone: ProjectMilestone):
    db = client["careerstack"]
    collection = db["project_milestones"]
    collection.insert_one(dict(project_milestone))
    return "Milestone created"

@project.get("/milestones/{project_id}")
async def get_project_milestones(project_id):
    db = client["careerstack"]
    collection = db["project_milestones"]
    return projectMilestoneListEntity(collection.find({'project_id': project_id}))

@project.delete("/milestones/{milestone_id}")
async def delete_project_milestones(milestone_id):
    db = client["careerstack"]
    collection = db["project_milestones"]
    return projectMilestoneEntity(collection.find_one_and_delete({'_id': ObjectId(milestone_id)}))
