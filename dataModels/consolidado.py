from pydantic import BaseModel, constr


class ConsolidadoBase(BaseModel):
    descripcion: constr(strip_whitespace=True, min_length=1)
    transportista: constr(strip_whitespace=True, min_length=1)

    class Config:
        from_attributes = True