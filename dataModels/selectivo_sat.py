from pydantic import BaseModel, constr, validator
from datetime import date

class SelectivoSatBase(BaseModel):
    id_selectivo: int
    consolidado_id: int
    fecha_selectivo: date
    selectivo_asignado: constr(strip_whitespace=True, min_length=1)

    @validator("selectivo_asignado")
    def check_selectivo_asignado(cls, v):
        if v not in ["Rojo", "Verde"]:
            raise ValueError("selectivo_asignado must be either 'Rojo' or 'Verde'")
        return v

    class Config:
        orm_mode = True