from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, BigInteger, Float
from sqlalchemy.orm import relationship
from config.database import Base

class Cuscar(Base):
    __tablename__ = 'Cuscar'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    no_guia = Column(BigInteger, ForeignKey('Guia.no_guia'))
    consignatorio = Column(String)
    cantidad = Column(BigInteger)
    peso_real_kg = Column(Float)
    flete_usd = Column(Float)
    valor_declarado_usd = Column(Float)
    descripcion = Column(String)
    partida = Column(String)
    porcentaje = Column(BigInteger)
    oea_verde_roja = Column(Boolean)
    codigo_oea = Column(BigInteger)
    conteo_verdes = Column(BigInteger)
    conteo_rojas = Column(BigInteger)

    guia = relationship("Guia")
