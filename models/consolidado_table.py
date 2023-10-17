from config.database import Base
from sqlalchemy import Column, Integer, String, Date, func


class Consolidado(Base):
    __tablename__ = "consolidado"

    id_consolidado = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String, nullable=False)
    fecha_consolidacion = Column(Date, default=func.now(), nullable=False)
    transportista = Column(String, nullable=False)