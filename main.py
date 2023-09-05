from fastapi import FastAPI
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.excelDB import excelDB_router
from routers.views import views_router
from routers.auth import auth_router
from middlewares.cors_middleware import getOrigins
from fastapi.middleware.cors import CORSMiddleware

#ORM
from models.Guia import Guia
from models.Cuscar import Cuscar
from models.Destino import Destino
from models.Facturacion import Facturacion
from models.Oea import OEA
from models.Paquete import Paquete
from models.Remitente import Remitente


app = FastAPI()
app.title = "SLI Backend API"

#CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=getOrigins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

#Error Handler
app.add_middleware(ErrorHandler)

#Routers
app.include_router(excelDB_router)
app.include_router(views_router)
app.include_router(auth_router)

#Database
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"Hello": "World"}