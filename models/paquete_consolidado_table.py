from config.database import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class PaqueteConsolidado(Base):
    __tablename__ = "paquete_consolidado"

    paqueteconsolidadoID = Column(Integer, primary_key=True, autoincrement=True)
    consolidado_id = Column(Integer, ForeignKey('consolidados.consolidadoID'))
    paquete_id = Column(Integer, ForeignKey('paquetes.codigo_tracking'))

    consolidados = relationship("Consolidados")
    paquetes = relationship("Paquetes")