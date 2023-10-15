from pydantic import BaseModel
from datetime import date

class CambioUsuarioBase(BaseModel):
    id_cambio: int
    modificado_id: int
    valor_previo: str
    valor_actual: str
    campo_modificado: str
    fecha_cambio: date
    modificador_id: int

    class Config:
        orm_mode = True