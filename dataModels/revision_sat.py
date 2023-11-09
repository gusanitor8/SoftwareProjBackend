from pydantic import BaseModel, constr, conint


class RevisionSatBase(BaseModel):
    selectivo_id: conint(gt=0)
    registro_previo: constr(strip_whitespace=True, min_length=1)
    registro_actual: constr(strip_whitespace=True, min_length=1)
    usuario_id: conint(gt=0)

    class Config:
        from_attributes = True