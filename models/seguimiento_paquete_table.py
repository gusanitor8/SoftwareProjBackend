from config.database import Base
from sqlalchemy import Column, Integer, Date, String, ForeignKey, func, CheckConstraint
from sqlalchemy.orm import relationship

class SeguimientoPaquete(Base):
    __tablename__ = "seguimiento_paquete"

    id_seguimiento = Column(Integer, primary_key=True, autoincrement=True)
    estado_actual = Column(String, CheckConstraint("estado_actual in ('en transito', 'en bodega', 'gestion aduana', 'liberado', 'listo', 'entregado')"), nullable=False)
    motivo_cambio = Column(String, nullable=False)
    paquete_id = Column(Integer, ForeignKey('paquete.id_paquete'), nullable=False)
    fecha_actualizacion = Column(Date, default=func.now(), nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuario.id_usuario'), nullable=False)

    paquete_seguido = relationship("Paquete")
    usuario_actualizador = relationship("Usuario")