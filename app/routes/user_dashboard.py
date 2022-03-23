from fastapi import APIRouter
from app.config.db import client
from app.schemas.event_registration import eventRegistrationListEntity
from app.schemas.applicant_detail import applicantDetailListEntity
from bson.objectid import ObjectId

dashboard = APIRouter()

@dashboard.get("/dashboard/event-count/{user_id}")
async def get_user_event_count(user_id):
    db = client["careerstack"]
    collection = db["event_registrations"]
    event_count = len(eventRegistrationListEntity(collection.find({"user_id": user_id})))
    return event_count

@dashboard.get("/dashboard/project-count/{user_id}")
async def get_user_project_count(user_id):
    db = client["careerstack"]
    collection = db["applicant_details"]
    project_count = len(applicantDetailListEntity(collection.find({"user_id": user_id})))
    return project_count