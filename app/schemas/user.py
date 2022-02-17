def userEntity(item) -> dict:
    return {
        "_id":str(item["_id"]),
        "user_id": item["user_id"],
        "first_name": item["first_name"],
        "last_name": item["last_name"],
        "email": item["email"],
        "image_url": item["image_url"]
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]