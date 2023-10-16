from config.database import Base
from sqlalchemy import Column, Integer, String, Float, Date

class Pedido(Base):
    __tablename__ = "pedido"

    id_pedido = Column(Integer, primary_key=True, autoincrement=True)
    factura = Column(String, unique=True)
    direccion_casillero = Column(String)
    fecha_pedido = Column(Date)
    valor_total_dolar = Column(Float)
    empresa_remitente = Column(String)
    cliente_nombre = Column(String)
    cliente_telefono = Column(String)
    cliente_email = Column(String)
    cliente_direccion = Column(String)