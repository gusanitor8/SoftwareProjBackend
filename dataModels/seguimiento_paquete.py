from pydantic import BaseModel, constr, conint


class SeguimientoPaqueteBase(BaseModel):
    estado_actual: constr(strip_whitespace=True, pattern="^(en transito|en bodega|gestion aduana|liberado|listo|entregado)$")
    motivo_cambio: constr(strip_whitespace=True, min_length=1)
    paquete_id: conint(gt=0)
    usuario_id: conint(gt=0)

    class Config:
        from_attributes = True
