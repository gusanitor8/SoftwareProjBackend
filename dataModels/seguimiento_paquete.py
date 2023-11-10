from pydantic import BaseModel, constr, conint, Field
from typing import Optional


class SeguimientoPaqueteBase(BaseModel):
    # id_seguimiento autogenerado
    estado_actual: constr(strip_whitespace=True, pattern="^(en transito|en bodega|gestion aduana|liberado|listo|entregado)$")
    motivo_cambio: constr(strip_whitespace=True, min_length=1)
    paquete_id: conint(gt=0)
    # fecha_actualizacion autogenerada
    usuario_id: Optional[conint(gt=0)] = Field(default=None)

    class Config:
        from_attributes = True