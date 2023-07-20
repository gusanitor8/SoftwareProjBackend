from config.database import Base
from sqlalchemy import Column, BigInteger, String, ForeignKey
from sqlalchemy.orm import relationship

class Destino(Base):
    __tablename__ = "Destino"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    No_guia = Column(BigInteger, ForeignKey('Guia.no_guia'))
    nombre = Column(String)
    direccion = Column(String)
    codigo_postal = Column(BigInteger)
    ciudad = Column(String)
    estado = Column(String)
    pais = Column(String)
    telefono = Column(BigInteger)

    guia = relationship("Guia")