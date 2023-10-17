from pydantic import BaseModel, conint


class ConsolidacionBase(BaseModel):
    id_consolidacion: int
    paquete_id: conint(gt=0)
    consolidado_id: conint(gt=0)

    class Config:
        orm_mode = True