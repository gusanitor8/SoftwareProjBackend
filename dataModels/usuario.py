from pydantic import BaseModel
from typing import Optional

class UsuarioBase(BaseModel):
    id_usuario: int
    username: str
    password: str
    nombre: str
    email: str
    puesto: str
    estado: bool
    rol: Optional[str] = "viewer"
    salt: str

    class Config:
        orm_mode = True