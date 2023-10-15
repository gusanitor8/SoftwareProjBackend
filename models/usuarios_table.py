from config.database import Base
from sqlalchemy import Column, Integer, String, Boolean

class Usuarios(Base):
    __tablename__ = "usuarios"

    userID = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    password = Column(String)
    nombre = Column(String)
    mail = Column(String)
    puesto = Column(String)
    estado = Column(Boolean)
    salt = Column(String)