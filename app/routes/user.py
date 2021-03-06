
from fastapi import APIRouter
from app.models.user import User
from app.helpers.redis_helper import get_token, set_token
from app.config.db import client
from app.schemas.user import userEntity, usersEntity
from bson.objectid import ObjectId

user = APIRouter()

@user.post("/user")
async def create_user(user: User):
    db = client["careerstack"]
    collection = db["users"]
    collection.insert_one(dict(user))
    return "User created"

@user.get("/users")
async def get_all_users():
    db = client["careerstack"]
    collection = db["users"]
    return usersEntity(collection.find())

@user.delete("/user/{id}")
async def delete_user(id):
    db = client["careerstack"]
    collection = db["users"]
    return userEntity(collection.find_one_and_delete({"_id":ObjectId(id)}))

