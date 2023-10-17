from pydantic import BaseModel, constr, validator
from typing import List

class PaqueteBase(BaseModel):
    id_paquete: int
    pedido_id: int
    codigo_rastreo: constr(strip_whitespace=True, min_length=1)
    contenido: constr(strip_whitespace=True, min_length=1)
    descripcion: constr(strip_whitespace=True, min_length=1)
    alto: float
    ancho: float
    largo: float
    peso_libras: float
    peso_volumetrico: float
    valor_producto_dolar: float
    unidades: int

    @validator("alto", "ancho", "largo", "peso_libras", "peso_volumetrico", "valor_producto_dolar")
    def check_float_values(cls, v):
        if v <= 0:
            raise ValueError("Value must be greater than 0")
        return v

    @validator("unidades")
    def check_unidades(cls, v):
        if v < 1:
            raise ValueError("unidades must be greater than or equal to 1")
        return v

    class Config:
        orm_mode = True