from pydantic import BaseModel

class ProjectCreatorDetail(BaseModel):
    project_id: str
    project_creator_id: str
    first_name: str
    last_name: str
    email: str