from config.database import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

class SelectivoSAT(Base):
    __tablename__ = "selectivo_sat"

    id_selectivo = Column(Integer, primary_key=True, autoincrement=True)
    consolidado_id = Column(Integer, ForeignKey('consolidado.id_consolidado'), unique=True)
    fecha_selectivo = Column(Date)
    selectivo_asignado = Column(String)

    consolidado = relationship("consolidado")