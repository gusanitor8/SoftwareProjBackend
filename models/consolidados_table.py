from config.database import Base
from sqlalchemy import Column, Integer, String, Date

class Consolidados(Base):
    __tablename__ = "consolidados"

    consolidadoID = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String)
    fecha_consolidacion = Column(Date)
    carrier = Column(String)