def eventEntity(item) -> dict:
    return {
        "_id":str(item["_id"]),
        "event_id": item["event_id"],
        "title": item["title"],
        "short_description": item["short_description"],
        "image_url": item["image_url"],
        "video_conference_url": item["video_conference_url"],
        "date": item["date"],
        "details": item["details"],
        "objective": item["objective"],
        "sponsor_details": item["sponsor_details"]
    }

def eventListEntity(entity) -> list:
    return [eventEntity(item) for item in entity]