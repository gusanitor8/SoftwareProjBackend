from pydantic import BaseModel, constr


class ConsolidadoBase(BaseModel):
    # id_consolidado autogenerado
    descripcion: constr(strip_whitespace=True, min_length=1)
    # fecha_consolidacion autogenerada
    transportista: constr(strip_whitespace=True, min_length=1)

    class Config:
        from_attributes = True