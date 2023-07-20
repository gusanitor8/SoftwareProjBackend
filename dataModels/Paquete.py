from pydantic import BaseModel

class PaqueteBase(BaseModel):
    id: int
    No_guia: int
    contenido: str
    piezas: int
    peso_libras: float
    peso_kilos: float
    valor_declarado: float
    news: str
    linea_de_negocio: str
    pre_alerta: str
    guia_externa: str
    precinto: str
    largo: float
    alto: float
    ancho: float
    carrier: str

    class Config:
        orm_mode = True
