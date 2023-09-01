from config.database import Base
from sqlalchemy import Column, BigInteger, String, ForeignKey
from sqlalchemy.orm import relationship

class Destino(Base):
    __tablename__ = "Destino"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    No_guia = Column(BigInteger, ForeignKey('Guia.no_guia'))
    DESTINO_nombre = Column(String)
    DESTINO_direccion = Column(String)
    DESTINO_codigo_postal = Column(BigInteger)
    DESTINO_ciudad = Column(String)
    DESTINO_estado = Column(String)
    DESTINO_pais = Column(String)
    DESTINO_telefono = Column(BigInteger)

    guia = relationship("Guia")
    