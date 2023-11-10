from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from typing import List, Annotated
from middlewares.JWTBearer import jwt_bearer
from dataModels.selectivo_sat import SelectivoSatBase
from src.database.db_sat_selective import carga_selectivo
from src.database.db_auth import roles_match
from src.Roles import Roles


sat_selective_router = APIRouter()


@sat_selective_router.post("/selectivo", tags=["selectivo_sat"])
def upload_selectivo(selectivo: SelectivoSatBase, 
                    user_id: Annotated[int, Depends(jwt_bearer)]):
    if not roles_match(user_id, Roles.EDITOR) and not roles_match(user_id, Roles.ADMIN):
        return JSONResponse(content={"message": "Usuario no autorizado para CARGA SELECTIVO"}, status_code=403)
    try:
        carga_selectivo(selectivo)

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
    
    return JSONResponse(content={"message": "Carga de Selectivo exitosa"}, status_code=201)