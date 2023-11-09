from pydantic import BaseModel, constr, conint


class SelectivoSatBase(BaseModel):
    consolidado_id: conint(gt=0)
    selectivo_asignado: constr(strip_whitespace=True, pattern="^(Rojo|Verde)$")

    class Config:
        from_attributes = True