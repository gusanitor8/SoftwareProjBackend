from fastapi import APIRouter
from dataModels.users import users
from fastapi.responses import JSONResponse
from src.db_auth import get_pw_and_salt, verify_password, get_jwt_credentials, new_user
from middlewares.jwt_manager import create_token
from sqlalchemy.exc import IntegrityError
auth_router = APIRouter()

@auth_router.post("/login", tags = ["auth"])
async def login(user: users):
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
    

@auth_router.post("/signup", tags = ["auth"])
async def signup(user: users):
    try:
        if not user.role:
            user.role = "viewer"
            
        new_user(user.email, user.password, user.role)
        return JSONResponse(content={"message": "User created"}, status_code=201)
    except IntegrityError:
        return JSONResponse(content={"message": "User already exists"}, status_code=409)