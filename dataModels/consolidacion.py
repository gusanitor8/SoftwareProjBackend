from pydantic import BaseModel, conint


class ConsolidacionBase(BaseModel):
    # id_consolidacion autogenerado
    paquete_id: conint(gt=0)
    consolidado_id: conint(gt=0)

    class Config:
        from_attributes = True