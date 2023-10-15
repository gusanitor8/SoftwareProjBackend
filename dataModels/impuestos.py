from pydantic import BaseModel
from datetime import date

class ImpuestosBase(BaseModel):
    polizaID: int
    tracking_id: int
    IVA: float
    monto_iva: float
    DAI: float
    monto_dai: float
    partida: str
    consignatario: str
    fecha_impuesto: date

    class Config:
        orm_mode = True