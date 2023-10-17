from config.database import Base
from sqlalchemy import Column, Integer, Date, String, ForeignKey, func
from sqlalchemy.orm import relationship

class CambioUsuario(Base):
    __tablename__ = "cambio_usuario"

    id_cambio = Column(Integer, primary_key=True, autoincrement=True)
    modificado_id = Column(Integer, ForeignKey('usuario.id_usuario'))
    valor_previo = Column(String)
    valor_actual = Column(String)
    campo_modificado = Column(String)
    fecha_cambio = Column(Date, default=func.now())
    modificador_id = Column(Integer, ForeignKey('usuario.id_usuario'))

    usuario_modificado = relationship('Usuario', foreign_keys=[modificado_id])
    usuario_modificador = relationship('Usuario', foreign_keys=[modificador_id], backref='cambios')