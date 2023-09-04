from pydantic import BaseModel

class users(BaseModel):    
    email: str
    password: str

    class Config:
        orm_mode = True