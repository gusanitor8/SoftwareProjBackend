from pydantic import BaseModel
from datetime import date

class ConsolidadosBase(BaseModel):
    consolidadoID: int
    descripcion: str
    fecha_consolidacion: date
    carrier: str

    class Config:
        orm_mode = True