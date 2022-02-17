from pydantic import BaseModel
from datetime import datetime

class ProjectMilestone(BaseModel):
    project_id: str
    project_creator_id: str
    name: str
    description: str
    status: str
    estimated_deadline: datetime
    completed_at: datetime