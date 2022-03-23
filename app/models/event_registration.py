from pydantic import BaseModel
from datetime import datetime

class EventRegistration(BaseModel):
    user_id: str
    event_id: str
    registered_at: datetime
    registration_status: str