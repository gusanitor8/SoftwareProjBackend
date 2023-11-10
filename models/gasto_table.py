from config.database import Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship


class Gasto(Base):
    __tablename__ = "gasto"

    id_gasto = Column(Integer, primary_key=True, autoincrement=True)
    paquete_id = Column(Integer, ForeignKey('paquete.id_paquete'), unique=True, nullable=False)
    monto_iva_quetzal = Column(Float, CheckConstraint('monto_iva_quetzal > 0'), nullable=False)
    monto_dai_quetzal = Column(Float, CheckConstraint('monto_dai_quetzal > 0'), nullable=False)
    monto_flete = Column(Float, CheckConstraint('monto_flete > 0'), nullable=False)
    monto_combex = Column(Float, CheckConstraint('monto_combex > 0'), nullable=False)
    valor_quetzal = Column(Float, CheckConstraint('valor_quetzal > 0'), nullable=False)
    gasto_total = Column(Float, CheckConstraint('gasto_total > 0'), nullable=False)

    gasto_paquete = relationship("Paquete")