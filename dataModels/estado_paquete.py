from pydantic import BaseModel
from datetime import date

class EstadoPaqueteBase(BaseModel):
    procesoID: int
    estado_id: int
    paquete_id: int
    fecha_actualizacion: date

    class Config:
        orm_mode = True