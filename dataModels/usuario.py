from pydantic import BaseModel, constr, validator
from typing import Optional

class UsuarioBase(BaseModel):
    id_usuario: int
    username: constr(strip_whitespace=True, min_length=1)
    password: constr(strip_whitespace=True, min_length=1)
    nombre: constr(strip_whitespace=True, min_length=1)
    email: constr(strip_whitespace=True, pattern="^[a-zA-Z0-9._-+]+@[a-zA-Z0-9.-+]+\.[a-zA-Z]{2,}$")
    puesto: constr(strip_whitespace=True, min_length=1)
    estado: bool
    rol: Optional[str] = "viewer"
    salt: constr(strip_whitespace=True, min_length=1)

    @validator("rol")
    def check_rol(cls, v):
        if v not in ["viewer", "editor", "admin"]:
            raise ValueError("rol debe de ser: 'viewer', 'editor', or 'admin'")
        return v

    class Config:
        orm_mode = True