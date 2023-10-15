from pydantic import BaseModel
from datetime import date

class SelectivoSATBase(BaseModel):
    revisionID: int
    consolidado_id: int
    fecha_selectivo: date
    selectivo: str

    class Config:
        orm_mode = True