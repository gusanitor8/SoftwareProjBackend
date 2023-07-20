from pydantic import BaseModel

class RemitenteBase(BaseModel):
    id: int
    No_guia: int
    compania: str
    contacto: str
    email: str
    direccion: str
    codigo_postal: int
    ciudad: str
    estado: str
    pais: str
    telefono: int

    class Config:
        orm_mode = True
