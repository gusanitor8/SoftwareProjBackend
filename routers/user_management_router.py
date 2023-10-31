from fastapi import APIRouter
from fastapi.responses import JSONResponse
from dataModels.usuario import UsuarioSelect
from src.db_auth import delete_user, alter_user_state

user_management_router = APIRouter()


@user_management_router.delete("/users", tags=["user management"])
async def delete_user(user: UsuarioSelect):
    flag = delete_user(user.email)

    if flag:
        return JSONResponse(content={"message": "User deleted"}, status_code=200)
    else:
        return JSONResponse(content={"message": "User not found"}, status_code=404)


@user_management_router.put("/users", tags=["user management"])
async def upddate_user_state(user: UsuarioSelect, state: bool):
    flag = alter_user_state(user.email, state)

    if flag:
        return JSONResponse(content={"message": "User updated"}, status_code=200)
    else:
        return JSONResponse(content={"message": "User not found"}, status_code=404)
