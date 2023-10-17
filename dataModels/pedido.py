from pydantic import BaseModel, constr, validator
from datetime import date

class PedidoBase(BaseModel):
    id_pedido: int
    factura: constr(strip_whitespace=True, min_length=1)
    direccion_casillero: constr(strip_whitespace=True, min_length=1)
    fecha_pedido: date
    valor_total_dolar: float
    empresa_remitente: constr(strip_whitespace=True, min_length=1)
    cliente_nombre: constr(strip_whitespace=True, min_length=1)
    cliente_telefono: constr(strip_whitespace=True, min_length=1)
    cliente_email: constr(strip_whitespace=True, min_length=1)
    cliente_direccion: constr(strip_whitespace=True, min_length=1)

    @validator("valor_total_dolar")
    def check_valor_total_dolar(cls, v):
        if v <= 0:
            raise ValueError("valor_total_dolar must be greater than 0")
        return v

    class Config:
        orm_mode = True

