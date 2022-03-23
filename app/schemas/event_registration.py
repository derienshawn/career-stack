def eventRegistrationEntity(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "user_id": item["user_id"],
        "event_id": item["event_id"],
        "registered_at": item["registered_at"],
        "registration_status": item["registration_status"]
    }

def eventRegistrationListEntity(entity) -> list:
    return [eventRegistrationEntity(item) for item in entity]