from fastapi import APIRouter, UploadFile
from fastapi.responses import JSONResponse
from src.data_manipulation import excelToDictList
from src.database.db_manager import upload_paquete
from dataModels.paquete import PaqueteBase
from utils.logging import Logging
from CustomExceptions.AttributeMismatch import AttributeMismatch

excel_ops_router = APIRouter()


@excel_ops_router.post("/precarga", tags=["precarga"])
async def upload_precarga(file: UploadFile):
    logging = Logging("utils/debug.txt")

    if not file.filename.endswith(".xlsx"):
        return {"message": "Invalid file type"}

    try:
        contents = await file.read()
        dict_list = excelToDictList(contents)
        logging.log(str(dict_list))
        #PaqueteBase.validation(dict_list[0]) # valida que los atributos del diccionario sean los mismos que los del modelo

        for paquete in dict_list:
            upload_paquete(PaqueteBase(**paquete))

        return JSONResponse(content=dict_list, status_code=200)

    except AttributeMismatch as e:
        return {"message": "Invalid file format", "error": str(e)}

    # except Exception as e:
    #     return {"message": "Error uploading file", "error": str(e)}
