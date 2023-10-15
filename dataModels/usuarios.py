from pydantic import BaseModel

class UsuariosBase(BaseModel):
    userID: int
    username: str
    password: str
    nombre: str
    mail: str
    puesto: str
    estado: bool
    salt: str

    class Config:
        orm_mode = True