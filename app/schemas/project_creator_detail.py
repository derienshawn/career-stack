def projectCreatorDetailEntity(item) -> dict:
    return {
        "_id":str(item["_id"]),
        "project_id": item["project_id"],
        "project_creator_id": item["project_creator_id"],
        "first_name": item["first_name"],
        "last_name": item["last_name"],
        "email": item["email"]
    }
def projectCreatorDetailListEntity(entity) -> list:
    return [projectCreatorDetailEntity(item) for item in entity]