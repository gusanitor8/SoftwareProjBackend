from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from config.database import engine, Base, Session
from typing import List
from middlewares.error_handler import ErrorHandler
from routers.excelDB import excelDB_router
from routers.views import views_router

#pydantic
from dataModels.Guia import GuiaBase as GuiaModel

#ORM
from models.Guia import Guia
from models.Cuscar import Cuscar
from models.Destino import Destino
from models.Facturacion import Facturacion
from models.Oea import OEA
from models.Paquete import Paquete
from models.Remitente import Remitente


app = FastAPI()
app.title = "SoftAPI"
app.add_middleware(ErrorHandler)
app.include_router(excelDB_router)
app.include_router(views_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"Hello": "World"}