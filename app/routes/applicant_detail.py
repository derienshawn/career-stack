from fastapi import APIRouter
from app.models.applicant_detail import ApplicantDetail
from app.config.db import client
from app.schemas.applicant_detail import applicantDetailEntity, applicantDetailListEntity
from bson.objectid import ObjectId

applicant_detail = APIRouter()

@applicant_detail.post("/applicant-detail")
async def create_applicant_detail(ad: ApplicantDetail):
    db = client["careerstack"]
    collection = db["applicant_details"]
    collection.insert_one(dict(ad))
    return "Applicant detail created."

@applicant_detail.get("/applicant-detail/{id}")
async def get_applicant_detail_by_id(id):
    db = client["careerstack"]
    collection = db["applicant_details"]
    return applicantDetailEntity(collection.find_one({"_id":ObjectId(id)}))

@applicant_detail.delete("/applicant-detail/{id}")
async def delete_project_detail_by_id(id):
    db = client["careerstack"]
    collection = db["applicant_details"]
    return applicantDetailEntity(collection.find_one_and_delete({"_id":ObjectId(id)}))