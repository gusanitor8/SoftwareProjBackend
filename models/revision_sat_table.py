from config.database import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, func
from sqlalchemy.orm import relationship

class RevisionSat(Base):
    __tablename__ = "revision_sat"

    id_revision = Column(Integer, primary_key=True, autoincrement=True)
    valor_paquete_previo = Column(Integer, nullable=False)
    valor_dai_previo = Column(Integer, nullable=False)
    motivo_cambio = Column(String, nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuario.id_usuario'), nullable=False)
    fecha_modificacion = Column(Date, default=func.now(), nullable=False)

    usuario_revisor = relationship("Usuario")