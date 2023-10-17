from config.database import Base
from sqlalchemy import Column, Integer, String, Float, Date, CheckConstraint


class Pedido(Base):
    __tablename__ = "pedido"

    id_pedido = Column(Integer, primary_key=True, autoincrement=True)
    factura = Column(String, unique=True, nullable=False)
    direccion_casillero = Column(String, nullable=False)
    fecha_pedido = Column(Date, nullable=False)
    valor_total_dolar = Column(Float, CheckConstraint('valor_total_dolar > 0'), nullable=False)
    empresa_remitente = Column(String, nullable=False)
    cliente_nombre = Column(String, nullable=False)
    cliente_telefono = Column(String, nullable=False)
    cliente_email = Column(String, nullable=False)
    cliente_direccion = Column(String, nullable=False)