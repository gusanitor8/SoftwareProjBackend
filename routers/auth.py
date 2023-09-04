from fastapi import APIRouter
from dataModels.users import users
from fastapi.responses import JSONResponse
from middlewares.hashing import verify_password
from src.db_auth import get_pw_and_salt

auth = APIRouter()

@auth.get("/login")
async def login(user: users):
    pw_and_salt = get_pw_and_salt(user.email)
    
    if not pw_and_salt:
        return JSONResponse(content={"message": "User not found"}, status_code=404)
    
    verify_password(user.password, pw_and_salt[0], pw_and_salt[1])