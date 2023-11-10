from pydantic import BaseModel, constr, conint


class RevisionSatBase(BaseModel):
    # id_revision autogenerada
    selectivo_id: conint(gt=0)
    registro_previo: constr(strip_whitespace=True, min_length=1)
    registro_actual: constr(strip_whitespace=True, min_length=1)
    usuario_id: conint(gt=0)
    # fecha_modificacion autogenerada

    class Config:
        from_attributes = True