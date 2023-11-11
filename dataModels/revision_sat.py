from pydantic import BaseModel, constr, conint, confloat, Field
from typing import Optional


class RevisionSatBase(BaseModel):
    # id_revision autogenerada
    nuevo_valor_paquete: Optional[confloat(gt=0)] = Field(default=None)
    nuevo_valor_dai: Optional[confloat(ge=0, le=100)] = Field(default=None)
    motivo_cambio: constr(strip_whitespace=True, min_length=1)
    usuario_id: Optional[conint(gt=0)] = Field(default=None)
    # fecha_modificacion autogenerada

    class Config:
        from_attributes = True