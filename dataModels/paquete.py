from pydantic import BaseModel, constr, confloat, conint


class PaqueteBase(BaseModel):
    id_paquete: int
    pedido_id: conint(gt=0)
    codigo_rastreo: constr(strip_whitespace=True, min_length=1)
    contenido: constr(strip_whitespace=True, min_length=1)
    descripcion: constr(strip_whitespace=True, min_length=1)
    alto: confloat(gt=0)
    ancho: confloat(gt=0)
    largo: confloat(gt=0)
    peso_libras: confloat(gt=0)
    peso_volumetrico: confloat(gt=0)
    valor_producto_dolar: confloat(gt=0)
    unidades: conint(ge=1)

    class Config:
        orm_mode = True