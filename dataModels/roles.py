from pydantic import BaseModel

class RolesBase(BaseModel):
    roleID: int
    nombre_rol: str

    class Config:
        orm_mode = True