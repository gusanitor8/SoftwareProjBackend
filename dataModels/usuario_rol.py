from pydantic import BaseModel

class UsuarioRolBase(BaseModel):
    rol_usuarioID: int
    user_id: int
    role_id: int

    class Config:
        orm_mode = True