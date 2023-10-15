from config.database import Base
from sqlalchemy import Column, Integer, String

class Rol(Base):
    __tablename__ = "rol"

    id_rol = Column(Integer, primary_key=True, autoincrement=True)
    rol = Column(String)