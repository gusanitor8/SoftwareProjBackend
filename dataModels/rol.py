from pydantic import BaseModel

class RolBase(BaseModel):
    id_rol: int
    rol: str

    class Config:
        orm_mode = True