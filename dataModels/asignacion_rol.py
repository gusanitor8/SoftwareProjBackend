from pydantic import BaseModel

class AsignacionRolBase(BaseModel):
    id_asignacion: int
    usuario_id: int
    rol_id: int

    class Config:
        orm_mode = True