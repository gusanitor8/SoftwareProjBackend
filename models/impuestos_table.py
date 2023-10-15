from config.database import Base
from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from sqlalchemy.orm import relationship

class Impuestos(Base):
    __tablename__ = "impuestos"

    polizaID = Column(Integer, primary_key=True, autoincrement=True)
    tracking_id = Column(Integer, ForeignKey('paquetes.codigo_tracking'))
    IVA = Column(Float)
    monto_iva = Column(Float)
    DAI = Column(Float)
    monto_dai = Column(Float)
    partida = Column(String)
    consignatario = Column(String)
    fecha_impuesto = Column(Date)

    paquetes = relationship("Paquetes")