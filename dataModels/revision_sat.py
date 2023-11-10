from pydantic import BaseModel, constr, conint, Field
from typing import Optional, Dict, Any


class RevisionSatBase(BaseModel):
    # id_revision autogenerada
    selectivo_id: conint(gt=0)
    registro_previo:  Dict[str, Any]
    registro_actual: Dict[str, Any]
    motivo_cambio: constr(strip_whitespace=True, min_length=1)
    usuario_id: Optional[conint(gt=0)] = Field(default=None)
    # fecha_modificacion autogenerada

    class Config:
        from_attributes = True