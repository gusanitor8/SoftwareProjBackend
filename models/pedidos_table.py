from config.database import Base
from sqlalchemy import Column, Integer, String, Float, Date

class Pedidos(Base):
    __tablename__ = "pedidos"

    codigo_invoice = Column(Integer, primary_key=True, autoincrement=True)
    casillero = Column(String)
    fecha_pedido = Column(Date)
    valor_total = Column(Float)
    compania_remitente = Column(String)
    nombre_cliente = Column(String)
    tel_cliente = Column(String)
    mail_cliente = Column(String)
    direccion_cliente = Column(String)