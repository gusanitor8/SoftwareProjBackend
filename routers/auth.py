from fastapi import APIRouter, Depends
from dataModels.usuario import UsuarioBase, UsuarioLogIn
from fastapi.responses import JSONResponse
from src.database.db_auth import get_pw_and_salt, verify_password, get_jwt_credentials, new_user, user_is_active, \
    roles_match, get_users, get_role
from middlewares.jwt_manager import create_token
from sqlalchemy.exc import IntegrityError
from middlewares.JWTBearer import jwt_bearer
from typing import Annotated
from src.Roles import Roles as Role
import json

auth_router = APIRouter()


@auth_router.post("/login", tags=["auth"])
async def login(user: UsuarioLogIn):
    is_active = user_is_active(user.email)
    if not is_active:
        return JSONResponse(content={"message": "User deactivated"}, status_code=401)

    pw_and_salt = get_pw_and_salt(user.email)

    if not pw_and_salt:
        return JSONResponse(content={"message": "User not found"}, status_code=404)

    verified = verify_password(user.password, pw_and_salt["password"], pw_and_salt["salt"])

    if verified:
        credentials = get_jwt_credentials(user.email)
        jwt_token = create_token(credentials)

        return JSONResponse(content=jwt_token, status_code=200)
    else:
        return JSONResponse(content={"message": "Invalid credentials"}, status_code=401)


@auth_router.post("/signup", tags=["auth"])
async def signup(user: UsuarioBase):
    try:
        if not user.rol:
            user.rol = "viewer"

        new_user(user.email, user.password, user.rol, user.nombre)
        return JSONResponse(content={"message": "User created"}, status_code=201)
    except IntegrityError:
        return JSONResponse(content={"message": "User already exists"}, status_code=409)


@auth_router.get("/users/permissions", tags=["auth"])
def get_user_permissions(user_id: Annotated[int, Depends(jwt_bearer)]):
    role = get_role(user_id)
    return JSONResponse(content=role, status_code=200)


@auth_router.get("/users", tags=["auth"])
def get_users_endpoint(page_num: int, user_id: Annotated[int, Depends(jwt_bearer)]):
    if not roles_match(user_id, Role.ADMIN):
        return JSONResponse(content={"message": "No cuenta con los permisos necesarios"}, status_code=401)

    users = get_users(page_num)
    return JSONResponse(content={"users": users}, status_code=200)
