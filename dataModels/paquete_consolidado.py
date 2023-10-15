from pydantic import BaseModel

class PaqueteConsolidadoBase(BaseModel):
    paqueteconsolidadoID: int
    consolidado_id: int
    paquete_id: int

    class Config:
        orm_mode = True