from pydantic import BaseModel, constr


class UsuarioBase(BaseModel):
    id_usuario: int
    username: constr(strip_whitespace=True, min_length=1)
    password: constr(strip_whitespace=True, min_length=1)
    nombre: constr(strip_whitespace=True, min_length=1)
    email: constr(strip_whitespace=True, pattern="^[a-zA-Z0-9._-+]+@[a-zA-Z0-9.-+]+\\.[a-zA-Z]{2,}$")
    puesto: constr(strip_whitespace=True, min_length=1)
    estado: bool
    rol: constr(strip_whitespace=True, pattern="^(viewer|editor|admin)$") = "viewer"
    salt: constr(strip_whitespace=True, min_length=1)

    class Config:
        orm_mode = True    