def projectMilestoneEntity(item) -> dict:
    return {
        "_id":str(item["_id"]),
        "project_id": item["project_id"],
        "project_creator_id": item["project_creator_id"],
        "name": item["name"],
        "description": item["description"],
        "status": item["status"],
        "estimated_deadline": item["estimated_deadline"],
        "completed_at": item["completed_at"]
    }
def projectMilestoneListEntity(entity) -> list:
    return [projectMilestoneEntity(item) for item in entity]