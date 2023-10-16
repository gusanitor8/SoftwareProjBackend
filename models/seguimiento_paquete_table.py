from config.database import Base
from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

class SeguimientoPaquete(Base):
    __tablename__ = "seguimiento_paquete"

    id_seguimiento = Column(Integer, primary_key=True, autoincrement=True)
    estado_previo_id = Column(Integer, ForeignKey('estado.id_estado'))
    estado_actual_id = Column(Integer, ForeignKey('estado.id_estado'))
    paquete_id = Column(Integer, ForeignKey('paquete.id_paquete'))
    fecha_actualizacion = Column(Date)

    estado = relationship("estado")
    paquete = relationship("paquete")