from pydantic import BaseModel, constr, conint, confloat


class ImpuestoBase(BaseModel):
    # id_impuesto autogenerado
    paquete_id: conint(gt=0)
    # monto_iva_dolar autocalculado
    dai_porcentaje: confloat(ge=0, le=100)
    # monto_dai_dolar autocalculado
    poliza: constr(strip_whitespace=True, min_length=1)
    partida: constr(strip_whitespace=True, min_length=1)
    consignatario: constr(strip_whitespace=True, min_length=1)
    # fecha_impuesto autogenerada

    class Config:
        from_attributes = True