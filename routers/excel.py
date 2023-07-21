from fastapi import APIRouter, File, UploadFile
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, StreamingResponse
import io
from utils.data_manipulation import read_excel, make_excel

excel_router = APIRouter()


@excel_router.post("/uploadfile/", tags = ["testing"])
async def create_upload_file(file: UploadFile = File(...)):
    if file.filename.endswith(".xlsx"):
        contents = await file.read()
        df = read_excel(contents)
        return JSONResponse(content=jsonable_encoder(df), status_code=201)
    else:
        return JSONResponse({"message": "Invalid file format"}, status_code=400)
    
@excel_router.get("/uploadfiles/", tags = ["testing"])
async def create_download_files():
    excel_writer = make_excel()
    return StreamingResponse(io.BytesIO(excel_writer.getvalue()), media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", headers={"Content-Disposition": "attachment; filename=prueba.xlsx"})