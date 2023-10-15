from config.database import Base
from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

class EstadoPaquete(Base):
    __tablename__ = "estado_paquete"

    procesoID = Column(Integer, primary_key=True, autoincrement=True)
    estado_id = Column(Integer, ForeignKey('estados.estadoID'))
    paquete_id = Column(Integer, ForeignKey('paquetes.codigo_tracking'))
    fecha_actualizacion = Column(Date)

    estados = relationship("Estados")
    paquetes = relationship("Paquetes")