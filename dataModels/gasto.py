from pydantic import BaseModel, confloat, conint


class GastoBase(BaseModel):
    # id_gasto autogenerado
    paquete_id: conint(gt=0)
    # monto_iva_quetzal autocalculado
    # monto_dai_quetzal autocalculado
    monto_flete: confloat(gt=0)
    monto_combex: confloat(gt=0)
    # valor_quetzal autocalculado
    # gasto_total autocalculado

    class Config:
        from_attributes = True