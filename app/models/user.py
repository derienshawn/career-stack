from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
        user_id: str
        first_name: str
        last_name: str
        email: str
        image_url: Optional[str]
