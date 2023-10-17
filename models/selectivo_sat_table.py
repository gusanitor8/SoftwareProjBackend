from config.database import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, func, CheckConstraint
from sqlalchemy.orm import relationship

class SelectivoSAT(Base):
    __tablename__ = "selectivo_sat"

    id_selectivo = Column(Integer, primary_key=True, autoincrement=True)
    consolidado_id = Column(Integer, ForeignKey('consolidado.id_consolidado'), nullable=False, unique=True)
    fecha_selectivo = Column(Date, default=func.now(), nullable=False)
    selectivo_asignado = Column(String, nullable=False)

    consolidado = relationship("consolidado")