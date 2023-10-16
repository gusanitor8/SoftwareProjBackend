from pydantic import BaseModel

class ConsolidacionBase(BaseModel):
    id_consolidacion: int
    consolidado_id: int
    paquete_id: int

    class Config:
        orm_mode = True