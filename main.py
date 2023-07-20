from fastapi import FastAPI
from pydantic import BaseModel
from config.database import engine, Base, Session
from  models.Guia import Guia
from models.Cuscar import Cuscar
from models.Destino import Destino
from models.Facturacion import Facturacion
from models.Oea import OEA
from models.Paquete import Paquete
from models.Remitente import Remitente


app = FastAPI()
app.title = "My API"

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"Hello": "World"}


@app.get("/database")
def home():
    db = Session()
    result = db.query()
