from pydantic import BaseModel

class EstadosBase(BaseModel):
    estadoID: int
    estado: str

    class Config:
        orm_mode = True