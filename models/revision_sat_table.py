from config.database import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, func
from sqlalchemy.orm import relationship

class RevisionSat(Base):
    __tablename__ = "revision_sat"

    id_revision = Column(Integer, primary_key=True, autoincrement=True)
    selectivo_id = Column(Integer, ForeignKey('selectivo_sat.id_selectivo'), unique=True, nullable=False)
    registro_previo = Column(String, nullable=False)
    registro_actual = Column(String, nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuario.id_usuario'), nullable=False)
    fecha_modificacion = Column(Date, default=func.now(), nullable=False)

    revision_rojo = relationship("SelectivoSat")
    usuario_revisor = relationship("Usuario")