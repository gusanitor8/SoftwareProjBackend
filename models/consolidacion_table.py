from config.database import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Consolidacion(Base):
    __tablename__ = "consolidacion"

    id_consolidacion = Column(Integer, primary_key=True, autoincrement=True)
    paquete_id = Column(Integer, ForeignKey('paquete.id_paquete'))
    consolidado_id = Column(Integer, ForeignKey('consolidado.id_consolidado'))

    consolidado = relationship("consolidado")
    paquete = relationship("paquete")