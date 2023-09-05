from pydantic import BaseModel
from typing import Optional

class users(BaseModel):    
    email: str
    password: str
    role: Optional[str] = "viewer"

    class Config:
        orm_mode = True