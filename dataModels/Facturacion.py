from pydantic import BaseModel

class FacturacionBase(BaseModel):
    No_factura: int
    No_guia: int
    nit: int
    archivo: str

    class Config:
        orm_mode = True
