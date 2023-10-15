from pydantic import BaseModel
from datetime import date

class ModificacionSATBase(BaseModel):
    mod_sat_id: int
    revision: int
    registro_antiguo: str
    registro_nuevo: str
    fecha_modificacion: date

    class Config:
        orm_mode = True