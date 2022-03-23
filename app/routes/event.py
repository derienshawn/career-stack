from fastapi import APIRouter
from app.models.event import Event
from app.config.db import client
from app.schemas.event import eventEntity, eventListEntity
from bson.objectid import ObjectId

event = APIRouter()

@event.post("/events")
async def create_event(event: Event):
    db = client["careerstack"]
    collection = db["events"]
    collection.insert_one(dict(event))
    return "Event created"

@event.get("/events")
async def get_events():
    db = client["careerstack"]
    collection = db["events"]
    return eventListEntity(collection.find())

