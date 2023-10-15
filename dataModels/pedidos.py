from pydantic import BaseModel
from datetime import date

class PedidosBase(BaseModel):
    codigo_invoice: int
    casillero: str
    fecha_pedido: date
    valor_total: float
    compania_remitente: str
    nombre_cliente: str
    tel_cliente: str
    mail_cliente: str
    direccion_cliente: str

    class Config:
        orm_mode = True
