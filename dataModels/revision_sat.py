from pydantic import BaseModel, constr
from datetime import date

class RevisionSatBase(BaseModel):
    id_revision: int
    selectivo_id: int
    registro_previo: constr(strip_whitespace=True, min_length=1)
    registro_actual: constr(strip_whitespace=True, min_length=1)
    usuario_id: int
    fecha_modificacion: date

    class Config:
        orm_mode = True