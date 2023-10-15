from config.database import Base
from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

class Gastos(Base):
    __tablename__ = "gastos"

    gastoID = Column(Integer, primary_key=True, autoincrement=True)
    paquete_id = Column(Integer, ForeignKey('paquetes.codigo_tracking'))
    monto_iva_q = Column(Float)
    monto_vol_q = Column(Float)
    flete_q = Column(Float)
    monto_combex = Column(Float)
    valor_q = Column(Float)

    paquete = relationship("Paquetes")