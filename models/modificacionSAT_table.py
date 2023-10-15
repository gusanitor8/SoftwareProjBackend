from config.database import Base
from sqlalchemy import Column, Integer, String, Date

class ModificacionSAT(Base):
    __tablename__ = "modificacionSAT"

    mod_sat_id = Column(Integer, primary_key=True, autoincrement=True)
    revision = Column(Integer)
    registro_antiguo = Column(String)
    registro_nuevo = Column(String)
    fecha_modificacion = Column(Date)