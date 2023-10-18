from config.database import Base
from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship


class Consolidacion(Base):
    __tablename__ = "consolidacion"

    id_consolidacion = Column(Integer, primary_key=True, autoincrement=True)
    paquete_id = Column(String, ForeignKey('paquete.id_paquete'), nullable=False)
    consolidado_id = Column(Integer, ForeignKey('consolidado.id_consolidado'), nullable=False)

    contenido = relationship("Consolidado")
    paquete_consolidado = relationship("Paquete")