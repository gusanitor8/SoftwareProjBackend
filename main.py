from fastapi import FastAPI
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.auth import auth_router
from routers.excel_ops import excel_ops_router
from routers.user_management_router import user_management_router
from routers.package_router import package_router
from middlewares.cors_middleware import getOrigins
from fastapi.middleware.cors import CORSMiddleware

#ORM
from models.cambio_usuario_table import CambioUsuario
from models.consolidacion_table import Consolidacion
from models.consolidado_table import Consolidado
from models.gasto_table import Gasto
from models.impuesto_table import Impuesto
from models.paquete_table import Paquete
from models.revision_sat_table import RevisionSat
from models.seguimiento_paquete_table import SeguimientoPaquete
from models.selectivo_sat_table import SelectivoSAT
from models.usuario_table import Usuario


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
app.include_router(auth_router)
app.include_router(excel_ops_router)
app.include_router(user_management_router)
app.include_router(package_router)

#Database
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"Hello": "World"}