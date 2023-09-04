from config.database import Base
from sqlalchemy import Column, BigInteger, String, Float, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship

class Costeo(Base):
    __tablename__ = "Costeo"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    No_guia = Column(BigInteger, ForeignKey('Guia.no_guia'))
    codigo = Column(String)
    courier = Column(String)
    correlativo = Column(BigInteger)
    consignatario = Column(String)
    libras_a_facturar = Column(Float)
    peso_real_lb = Column(Float)
    peso_vol_lb = Column(Float)
    descripcion_costeo = Column(String)
    cobro_flete = Column(Float)
    ultima_milla = Column(Float)
    gestion_aduana = Column(Float)
    manejo_almacenaje = Column(Float)
    descuentos = Column(Float)
    DAI = Column(Float)
    IVA = Column(Float)

    guia = relationship("Guia")
