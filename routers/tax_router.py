from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from typing import Annotated
from middlewares.JWTBearer import jwt_bearer
from dataModels.impuesto import ImpuestoBase
from src.database.db_tax import carga_impuestos
from src.database.db_auth import roles_match
from src.Roles import Roles


tax_router = APIRouter()


@tax_router.post("/impuesto", tags=["impuesto"])
def upload_impuesto(impuesto: ImpuestoBase, 
                    user_id: Annotated[int, Depends(jwt_bearer)]):
    if not roles_match(user_id, Roles.EDITOR) and not roles_match(user_id, Roles.ADMIN):
        return JSONResponse(content={"message": "Usuario no autorizado para CARGA IMPUESTO"}, status_code=403)
    try:
        carga_impuestos(impuesto)
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
    
    return JSONResponse(content={"message": "Carga de impuestos exitosa"}, status_code=201)