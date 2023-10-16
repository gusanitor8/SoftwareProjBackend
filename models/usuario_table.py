from config.database import Base
from sqlalchemy import Column, Integer, String, Boolean

class Usuario(Base):
    __tablename__ = "usuario"

    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    password = Column(String)
    nombre = Column(String)
    email = Column(String, unique=True)
    puesto = Column(String)
    estado = Column(Boolean)
    salt = Column(String, unique=True)