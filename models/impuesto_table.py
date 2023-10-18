from config.database import Base
from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey, CheckConstraint, func
from sqlalchemy.orm import relationship


class Impuesto(Base):
    __tablename__ = "impuesto"

    id_impuesto = Column(Integer, primary_key=True, autoincrement=True)
    paquete_id = Column(String, ForeignKey('paquete.id_paquete'), unique=True, nullable=False)
    monto_iva_dolar = Column(Float, CheckConstraint('monto_iva_dolar > 0'), nullable=False)
    dai_porcentaje = Column(Float, CheckConstraint('dai_porcentaje >= 0 AND dai_porcentaje <= 100'), nullable=False)
    monto_dai_dolar = Column(Float, CheckConstraint('monto_dai_dolar > 0'),nullable=False)
    poliza = Column(String, nullable=False)
    partida = Column(String, nullable=False)
    consignatario = Column(String, nullable=False)
    fecha_impuesto = Column(Date, default=func.now(), nullable=False)

    impuesto_paquete = relationship("paquete")