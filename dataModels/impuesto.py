from pydantic import BaseModel, constr, conint, confloat


class ImpuestoBase(BaseModel):
    paquete_id: conint(gt=0)
    monto_iva_dolar: confloat(gt=0)
    dai_porcentaje: confloat(ge=0, le=100)
    monto_dai_dolar: confloat(gt=0)
    poliza: constr(strip_whitespace=True, min_length=1)
    partida: constr(strip_whitespace=True, min_length=1)
    consignatario: constr(strip_whitespace=True, min_length=1)

    class Config:
        from_attributes = True