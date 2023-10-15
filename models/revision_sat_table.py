from config.database import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship


class RevisionSat(Base):
    __tablename__ = "revision_sat"

    id_revision = Column(Integer, primary_key=True, autoincrement=True)
    selectivo_id = Column(Integer, ForeignKey('selectivo_sat.id_selectivo'), unique=True)
    registro_previo = Column(String)
    registro_actual = Column(String)
    usuario_id = Column(Integer, ForeignKey('usuario.id_usuario'))
    fecha_modificacion = Column(Date)

    selectivo_sat = relationship("selectivo_sat")
    usuario = relationship("usuario")