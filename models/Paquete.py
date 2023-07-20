from sqlalchemy import Column, ForeignKey, Integer, String, BigInteger, Float
from sqlalchemy.orm import relationship
from config.database import Base

class Paquete(Base):
    __tablename__ = 'Paquete'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    No_guia = Column(BigInteger, ForeignKey('Guia.no_guia'))
    contenido = Column(String)
    piezas = Column(BigInteger)
    peso_libras = Column(Float)
    peso_kilos = Column(Float)
    valor_declarado = Column(Float)
    news = Column(String)
    linea_de_negocio = Column(String)
    pre_alerta = Column(String)
    guia_externa = Column(String)
    precinto = Column(String)
    largo = Column(Float)
    alto = Column(Float)
    ancho = Column(Float)
    carrier = Column(String)

    guia = relationship("Guia")
