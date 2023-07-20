from pydantic import BaseModel

class OEABase(BaseModel):
    Numero_de_Declaracion: int
    No_guia: int
    Declaracion: str
    Selectivo: str

    class Config:
        orm_mode = True
