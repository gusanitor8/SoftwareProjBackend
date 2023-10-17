from pydantic import BaseModel
from datetime import date

class SeguimientoPaqueteBase(BaseModel):
    id_seguimiento: int
    estado_actual: str
    motivo_cambio: str
    paquete_id: int
    fecha_actualizacion: date
    usuario_id: int

    class Config:
        orm_mode = True