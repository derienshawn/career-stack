from pydantic import BaseModel
from datetime import datetime

class ApplicantDetail(BaseModel):
    user_id: str
    project_id: str
    email: str
    role_of_interest: str
    applied_at: datetime
    application_status: str
    resume: str
    message: str