from pydantic import BaseModel

class GastosBase(BaseModel):
    gastoID: int
    paquete_id: int
    monto_iva_q: float
    monto_vol_q: float
    flete_q: float
    monto_combex: float
    valor_q: float

    class Config:
        orm_mode = True