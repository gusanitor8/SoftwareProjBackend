from config.database import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship

class Paquete(Base):
    __tablename__ = "paquete"

    id_paquete = Column(Integer, primary_key=True, autoincrement=True)
    pedido_id = Column(Integer, ForeignKey('pedido.id_pedido'), nullable=False)
    codigo_rastreo = Column(String, unique=True, nullable=False)
    contenido = Column(String, nullable=False)
    descripcion = Column(String, nullable=False)
    alto = Column(Float, CheckConstraint('alto>0'), nullable=False)
    ancho = Column(Float, CheckConstraint('ancho>0'), nullable=False)
    largo = Column(Float, CheckConstraint('largo>0'), nullable=False)
    peso_libras = Column(Float, CheckConstraint('peso_libras>0'), nullable=False)
    peso_volumetrico = Column(Float, CheckConstraint('peso_volumetrico>0'), nullable=False)
    valor_producto_dolar = Column(Float, CheckConstraint('valor_producto_dolar>0'), nullable=False)
    unidades = Column(Integer, CheckConstraint('unidades>=1'), nullable=False)

    pedido = relationship("pedido")
