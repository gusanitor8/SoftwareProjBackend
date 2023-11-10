from fastapi import APIRouter
from datetime import date
from typing import List
from dataModels.paquete import PaqueteBase

package_router = APIRouter()


@package_router.post("/precarga", tags=["precarga"])
def upload_precarga(id_consolidado: int, descripcion: str, fecha: date, transportista: str, paquete: List[PaqueteBase]):
    return {"message": "Hello World"}
