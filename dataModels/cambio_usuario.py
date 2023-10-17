from pydantic import BaseModel, constr, conint
from datetime import date


class CambioUsuarioBase(BaseModel):
    id_cambio: int
    modificado_id: conint(gt=0)
    valor_previo: constr(strip_whitespace=True, min_length=1)
    valor_actual: constr(strip_whitespace=True, min_length=1)
    campo_modificado: constr(strip_whitespace=True, min_length=1)
    fecha_cambio: date
    modificador_id: conint(gt=0)

    class Config:
        orm_mode = True