from sqlalchemy import Column, ForeignKey, Integer, String, BigInteger
from sqlalchemy.orm import relationship
from config.database import Base

class Remitente(Base):
    __tablename__ = 'Remitente'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    No_guia = Column(BigInteger, ForeignKey('Guia.no_guia'))
    compania = Column(String)
    contacto = Column(String)
    email = Column(String)
    direccion = Column(String)
    codigo_postal = Column(BigInteger)
    ciudad = Column(String)
    estado = Column(String)
    pais = Column(String)
    telefono = Column(BigInteger)

    guia = relationship("Guia")
