from config.database import Base
from sqlalchemy import Column, Integer, String, Date

class Consolidado(Base):
    __tablename__ = "consolidado"

    id_consolidado = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String)
    fecha_consolidacion = Column(Date)
    transportista = Column(String)