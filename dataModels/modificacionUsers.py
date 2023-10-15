from pydantic import BaseModel
from datetime import date

class ModificacionUsersBase(BaseModel):
    mod_user_id: int
    modded_user: int
    valor_anterior: str
    valor_nuevo: str
    campo_modificado: str
    fecha_cambio: date

    class Config:
        orm_mode = True