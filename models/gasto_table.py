from config.database import Base
from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

class Gasto(Base):
    __tablename__ = "gasto"

    id_gasto = Column(Integer, primary_key=True, autoincrement=True)
    paquete_id = Column(Integer, ForeignKey('paquete.id_paquete'))
    monto_iva_quetzal = Column(Float)
    monto_dai_quetzal = Column(Float)
    monto_flete = Column(Float)
    monto_combex = Column(Float)
    valor_quetzal = Column(Float)

    paquete = relationship("paquete")