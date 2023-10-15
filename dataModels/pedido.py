from pydantic import BaseModel
from datetime import date

class PedidoBase(BaseModel):
    id_pedido: int
    factura: str
    direccion_casillero: str
    fecha_pedido: date
    valor_total_dolar: float
    empresa_remitente: str
    cliente_nombre: str
    cliente_telefono: str
    cliente_email: str
    cliente_direccion: str

    class Config:
        orm_mode = True
