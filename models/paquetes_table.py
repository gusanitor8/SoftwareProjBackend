from config.database import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class Paquetes(Base):
    __tablename__ = "paquetes"

    codigo_tracking = Column(Integer, primary_key=True, autoincrement=True)
    invoice_id = Column(Integer, ForeignKey('pedidos.codigo_invoice'))
    contenido = Column(String)
    descripcion = Column(String)
    alto = Column(Float)
    ancho = Column(Float)
    largo = Column(Float)
    peso_lbs = Column(Float)
    peso_vol = Column(Float)
    valor_producto = Column(Float)
    cantidad = Column(Integer)

    pedidos = relationship("Pedidos")