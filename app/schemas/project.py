def projectEntity(item) -> dict:
    return {
        "_id":str(item["_id"]),
        "project_id": item["project_id"],
        "name": item["name"],
        "icon_url": item["icon_url"],
        "images": item["images"],
        "description": item["description"],
        "estimated_deadline": item["estimated_deadline"],
        "project_budget": item["project_budget"],
        "minimum_participants": item["minimum_participants"],
        "project_requirements": item["project_requirements"],
        "definition_of_done": item["definition_of_done"],
        "project_status": item["project_status"]
    }

def projectsEntity(entity) -> list:
    return [projectEntity(item) for item in entity]