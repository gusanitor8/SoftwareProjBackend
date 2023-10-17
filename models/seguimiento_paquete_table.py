from config.database import Base
from sqlalchemy import Column, Integer, Date, String, ForeignKey
from sqlalchemy.orm import relationship

class SeguimientoPaquete(Base):
    __tablename__ = "seguimiento_paquete"

    id_seguimiento = Column(Integer, primary_key=True, autoincrement=True)
    estado_actual = Column(String)
    motivo_cambio = Column(String)
    paquete_id = Column(Integer, ForeignKey('paquete.id_paquete'))
    fecha_actualizacion = Column(Date)
    usuario_id = Column(Integer, ForeignKey('usuario.id_usuario'))

    paquete = relationship("paquete")
    usuario = relationship("usuario")