from pydantic import BaseModel, constr, conint


class CambioUsuarioBase(BaseModel):
    modificado_id: conint(gt=0)
    valor_previo: constr(strip_whitespace=True, min_length=1)
    valor_actual: constr(strip_whitespace=True, min_length=1)
    campo_modificado: constr(strip_whitespace=True, min_length=1)
    modificador_id: conint(gt=0)

    class Config:
        from_attributes = True