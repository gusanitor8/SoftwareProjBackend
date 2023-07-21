from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from config.database import engine, Base, Session
from typing import List
from middlewares.error_handler import ErrorHandler
from routers.excel import excel_router

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
app.include_router(excel_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"Hello": "World"}


@app.get("/database", tags = ["testing"], response_model=List[GuiaModel])
def db():
    db = Session()
    result = db.query(Guia).all()
    db.close()

    if not result:
        return JSONResponse({"message": "No guides found"}, status_code=404)

    return JSONResponse(content=jsonable_encoder(result), status_code=201)
