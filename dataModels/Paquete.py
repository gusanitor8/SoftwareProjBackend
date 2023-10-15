from pydantic import BaseModel

class PaqueteBase(BaseModel):
    id_paquete: int
    pedido_id: int
    codigo_rastreo: str
    contenido: str
    descripcion: str
    alto: float
    ancho: float
    largo: float
    peso_libras: float
    peso_volumetrico: float
    valor_producto_dolar: float
    cantidad: int

    class Config:
        orm_mode = True