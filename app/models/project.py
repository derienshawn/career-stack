from datetime import datetime
from pydantic import BaseModel

class Project(BaseModel):
    project_id: str
    name: str
    icon_url: str
    images: list
    description: str
    estimated_deadline: datetime
    project_budget: float
    minimum_participants: int
    project_requirements: str
    definition_of_done: str
    project_status: str
