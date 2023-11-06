from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from dataModels.usuario import UsuarioSelect
from src.db_auth import delete_user, alter_user_state
from middlewares.JWTBearer import jwt_bearer
from middlewares.jwt_manager import validate_token
from typing import Annotated
from src.Roles import Roles
from src.db_auth import roles_match, update_user_permissions
from fastapi.security import OAuth2PasswordBearer

user_management_router = APIRouter()


@user_management_router.delete("/users", tags=["user management"])
async def delete_user_endpoint(user: UsuarioSelect, user_id: Annotated[int, Depends(jwt_bearer)]):
    if not roles_match(user_id, Roles.ADMIN):
        return JSONResponse(content={"message": "Unauthorized"}, status_code=401)

    flag = delete_user(user.email)

    if flag:
        return JSONResponse(content={"message": "User deleted"}, status_code=200)
    else:
        return JSONResponse(content={"message": "User not found"}, status_code=404)


@user_management_router.put("/users/state", tags=["user management"])
async def update_user_state(user: UsuarioSelect, state: bool, user_id: Annotated[int, Depends(jwt_bearer)]):
    if not roles_match(user_id, Roles.ADMIN):
        return JSONResponse(content={"message": "Unauthorized"}, status_code=401)

    flag = alter_user_state(user.email, state)

    if flag:
        return JSONResponse(content={"message": "User updated"}, status_code=200)
    else:
        return JSONResponse(content={"message": "User not found"}, status_code=404)


@user_management_router.post("/users/permissions", tags=["user management"])
def update_user_permissions_endpoint(user_email: str, role: str, user_id: Annotated[int, Depends(jwt_bearer)]):
    if not roles_match(user_id, Roles.ADMIN):
        return JSONResponse(content={"message": "Unauthorized"}, status_code=401)

    role_upper = role.upper()
    role_lower = role.lower()
    if role_upper in Roles.__members__:
        flag = update_user_permissions(user_email, role_lower)

        if flag:
            return JSONResponse(content={"message": "User updated"}, status_code=200)
        else:
            return JSONResponse(content={"message": "User not found"}, status_code=404)

    else:
        return JSONResponse(content={"message": "Invalid role"}, status_code=400)

