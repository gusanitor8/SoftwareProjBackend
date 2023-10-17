from pydantic import BaseModel

class GastoBase(BaseModel):
    id_gasto: int
    paquete_id: int
    monto_iva_quetzal: float
    monto_dai_quetzal: float
    monto_flete: float
    monto_combex: float
    valor_quetzal: float
    gasto_total: float

    class Config:
        orm_mode = True