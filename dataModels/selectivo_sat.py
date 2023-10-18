from pydantic import BaseModel, constr, conint
from datetime import date


class SelectivoSatBase(BaseModel):
    id_selectivo: int
    consolidado_id: conint(gt=0)
    fecha_selectivo: date
    selectivo_asignado: constr(strip_whitespace=True, pattern="^(Rojo|Verde)$")

    class Config:
        from_attributes = True