from config.database import Base
from sqlalchemy import Column, Integer, String

class Roles(Base):
    __tablename__ = "roles"

    roleID = Column(Integer, primary_key=True, autoincrement=True)
    nombre_rol = Column(String)