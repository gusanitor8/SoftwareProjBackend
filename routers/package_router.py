from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from datetime import date
from typing import List, Annotated
from middlewares.JWTBearer import jwt_bearer
from dataModels.paquete import PaqueteBase
from src.database.db_package import upload_packages
from sqlalchemy.exc import IntegrityError
from src.Roles import Roles
from src.database.db_auth import roles_match
from psycopg2.errors import UniqueViolation

package_router = APIRouter()


@package_router.post("/precarga", tags=["precarga"])
def upload_precarga(id_consolidado: int, descripcion: str, fecha: date, transportista: str, paquetes: List[PaqueteBase],
                    user_id: Annotated[int, Depends(jwt_bearer)]):
    if not roles_match(user_id, Roles.EDITOR) and not roles_match(user_id, Roles.ADMIN):
        return JSONResponse(content={"message": "Unauthorized"}, status_code=401)

    try:
        upload_packages(paquetes, id_consolidado, descripcion, fecha, transportista)

    except IntegrityError as e:
        return JSONResponse(content={"message": "Consolidado already exists"}, status_code=409)
    except Exception as e:
        return JSONResponse(content={"message": str(e)}, status_code=500)

    return JSONResponse(content={"message": "Packages uploaded"}, status_code=201)