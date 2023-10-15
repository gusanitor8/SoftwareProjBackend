from config.database import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

class SelectivoSAT(Base):
    __tablename__ = "selectivoSAT"

    revisionID = Column(Integer, primary_key=True, autoincrement=True)
    consolidado_id = Column(Integer, ForeignKey('consolidados.consolidadoID'))
    fecha_selectivo = Column(Date)
    selectivo = Column(String)

    consolidados = relationship("Consolidados")