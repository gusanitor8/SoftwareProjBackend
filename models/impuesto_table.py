from config.database import Base
from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from sqlalchemy.orm import relationship

class Impuesto(Base):
    __tablename__ = "impuesto"

    id_impuesto = Column(Integer, primary_key=True, autoincrement=True)
    paquete_id = Column(Integer, ForeignKey('paquete.id_paquete'), unique = True)
    monto_iva_dolar = Column(Float)
    dai_porcentaje = Column(Float)
    monto_dai_dolar = Column(Float)
    poliza = Column(String)
    partida = Column(String)
    consignatario = Column(String)
    fecha_impuesto = Column(Date)

    paquete = relationship("paquete")