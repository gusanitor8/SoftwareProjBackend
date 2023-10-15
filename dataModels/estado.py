from pydantic import BaseModel

class EstadoBase(BaseModel):
    id_estado: int
    estado: str

    class Config:
        orm_mode = True