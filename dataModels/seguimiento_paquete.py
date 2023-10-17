from pydantic import BaseModel, constr, validator, conint
from datetime import date

class SeguimientoPaqueteBase(BaseModel):
    id_seguimiento: conint(gt=0)
    estado_actual: constr(strip_whitespace=True, min_length=1)
    motivo_cambio: constr(strip_whitespace=True, min_length=1)
    paquete_id: conint(gt=0)
    fecha_actualizacion: date
    usuario_id: conint(gt=0)

    @validator("estado_actual")
    def check_estado_actual(cls, v):
        valid_states = ['en transito', 'en bodega', 'gestion aduana', 'liberado', 'listo', 'entregado']
        if v not in valid_states:
            raise ValueError(f"estado_actual must be one of {valid_states}")
        return v

    class Config:
        orm_mode = True
