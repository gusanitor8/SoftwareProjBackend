from pydantic import BaseModel
from datetime import date

class SeguimientoPaqueteBase(BaseModel):
    id_seguimiento: int
    estado_previo_id: int
    estado_actual_id: int
    paquete_id: int
    fecha_actualizacion: date

    class Config:
        orm_mode = True