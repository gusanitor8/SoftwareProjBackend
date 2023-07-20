from pydantic import BaseModel

class CuscarBase(BaseModel):
    id: int
    no_guia: int
    consignatorio: str
    cantidad: int
    peso_real_kg: float
    flete_usd: float
    valor_declarado_usd: float
    descripcion: str
    partida: str
    porcentaje: int
    oea_verde_roja: bool
    codigo_oea: int
    conteo_verdes: int
    conteo_rojas: int

    class Config:
        orm_mode = True
