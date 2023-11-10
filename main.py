from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from middlewares.cors_middleware import getOrigins
from fastapi.middleware.cors import CORSMiddleware
from routers.auth import auth_router
from routers.user_management_router import user_management_router
from routers.package_router import package_router
from routers.tax_router import tax_router
from routers.expense_router import expense_router
from routers.sat_selective_router import sat_selective_router

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
app.title = "Courier Backend API"

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
app.include_router(user_management_router)
app.include_router(package_router)
app.include_router(tax_router)
app.include_router(expense_router)
app.include_router(sat_selective_router)

#Database
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return RedirectResponse("/docs")