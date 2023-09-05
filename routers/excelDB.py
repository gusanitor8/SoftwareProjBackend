from fastapi import APIRouter, File, UploadFile
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, StreamingResponse
import io
from src.data_manipulation import *
from src.db_manager import *
from dataModels.AnicamView import AnicamView
from typing import List

excelDB_router = APIRouter()


@excelDB_router.post("/excel/anicam", tags = ["excelDB"])
async def create_upload_file(file: UploadFile = File(...)):
    if file.filename.endswith(".xlsx"):
        contents = await file.read()
        dictList = excelToDictList(contents)
        
        for dict in dictList:
            updateAnicamData(**dict)

        return JSONResponse(content=jsonable_encoder(dictList), status_code=201)
    else:
        return JSONResponse({"message": "Invalid file format"}, status_code=400)
     
@excelDB_router.get("/excel/anicam", tags = ["excelDB"])
async def create_download_files():
    result = getAnicamViewSql()
    df = dictListToDataframe(result)
    excel = createExcelFile(df)

    return StreamingResponse(io.BytesIO(excel), media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", headers={"Content-Disposition": "attachment; filename=prueba.xlsx"})



@excelDB_router.post("/excel/finances", tags = ["excelDB"])
async def import_finance_file(file: UploadFile = File(...)):
    if file.filename.endswith(".xlsx"):
        contents = await file.read()
        dictList = excelToDictList(contents)
        return JSONResponse(content=jsonable_encoder(dictList), status_code=201)
    else:
        return JSONResponse({"message": "Invalid file format"}, status_code=400)


@excelDB_router.get("/excel/finances", tags = ["excelDB"])
async def export_finance_files():
    result = getFinancesViewSql()
    df = dictListToDataframe(result)
    excel = createExcelFile(df)
    return StreamingResponse(io.BytesIO(excel), media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", headers={"Content-Disposition": "attachment; filename=pruebaFinance.xlsx"})