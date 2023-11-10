from config.database import Base
from sqlalchemy import Column, Integer, String, Float, Date, CheckConstraint


class Paquete(Base):
    __tablename__ = "paquete"

    id_paquete = Column(Integer, primary_key=True, autoincrement=True)
    factura = Column(String, nullable=False)
    fecha_orden = Column(Date, nullable=False)
    contenido = Column(String, nullable=False)
    descripcion = Column(String, nullable=False)
    alto = Column(Float, CheckConstraint('alto > 0'), nullable=False)
    ancho = Column(Float, CheckConstraint('ancho > 0'), nullable=False)
    largo = Column(Float, CheckConstraint('largo > 0'), nullable=False)
    peso_libras = Column(Float, CheckConstraint('peso_libras > 0'), nullable=False)
    peso_volumetrico = Column(Float, CheckConstraint('peso_volumetrico > 0'), nullable=False)
    valor_producto_dolar = Column(Float, CheckConstraint('valor_producto_dolar > 0'), nullable=False)
    unidades = Column(Integer, CheckConstraint('unidades >= 1'), nullable=False)
    direccion_casillero = Column(String, nullable=False)
    empresa_remitente = Column(String, nullable=False)
    cliente_nombre = Column(String, nullable=False)
    cliente_telefono = Column(String, nullable=False)
    cliente_email = Column(String, nullable=False)
    cliente_direccion = Column(String, nullable=False)