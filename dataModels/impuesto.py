from pydantic import BaseModel
from datetime import date

class ImpuestoBase(BaseModel):
    id_impuesto: int
    paquete_id: int
    monto_iva_dolar: float
    dai_porcentaje: float
    monto_dai_dolar: float
    poliza: str
    partida: str
    consignatario: str
    fecha_impuesto: date

    class Config:
        orm_mode = True