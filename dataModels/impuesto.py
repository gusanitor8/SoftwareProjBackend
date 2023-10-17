from pydantic import BaseModel, constr, validator
from datetime import date

class ImpuestoBase(BaseModel):
    id_impuesto: int
    paquete_id: int
    monto_iva_dolar: float
    dai_porcentaje: float
    monto_dai_dolar: float
    poliza: constr(strip_whitespace=True, min_length=1)
    partida: constr(strip_whitespace=True, min_length=1)
    consignatario: constr(strip_whitespace=True, min_length=1)
    fecha_impuesto: date

    @validator("dai_porcentaje")
    def check_dai_porcentaje(cls, v):
        if v < 0 or v > 100:
            raise ValueError("dai_porcentaje must be between 0 and 100")
        return v

    class Config:
        orm_mode = True