from pydantic import BaseModel
from datetime import date

class ConsolidadoBase(BaseModel):
    id_consolidado: int
    descripcion: str
    fecha_consolidacion: date
    transportista: str

    class Config:
        orm_mode = True