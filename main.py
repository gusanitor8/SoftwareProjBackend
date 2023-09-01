from fastapi import FastAPI
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.excelDB import excelDB_router
from routers.views import views_router
from middlewares.cors_middleware import getOrigins
from fastapi.middleware.cors import CORSMiddleware


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

#Database
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"Hello": "World"}