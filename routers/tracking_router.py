from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from typing import List, Annotated
from middlewares.JWTBearer import jwt_bearer
from dataModels.seguimiento_paquete import SeguimientoPaqueteBase
from src.database.db_tracking import seguimiento_paquete
from src.database.db_auth import roles_match
from src.Roles import Roles

tracking_router = APIRouter()

@tracking_router.post("/seguimiento", tags=["seguimiento"])
def upload_estado(seguimiento: SeguimientoPaqueteBase,
                  user_id: Annotated[int, Depends(jwt_bearer)]):
    if not roles_match(user_id, Roles.EDITOR) and not roles_match(user_id, Roles.ADMIN):
        return JSONResponse(content={"message": "Usuario no autorizado para ACTUALIZAR ESTADO PAQUETE"}, status_code=403)
    try:
        seguimiento.usuario_id = user_id
        seguimiento_paquete(seguimiento)

    except ValueError as e:
        # Dinstincion entre errores esperados
        error_message = str(e)
        if 'integridad' in error_message:
            status_code = 409
        else:
            status_code = 400
        return JSONResponse(content={"message": error_message}, status_code=status_code)
    
    except Exception as e:
        # Manejo de otros errores
        return JSONResponse(content={"message": str(e)}, status_code=500)
    
    return JSONResponse(content={"message": "Precarga exitosa"}, status_code=201)