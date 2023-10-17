from config.database import Base
from sqlalchemy import Column, Integer, String, Boolean, CheckConstraint

class Usuario(Base):
    __tablename__ = "usuario"

    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    puesto = Column(String, nullable=False)
    estado = Column(Boolean, nullable=False)
    rol = Column(String, CheckConstraint("rol in ('viewer', 'editor', 'admin')"), nullable=False)
    salt = Column(String, unique=True, nullable=False)