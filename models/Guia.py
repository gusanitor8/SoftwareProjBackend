from config.database import Base
from sqlalchemy import Column, BigInteger, Date

class Guia(Base):
    __tablename__ = 'Guia'

    no_guia = Column(BigInteger, primary_key=True, autoincrement=True)
    fecha = Column(Date)