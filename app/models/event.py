from pydantic import BaseModel
from datetime import datetime

class Event(BaseModel):
    event_id: str
    title: str
    short_description: str
    image_url: str
    video_conference_url: str
    date: datetime
    details: str
    objective: str
    sponsor_details: str