from config.database import Base
from sqlalchemy import Column, Integer, String

class Estados(Base):
    __tablename__ = "estados"

    estadoID = Column(Integer, primary_key=True, autoincrement=True)
    estado = Column(String)