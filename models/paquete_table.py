from config.database import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class Paquete(Base):
    __tablename__ = "paquete"

    id_paquete = Column(Integer, primary_key=True, autoincrement=True)
    pedido_id = Column(Integer, ForeignKey('pedido.id_pedido'))
    codigo_rastreo = Column(String, unique = True)
    contenido = Column(String)
    descripcion = Column(String)
    alto = Column(Float)
    ancho = Column(Float)
    largo = Column(Float)
    peso_libras = Column(Float)
    peso_volumetrico = Column(Float)
    valor_producto_dolar = Column(Float)
    cantidad = Column(Integer)

    pedido = relationship("pedido")