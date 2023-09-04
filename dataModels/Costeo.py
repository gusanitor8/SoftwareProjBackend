from pydantic import BaseModel

class CosteoBase(BaseModel):
    id: int
    No_guia: int
    codigo: str
    courier: str
    correlativo: int
    consignatario: str
    libras_a_facturar: float
    peso_real_lb: float
    peso_vol_lb: float
    descripcion_costeo: str
    cobro_flete: float
    ultima_milla: float
    gestion_aduana: float
    manejo_almacenaje: float
    descuentos: float
    DAI: float
    IVA: float

    class Config:
        orm_mode = True