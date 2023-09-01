from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from typing import Tuple
import traceback

class ErrorHandler(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) ->  Tuple[Response, JSONResponse]:
        try:
            return await call_next(request)
        except Exception as e:
            traceback_info = traceback.format_exc()
            return JSONResponse({"message": str(e), "traceback" : traceback_info }, status_code=500)