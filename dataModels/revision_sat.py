from pydantic import BaseModel, constr, conint
from datetime import date


class RevisionSatBase(BaseModel):
    id_revision: int
    selectivo_id: conint(gt=0)
    registro_previo: constr(strip_whitespace=True, min_length=1)
    registro_actual: constr(strip_whitespace=True, min_length=1)
    usuario_id: conint(gt=0)
    fecha_modificacion: date

    class Config:
        orm_mode = True