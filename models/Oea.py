from sqlalchemy import Column, ForeignKey, Integer, String, BigInteger
from sqlalchemy.orm import relationship
from config.database import Base

class OEA(Base):
    __tablename__ = 'OEA'

    Numero_de_Declaracion = Column(BigInteger, primary_key=True, autoincrement=True)
    No_guia = Column(BigInteger, ForeignKey('Guia.no_guia'))
    Declaracion = Column(String)
    Selectivo = Column(String)

    guia = relationship("Guia")
