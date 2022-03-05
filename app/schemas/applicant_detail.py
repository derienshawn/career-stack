def applicantDetailEntity(item) -> dict:
    return {
        "_id":str(item["_id"]),
        "user_id": item["user_id"],
        "project_id": item["project_id"],
        "email": item["email"],
        "role_of_interest": item["role_of_interest"],
        "applied_at": item["applied_at"],
        "application_status": item["application_status"],
        "resume": item["resume"],
        "message": item["message"]
    }
def applicantDetailListEntity(entity) -> list:
    return [applicantDetailEntity(item) for item in entity]