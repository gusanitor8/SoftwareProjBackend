from config.database import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

class CambioUsuario(Base):
    __tablename__ = "cambio_usuario"

    id_cambio = Column(Integer, primary_key=True, autoincrement=True)
    modificado_id = Column(Integer, ForeignKey('usuario.id_usuario'))
    valor_previo = Column(String)
    valor_actual = Column(String)
    campo_modificado = Column(String)
    fecha_cambio = Column(Date)
    modificador_id = Column(Integer, ForeignKey('usuario.id_usuario'))

    usuario = relationship('usuario')