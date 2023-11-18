from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from typing import List, Annotated
from middlewares.JWTBearer import jwt_bearer
from dataModels.revision_sat import RevisionSatBase
from src.database.db_sat_revision import registrar_revision
from src.database.db_auth import roles_match
from src.database.db_verifications import check_red_selective
from src.Roles import Roles
from src.Selectivos import Selectivos

sat_revision_router = APIRouter()


@sat_revision_router.post("/revisionSAT", tags=["revisionSAT"])
def upload_revision(revision: RevisionSatBase, paquete_id: int,
                    user_id: Annotated[int, Depends(jwt_bearer)]):
    if not roles_match(user_id, Roles.EDITOR) and not roles_match(user_id, Roles.ADMIN):
        return JSONResponse(content={"message": "Usuario no autorizado para PRECARGA"}, status_code=403)
    if not check_red_selective(paquete_id, Selectivos.ROJO):
        return JSONResponse(content={"message": "Paquete no es parte de un selectivo ROJO"}, status_code=400)
    try:
        # Asignar id de usuario loggeado
        revision.usuario_id = user_id

        # Registrar la revision
        registrar_revision(revision, paquete_id)

    except ValueError as e:
        # Dinstincion entre errores esperados
        error_message = str(e)
        if 'integridad' in error_message:
            status_code = 409
        elif 'no encontrado' in error_message:
            status_code = 404
        else:
            status_code = 400
        return JSONResponse(content={"message": error_message}, status_code=status_code)
    
    except Exception as e:
        # Manejo de otros errores
        return JSONResponse(content={"message": str(e)}, status_code=500)
    
    return JSONResponse(content={"message": "Revision registrada con éxito"}, status_code=201)