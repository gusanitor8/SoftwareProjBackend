from pydantic import BaseModel

class ConsolidacionBase(BaseModel):
    id_consolidacion: int
    paquete_id: int
    consolidado_id: int

    class Config:
        orm_mode = True