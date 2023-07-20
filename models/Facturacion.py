from sqlalchemy import Column, ForeignKey, String, BigInteger
from sqlalchemy.orm import relationship
from config.database import Base

class Facturacion(Base):
    __tablename__ = 'Facturacion'

    No_factura = Column(BigInteger, primary_key=True, autoincrement=True)
    No_guia = Column(BigInteger, ForeignKey('Guia.no_guia'))
    nit = Column(BigInteger)
    archivo = Column(String)

    guia = relationship("Guia")