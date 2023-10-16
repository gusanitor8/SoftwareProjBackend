from config.database import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class AsignacionRol(Base):
    __tablename__ = "asignacion_rol"

    id_asignacion = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id_usuario'))
    rol_id = Column(Integer, ForeignKey('rol.id_rol'))

    usuario = relationship("usuario")
    rol = relationship("rol")