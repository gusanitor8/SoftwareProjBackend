from pydantic import BaseModel

class UsuarioBase(BaseModel):
    id_usuario: int
    username: str
    password: str
    nombre: str
    email: str
    puesto: str
    estado: bool
    salt: str

    class Config:
        orm_mode = True