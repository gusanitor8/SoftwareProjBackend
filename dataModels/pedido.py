from pydantic import BaseModel, constr, confloat
from datetime import date


class PedidoBase(BaseModel):
    id_pedido: int
    factura: constr(strip_whitespace=True, min_length=1)
    direccion_casillero: constr(strip_whitespace=True, min_length=1)
    fecha_pedido: date
    valor_total_dolar: confloat(min=0.01)
    empresa_remitente: constr(strip_whitespace=True, min_length=1)
    cliente_nombre: constr(strip_whitespace=True, min_length=1)
    cliente_telefono: constr(strip_whitespace=True, min_length=1)
    cliente_email: constr(strip_whitespace=True, pattern="^[a-zA-Z0-9._-+]+@[a-zA-Z0-9.-+]+\\.[a-zA-Z]{2,}$")
    cliente_direccion: constr(strip_whitespace=True, min_length=1)

    class Config:
        orm_mode = True