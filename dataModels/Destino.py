from pydantic import BaseModel

class DestinoBase(BaseModel):
    id: int
    No_guia: int
    nombre: str
    direccion: str
    codigo_postal: int
    ciudad: str
    estado: str
    pais: str
    telefono: int

    class Config:
        orm_mode = True