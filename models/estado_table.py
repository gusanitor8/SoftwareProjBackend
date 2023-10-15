from config.database import Base
from sqlalchemy import Column, Integer, String

class Estado(Base):
    __tablename__ = "estado"

    id_estado = Column(Integer, primary_key=True, autoincrement=True)
    estado = Column(String)