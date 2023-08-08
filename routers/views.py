from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from src.db_manager import *

views_router = APIRouter()

@views_router.get("/views/anicam/", tags = ["views"])
async def get_anicam_view():
    result = getAnicamView()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@views_router.get("/views/cuscar/", tags = ["views"])
async def get_cuscar_view():
    result = getCuscarView()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)
