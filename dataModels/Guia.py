from pydantic import BaseModel
from datetime import date

class GuiaBase(BaseModel):
    no_guia: int
    fecha: date

    class Config:
        orm_mode = True