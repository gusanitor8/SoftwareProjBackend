from config.database import Base
from sqlalchemy import Column, Integer, String, Date

class ModificacionUsers(Base):
    __tablename__ = "modificacionUsers"

    mod_user_id = Column(Integer, primary_key=True, autoincrement=True)
    modded_user = Column(Integer)
    valor_anterior = Column(String)
    valor_nuevo = Column(String)
    campo_modificado = Column(String)
    fecha_cambio = Column(Date)