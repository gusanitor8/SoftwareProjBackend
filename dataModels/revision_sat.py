from pydantic import BaseModel
from datetime import date

class RevisionSatBase(BaseModel):
    id_revision: int
    selectivo_id: int
    registro_previo: str
    registro_actual: str
    usuario_id: int
    fecha_modificacion: date

    class Config:
        orm_mode = True