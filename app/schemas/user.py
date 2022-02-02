def userEntity(item) -> dict:
    return {
        "_id":str(item["_id"]),
        "first_name": item["first_name"],
        "last_name": item["last_name"],
        "email": item["email"],
        "password": item["password"]
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]