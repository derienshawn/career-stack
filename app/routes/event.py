from fastapi import APIRouter
from app.models.event import Event
from app.models.event_registration import EventRegistration
from app.config.db import client
from app.schemas.event import eventEntity, eventListEntity
from app.schemas.event_registration import eventRegistrationEntity
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

@event.get("/events/{id}")
async def get_event_by_id(id):
    db = client["careerstack"]
    collection = db["events"]
    return eventListEntity(collection.find({"event_id": id}))

@event.delete("/events/{id}")
async def delete_event_by_id(id):
    db = client["careerstack"]
    collection = db["events"]
    return eventEntity(collection.find_one_and_delete({"_id":ObjectId(id)}))

@event.post("/events/register")
async def create_event_registration(event_registration: EventRegistration):
    db = client["careerstack"]
    collection = db["event_registrations"]
    collection.insert_one(dict(event_registration))
    return "User registered successfully"

