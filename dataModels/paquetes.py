from pydantic import BaseModel

class PaquetesBase(BaseModel):
    codigo_tracking: int
    invoice_id: int
    contenido: str
    descripcion: str
    alto: float
    ancho: float
    largo: float
    peso_lbs: float
    peso_vol: float
    valor_producto: float
    cantidad: int

    class Config:
        orm_mode = True