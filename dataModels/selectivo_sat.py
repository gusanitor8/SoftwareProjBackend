from pydantic import BaseModel
from datetime import date

class SelectivoSatBase(BaseModel):
    id_selectivo: int
    consolidado_id: int
    fecha_selectivo: date
    selectivo_asignado: str

    class Config:
        orm_mode = True