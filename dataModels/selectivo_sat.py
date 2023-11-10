from pydantic import BaseModel, constr, conint


class SelectivoSatBase(BaseModel):
    # id_selectivo autogenerado
    consolidado_id: conint(gt=0)
    # fecha_selectivo autogenerada
    selectivo_asignado: constr(strip_whitespace=True, pattern="^(Rojo|Verde)$")

    class Config:
        from_attributes = True