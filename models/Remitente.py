from sqlalchemy import Column, ForeignKey, String, BigInteger
from sqlalchemy.orm import relationship
from config.database import Base

class Remitente(Base):
    __tablename__ = 'Remitente'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    No_guia = Column(BigInteger, ForeignKey('Guia.no_guia'))
    REMITENTE_compania = Column(String)
    REMITENTE_contacto = Column(String)
    REMITENTE_email = Column(String)
    REMITENTE_direccion = Column(String)
    REMITENTE_codigo_postal = Column(BigInteger)
    REMITENTE_ciudad = Column(String)
    REMITENTE_estado = Column(String)
    REMITENTE_pais = Column(String)
    REMITENTE_telefono = Column(BigInteger)

    guia = relationship("Guia")
