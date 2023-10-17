from pydantic import BaseModel, constr
from datetime import date


class ConsolidadoBase(BaseModel):
    id_consolidado: int
    descripcion: constr(strip_whitespace=True, min_length=1)
    fecha_consolidacion: date
    transportista: constr(strip_whitespace=True, min_length=1)

    class Config:
        orm_mode = True